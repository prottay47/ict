import os
import re
import glob
import json
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dsa_base import DSA_KEYWORDS_REGEX, EXCLUDE_TERMS, clean_text

def get_exam_meta_from_jobqns(filepath, content):
    filename = os.path.basename(filepath)
    title = ""
    year = ""
    for l in content.splitlines()[:15]:
        if l.startswith('# '):
            title = l.replace('# ', '').strip()
            break
    if not title:
        title = filename.replace('.md', '').split('_', 1)[-1]
        
    m = re.search(r'\b(201\d|202\d)\b', title)
    if not m:
        m = re.search(r'\b(201\d|202\d)\b', filename)
    year = m.group(1) if m else "Unknown"
    
    # Check exam taker
    taker = "Unknown"
    taker_m = re.search(r'Exam\s*Taker\s*:\s*([A-Za-z0-9]+)', content, re.I)
    if taker_m:
        taker = taker_m.group(1)
    elif 'BUET' in content[:1000]:
        taker = 'BUET'
    elif 'BIBM' in content[:1000]:
        taker = 'BIBM'
    elif 'KUET' in content[:1000]:
        taker = 'KUET'
    elif 'DU' in content[:1000]:
        taker = 'DU'
        
    return title, year, taker

def get_exam_meta_from_duronto(filepath, content):
    filename = os.path.basename(filepath)
    title = ""
    year = ""
    taker = "Unknown"
    
    for l in content.splitlines()[:15]:
        if l.startswith('# '):
            title = l.replace('# ', '').strip()
            break
            
    m = re.search(r'\b(201\d|202\d)\b', title)
    if not m:
        m = re.search(r'\b(201\d|202\d)\b', filename)
    year = m.group(1) if m else "Unknown"
    
    # check metadata table
    taker_m = re.search(r'\*\*Exam\s*Taker\*\*\s*\|\s*([^|\n]+)', content, re.I)
    if taker_m:
        taker = taker_m.group(1).strip()
    else:
        taker_m2 = re.search(r'Exam\s*Taker\s*:\s*([A-Za-z0-9]+)', content, re.I)
        if taker_m2:
            taker = taker_m2.group(1).strip()
            
    return title, year, taker

def extract_questions_jobqns(filepath):
    # Skip MCQ only files
    if '(MCQ)' in filepath or '(mcq)' in filepath:
        return []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    title, year, taker = get_exam_meta_from_jobqns(filepath, content)
    
    questions = []
    
    # Pattern 1: \n(\d+)\s*\n([A-Z][A-Za-z &,/]+)\s*\n
    p1 = list(re.finditer(r'\n(?=(\d+)\s*\n([A-Z][A-Za-z &,/]+)\s*\n)', content))
    if len(p1) >= 2:
        for i in range(len(p1)):
            start = p1[i].start()
            end = p1[i+1].start() if i+1 < len(p1) else len(content)
            q_chunk = content[start:end].strip()
            questions.append({
                'source': 'JobQns',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'chunk': q_chunk
            })
        return questions

    # Pattern 2: #### Question \d+ or #### \d+\.
    p2 = list(re.finditer(r'\n(?=#{2,4}\s*(?:Question\s*\d+|\d+[\.\)]))', content, re.I))
    if len(p2) >= 2:
        for i in range(len(p2)):
            start = p2[i].start()
            end = p2[i+1].start() if i+1 < len(p2) else len(content)
            q_chunk = content[start:end].strip()
            questions.append({
                'source': 'JobQns',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'chunk': q_chunk
            })
        return questions

    # Pattern 3: \n\d+[\.\)]\s+
    p3 = list(re.finditer(r'\n(?=(?:\*{0,2}\d+[\.\)]\*{0,2}\s+[A-Za-z]))', content))
    if len(p3) >= 2:
        for i in range(len(p3)):
            start = p3[i].start()
            end = p3[i+1].start() if i+1 < len(p3) else len(content)
            q_chunk = content[start:end].strip()
            questions.append({
                'source': 'JobQns',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'chunk': q_chunk
            })
        return questions
        
    return questions

def extract_questions_duronto(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    title, year, taker = get_exam_meta_from_duronto(filepath, content)
    questions = []
    
    # Body after first ---
    body = content.split('---', 1)[-1] if '---' in content else content
    
    # Pattern 1: Table rows like | 1 | ... | or | 1<br> | ... |
    p_table = list(re.finditer(r'\n(?=\|\s*\d+(?:<br>)?\s*\|)', body))
    if len(p_table) >= 2:
        for i in range(len(p_table)):
            start = p_table[i].start()
            end = p_table[i+1].start() if i+1 < len(p_table) else len(body)
            chunk = body[start:end].strip()
            questions.append({
                'source': 'Duronto IT',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'chunk': chunk
            })
        return questions

    # Pattern 2: \n\d+[\.\)]\s+ or **\d+[\.\)]**
    p_num = list(re.finditer(r'\n(?=(?:\|?\s*(?:\*{0,2}\d+[\.\)]\*{0,2}|#{2,6}\s+\*{0,2}\d+[\.\)]\*{0,2})\s*))', body))
    if len(p_num) >= 2:
        for i in range(len(p_num)):
            start = p_num[i].start()
            end = p_num[i+1].start() if i+1 < len(p_num) else len(body)
            chunk = body[start:end].strip()
            questions.append({
                'source': 'Duronto IT',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'chunk': chunk
            })
        return questions
        
    return questions

if __name__ == '__main__':
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)
    
    all_job = []
    for f in jobqns_files:
        all_job.extend(extract_questions_jobqns(f))
        
    all_dur = []
    for f in duronto_files:
        all_dur.extend(extract_questions_duronto(f))
        
    print(f'Total segmented JobQns questions: {len(all_job)}')
    print(f'Total segmented Duronto questions: {len(all_dur)}')
