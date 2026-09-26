import os
import re
import glob
import json

def parse_jobqns_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Extract exam title and year
    lines = content.splitlines()
    title = ""
    year = ""
    for l in lines[:10]:
        if l.startswith('# '):
            title = l.replace('# ', '').strip()
            break
    
    # Try finding year in title or filename
    year_match = re.search(r'\b(201\d|202\d)\b', title)
    if not year_match:
        year_match = re.search(r'\b(201\d|202\d)\b', filepath)
    year = year_match.group(1) if year_match else "Unknown"

    questions = []
    
    # Check if file uses '- ☆' format
    if '- ☆' in content:
        parts = re.split(r'\n-\s*☆\s*\n', content)
        # part 0 is header
        for p in parts[1:]:
            p_strip = p.strip()
            if not p_strip: continue
            questions.append({
                'source_file': filepath,
                'source_type': 'JobQns',
                'exam_title': title,
                'year': year,
                'raw_content': p_strip
            })
    # Check if file uses '#### Question' or similar markdown headers
    elif re.search(r'\n#{2,4}\s+(?:Question|\d+\.|\d+\)|\b[A-Z])', content):
        # Split by header 2, 3, or 4
        parts = re.split(r'\n(?=#{2,4}\s+)', content)
        for p in parts[1:]:
            p_strip = p.strip()
            if not p_strip: continue
            # Avoid the first top-level metadata
            if p_strip.startswith('# ') or 'Original URL:' in p_strip:
                continue
            questions.append({
                'source_file': filepath,
                'source_type': 'JobQns',
                'exam_title': title,
                'year': year,
                'raw_content': p_strip
            })
    # Check if numbered list '1. ' or '1) ' at line start
    elif re.search(r'\n(?:\d+[\.\)]\s+)', content):
        parts = re.split(r'\n(?=\d+[\.\)]\s+)', content)
        for p in parts[1:]:
            p_strip = p.strip()
            if not p_strip: continue
            questions.append({
                'source_file': filepath,
                'source_type': 'JobQns',
                'exam_title': title,
                'year': year,
                'raw_content': p_strip
            })
    else:
        # Fallback: treat sections after --- as content
        body = content.split('---', 1)[-1].strip()
        if body:
            questions.append({
                'source_file': filepath,
                'source_type': 'JobQns',
                'exam_title': title,
                'year': year,
                'raw_content': body
            })
            
    return questions

def parse_duronto_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.splitlines()
    title = ""
    for l in lines[:10]:
        if l.startswith('# '):
            title = l.replace('# ', '').strip()
            break
            
    year_match = re.search(r'\b(201\d|202\d)\b', title)
    if not year_match:
        year_match = re.search(r'\b(201\d|202\d)\b', filepath)
    year = year_match.group(1) if year_match else "Unknown"

    # In duronto, skip the header table and look after ---
    body = content.split('---', 1)[-1].strip() if '---' in content else content
    
    questions = []
    # Check if table rows | 1) ... | or | 1. ... |
    # or numbered items
    if re.search(r'(?:^|\n)\s*(?:\|\s*)?(?:\*{0,2}\d+[\.\)]\*{0,2}|#{2,6}\s+\*{0,2}\d+[\.\)])', body):
        parts = re.split(r'\n(?=\s*(?:\|\s*)?(?:\*{0,2}\d+[\.\)]\*{0,2}|#{2,6}\s+\*{0,2}\d+[\.\)]))', body)
        for p in parts:
            p_strip = p.strip()
            if not p_strip: continue
            questions.append({
                'source_file': filepath,
                'source_type': 'Duronto',
                'exam_title': title,
                'year': year,
                'raw_content': p_strip
            })
    else:
        # split by paragraphs or double newlines
        parts = re.split(r'\n\s*\n', body)
        for p in parts:
            p_strip = p.strip()
            if len(p_strip) > 40:
                questions.append({
                    'source_file': filepath,
                    'source_type': 'Duronto',
                    'exam_title': title,
                    'year': year,
                    'raw_content': p_strip
                })
                
    return questions

if __name__ == '__main__':
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)
    
    all_jobqns_q = []
    for f in jobqns_files:
        all_jobqns_q.extend(parse_jobqns_file(f))
        
    all_duronto_q = []
    for f in duronto_files:
        all_duronto_q.extend(parse_duronto_file(f))
        
    print(f'JobQns questions parsed: {len(all_jobqns_q)}')
    print(f'Duronto questions parsed: {len(all_duronto_q)}')
