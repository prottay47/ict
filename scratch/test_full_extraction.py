import os
import re
import glob
import json
import sys

sys.path.insert(0, os.path.dirname(__file__))
from cleaner_helpers import clean_markdown_text, normalize_question_fingerprint
from test_topic_classifier import TOPIC_RULES, GLOBAL_EXCLUDES, classify_chunk
from test_segmentation import get_exam_meta_from_jobqns, get_exam_meta_from_duronto
from refinements import is_cybersecurity_hashing, is_network_routing

sys.stdout.reconfigure(encoding='utf-8')

def parse_jobqns_thorough(filepath):
    if '(MCQ)' in filepath or '(mcq)' in filepath:
        return []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Filter out pure MCQ files even if not named MCQ
    if 'Here Total Question: 25 To show all question with answer click' in content or 'Correct Answer:' in content and 'Explanation:' in content:
        # Check if it has 4 multiple choices on almost every question
        options_count = len(re.findall(r'\n[A-D]\)\s+', content)) + len(re.findall(r'\n\s*None\s*\n', content))
        if options_count > 15:
            return []

    title, year, taker = get_exam_meta_from_jobqns(filepath, content)

    # Split protecting code blocks
    # Replace code blocks with placeholders temporarily
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    
    masked_content = re.sub(r'```.*?```', save_cb, content, flags=re.DOTALL)
    
    # Try different split strategies
    raw_chunks = []
    
    # Strategy A: \n(\d+)\s*\n([A-Z][A-Za-z &,/]+)\s*\n
    matches_a = list(re.finditer(r'\n(?=(\d+)\s*\n([A-Z][A-Za-z &,/]+)\s*\n)', masked_content))
    if len(matches_a) >= 2:
        for i in range(len(matches_a)):
            st = matches_a[i].start()
            en = matches_a[i+1].start() if i+1 < len(matches_a) else len(masked_content)
            raw_chunks.append(masked_content[st:en])
    else:
        # Strategy B: #### Question \d+ or #### \d+\.
        matches_b = list(re.finditer(r'\n(?=#{2,4}\s*(?:Question\s*\d+|\d+[\.\)]))', masked_content, re.I))
        if len(matches_b) >= 2:
            for i in range(len(matches_b)):
                st = matches_b[i].start()
                en = matches_b[i+1].start() if i+1 < len(matches_b) else len(masked_content)
                raw_chunks.append(masked_content[st:en])
        else:
            # Strategy C: \n\d+[\.\)]\s+[A-Za-z]
            matches_c = list(re.finditer(r'\n(?=(?:\*{0,2}\d+[\.\)]\*{0,2}\s+[A-Z][a-zA-Z]))', masked_content))
            if len(matches_c) >= 2:
                for i in range(len(matches_c)):
                    st = matches_c[i].start()
                    en = matches_c[i+1].start() if i+1 < len(matches_c) else len(masked_content)
                    raw_chunks.append(masked_content[st:en])
            else:
                # Strategy D: split by --- or sections
                parts = masked_content.split('---')
                if len(parts) > 1:
                    raw_chunks.extend(parts[1:])
                else:
                    raw_chunks.append(masked_content)

    # Restore code blocks and format
    questions = []
    for chunk in raw_chunks:
        # restore code blocks
        for idx, cb in enumerate(code_blocks):
            chunk = chunk.replace(f"__CODE_BLOCK_{idx}__", cb)
        chunk = clean_markdown_text(chunk)
        if len(chunk.strip()) > 30:
            questions.append({
                'source': 'JobQns',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'content': chunk.strip()
            })
    return questions

def parse_duronto_thorough(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    title, year, taker = get_exam_meta_from_duronto(filepath, content)
    body = content.split('---', 1)[-1] if '---' in content else content

    # Split protecting code blocks
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    
    masked_body = re.sub(r'```.*?```', save_cb, body, flags=re.DOTALL)
    
    raw_chunks = []
    # Check table rows like \n|\s*\d+
    matches_table = list(re.finditer(r'\n(?=\|\s*\d+(?:<br>)?\s*\|)', masked_body))
    if len(matches_table) >= 2:
        for i in range(len(matches_table)):
            st = matches_table[i].start()
            en = matches_table[i+1].start() if i+1 < len(matches_table) else len(masked_body)
            raw_chunks.append(masked_body[st:en])
    else:
        # Check numbered items
        matches_num = list(re.finditer(r'\n(?=(?:\|?\s*(?:\*{0,2}\d+[\.\)]\*{0,2}|#{2,6}\s+\*{0,2}\d+[\.\)]\*{0,2})\s*))', masked_body))
        if len(matches_num) >= 2:
            for i in range(len(matches_num)):
                st = matches_num[i].start()
                en = matches_num[i+1].start() if i+1 < len(matches_num) else len(masked_body)
                raw_chunks.append(masked_body[st:en])
        else:
            # Fallback
            parts = masked_body.split('\n\n')
            raw_chunks.extend(parts)

    questions = []
    for chunk in raw_chunks:
        for idx, cb in enumerate(code_blocks):
            chunk = chunk.replace(f"__CODE_BLOCK_{idx}__", cb)
        chunk = clean_markdown_text(chunk)
        if len(chunk.strip()) > 30:
            questions.append({
                'source': 'Duronto IT',
                'file': filepath,
                'exam_title': title,
                'year': year,
                'taker': taker,
                'content': chunk.strip()
            })
    return questions

def run_extraction():
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)

    all_raw = []
    for f in jobqns_files:
        all_raw.extend(parse_jobqns_thorough(f))
    for f in duronto_files:
        all_raw.extend(parse_duronto_thorough(f))

    print(f'Total raw questions parsed: {len(all_raw)}')

    # Filter and classify
    dsa_candidates = []
    for item in all_raw:
        c = item['content']
        # Refinement checks
        if is_cybersecurity_hashing(c):
            continue
        if is_network_routing(c):
            continue
            
        topic = classify_chunk(c)
        if topic:
            item['topic'] = topic
            dsa_candidates.append(item)

    print(f'Total DSA questions matched before de-duplication: {len(dsa_candidates)}')

    # De-duplicate across same/similar questions
    # Group by fingerprint
    unique_dsa = []
    seen_fp = {}

    for item in dsa_candidates:
        # Extract first 2-3 sentences of question
        lines = [l.strip() for l in item['content'].splitlines() if l.strip() and not l.strip().startswith('#') and not re.match(r'^\d+\s*$', l.strip())]
        core_q = " ".join(lines[:3])
        fp = normalize_question_fingerprint(core_q)
        
        if len(fp) < 15:
            # too short, use full content
            fp = normalize_question_fingerprint(item['content'])

        if fp in seen_fp:
            # Merge sources if from different source
            existing = seen_fp[fp]
            if item['source'] not in existing['sources']:
                existing['sources'].append(item['source'])
                existing['exam_mentions'].append(f"{item['exam_title']} ({item['year']})")
                # Keep the longer, more complete content (with solution)
                if len(item['content']) > len(existing['content']):
                    existing['content'] = item['content']
        else:
            item['sources'] = [item['source']]
            item['exam_mentions'] = [f"{item['exam_title']} ({item['year']})"]
            seen_fp[fp] = item
            unique_dsa.append(item)

    print(f'Unique DSA questions after de-duplication: {len(unique_dsa)}')

    from collections import Counter
    topic_counts = Counter([q['topic'] for q in unique_dsa])
    print('\nBreakdown by Topic:')
    for t, cnt in topic_counts.most_common():
        print(f'  {t}: {cnt}')

    return unique_dsa

if __name__ == '__main__':
    res = run_extraction()
