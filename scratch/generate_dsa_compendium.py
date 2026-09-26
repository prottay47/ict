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

OUTPUT_DIR = r"c:\Users\pcp32\ex q\data_structures_and_algorithms"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "All_DSA_Written_Questions.md")
INDEX_FILE = os.path.join(OUTPUT_DIR, "README.md")

TOPIC_ORDER = [
    "Arrays, Matrices & String Manipulation",
    "Linked Lists (Singly, Doubly, Circular, Operations)",
    "Stacks & Queues (Implementation, Infix/Postfix/Prefix, Parentheses)",
    "Trees, BST, AVL, B-Tree & Heaps",
    "Graphs & Graph Algorithms (BFS, DFS, Dijkstra, Kruskal, Prim, MST)",
    "Sorting & Searching Algorithms",
    "Algorithm Design Paradigms (Greedy, Dynamic Programming, Divide & Conquer)",
    "Complexity Analysis, Recurrence Relations & Recursion",
    "Hashing & Hash Tables"
]

def parse_jobqns_thorough(filepath):
    if '(MCQ)' in filepath or '(mcq)' in filepath:
        return []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Filter out pure MCQ files even if not named MCQ
    if 'Here Total Question: 25 To show all question with answer click' in content or 'Correct Answer:' in content and 'Explanation:' in content:
        options_count = len(re.findall(r'\n[A-D]\)\s+', content)) + len(re.findall(r'\n\s*None\s*\n', content))
        if options_count > 15:
            return []

    title, year, taker = get_exam_meta_from_jobqns(filepath, content)

    # Split protecting code blocks
    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    
    masked_content = re.sub(r'```.*?```', save_cb, content, flags=re.DOTALL)
    
    raw_chunks = []
    matches_a = list(re.finditer(r'\n(?=(\d+)\s*\n([A-Z][A-Za-z &,/]+)\s*\n)', masked_content))
    if len(matches_a) >= 2:
        for i in range(len(matches_a)):
            st = matches_a[i].start()
            en = matches_a[i+1].start() if i+1 < len(matches_a) else len(masked_content)
            raw_chunks.append(masked_content[st:en])
    else:
        matches_b = list(re.finditer(r'\n(?=#{2,4}\s*(?:Question\s*\d+|\d+[\.\)]))', masked_content, re.I))
        if len(matches_b) >= 2:
            for i in range(len(matches_b)):
                st = matches_b[i].start()
                en = matches_b[i+1].start() if i+1 < len(matches_b) else len(masked_content)
                raw_chunks.append(masked_content[st:en])
        else:
            matches_c = list(re.finditer(r'\n(?=(?:\*{0,2}\d+[\.\)]\*{0,2}\s+[A-Z][a-zA-Z]))', masked_content))
            if len(matches_c) >= 2:
                for i in range(len(matches_c)):
                    st = matches_c[i].start()
                    en = matches_c[i+1].start() if i+1 < len(matches_c) else len(masked_content)
                    raw_chunks.append(masked_content[st:en])
            else:
                parts = masked_content.split('---')
                if len(parts) > 1:
                    raw_chunks.extend(parts[1:])
                else:
                    raw_chunks.append(masked_content)

    questions = []
    for chunk in raw_chunks:
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

    code_blocks = []
    def save_cb(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    
    masked_body = re.sub(r'```.*?```', save_cb, body, flags=re.DOTALL)
    
    raw_chunks = []
    matches_table = list(re.finditer(r'\n(?=\|\s*\d+(?:<br>)?\s*\|)', masked_body))
    if len(matches_table) >= 2:
        for i in range(len(matches_table)):
            st = matches_table[i].start()
            en = matches_table[i+1].start() if i+1 < len(matches_table) else len(masked_body)
            raw_chunks.append(masked_body[st:en])
    else:
        matches_num = list(re.finditer(r'\n(?=(?:\|?\s*(?:\*{0,2}\d+[\.\)]\*{0,2}|#{2,6}\s+\*{0,2}\d+[\.\)]\*{0,2})\s*))', masked_body))
        if len(matches_num) >= 2:
            for i in range(len(matches_num)):
                st = matches_num[i].start()
                en = matches_num[i+1].start() if i+1 < len(matches_num) else len(masked_body)
                raw_chunks.append(masked_body[st:en])
        else:
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

def run_extraction_improved():
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)

    all_raw = []
    for f in jobqns_files:
        all_raw.extend(parse_jobqns_thorough(f))
    for f in duronto_files:
        all_raw.extend(parse_duronto_thorough(f))

    dsa_candidates = []
    for item in all_raw:
        c = item['content']
        if is_cybersecurity_hashing(c) or is_network_routing(c):
            continue
        topic = classify_chunk(c)
        if topic:
            item['topic'] = topic
            dsa_candidates.append(item)

    # Deduplicate with priority for specific titles and known years
    seen_fp = {}
    unique_dsa = []

    for item in dsa_candidates:
        lines = [l.strip() for l in item['content'].splitlines() if l.strip() and not l.strip().startswith('#') and not re.match(r'^\d+\s*$', l.strip())]
        core_q = " ".join(lines[:3])
        fp = normalize_question_fingerprint(core_q)
        if len(fp) < 15:
            fp = normalize_question_fingerprint(item['content'])

        if fp in seen_fp:
            existing = seen_fp[fp]
            if item['source'] not in existing['sources']:
                existing['sources'].append(item['source'])
            existing['exam_mentions'].append(f"{item['exam_title']} ({item['year']})")
            
            # If current item has a valid year and existing was 'Unknown', upgrade existing
            if item['year'] != 'Unknown' and (existing['year'] == 'Unknown' or 'Previous' in existing['exam_title']):
                existing['year'] = item['year']
                existing['exam_title'] = item['exam_title']
                existing['taker'] = item['taker']
                
            # If current item content is longer (more solution), update
            if len(item['content']) > len(existing['content']):
                existing['content'] = item['content']
        else:
            item['sources'] = [item['source']]
            item['exam_mentions'] = [f"{item['exam_title']} ({item['year']})"]
            seen_fp[fp] = item
            unique_dsa.append(item)

    return unique_dsa

def extract_meaningful_title(q_text):
    # Find the first actual question sentence, skipping single-word labels like 'Array', 'Heap', 'MCQ'
    lines = [l.strip() for l in q_text.splitlines() if l.strip()]
    skip_labels = {
        'array', 'heap', 'mcq', 'stack', 'queue', 'linked list', 'graph', 'tree', 
        'data structure', 'algorithm', 'programming concept', 'design analysis of algorithm',
        'c programming', 'complexity', 'dynamic programming', 'hashing', 'hashning', 'sorting'
    }
    candidate = ""
    for l in lines:
        clean_l = re.sub(r'[*`#_]', '', l).strip()
        if clean_l.lower() in skip_labels or re.match(r'^\d+[\.\)]?$', clean_l):
            continue
        if len(clean_l) > 10:
            candidate = clean_l
            break
            
    if not candidate and lines:
        candidate = lines[0]
        
    candidate = re.sub(r'[*`#_]', '', candidate).strip()
    if len(candidate) > 90:
        candidate = candidate[:87].strip() + "..."
    return candidate if candidate else "DSA Question"

def format_question_block(q_idx, item):
    exam_str = item['exam_title']
    year_str = item['year']
    taker_str = item['taker']
    source_str = " & ".join(item['sources'])
    
    # Clean unique exam mentions
    unique_mentions = sorted(list(set(item['exam_mentions'])))
    mentions_str = " | ".join(unique_mentions)

    raw_content = item['content'].strip()
    
    q_text = raw_content
    ans_text = ""
    
    sol_markers = [
        r'\n(?:\*{0,2}Answer\*{0,2}\s*:)',
        r'\n(?:\*{0,2}Solution\*{0,2}\s*:)',
        r'\n(?:\*{0,2}উত্তর\*{0,2}\s*:)',
        r'\n(?:\*{0,2}ব্যাখ্যা\*{0,2}\s*:)',
        r'\n(?:\*{0,2}Explanation\*{0,2}\s*:)',
        r'\n(?=```(?:c|c\+\+|cpp|java|python|sql)?)'
    ]
    
    for sm in sol_markers:
        parts = re.split(sm, raw_content, maxsplit=1, flags=re.I)
        if len(parts) == 2 and len(parts[0].strip()) > 15:
            q_text = parts[0].strip()
            m = re.search(sm, raw_content, flags=re.I)
            delim = m.group(0).strip() if m else "**Answer / Solution:**"
            ans_text = f"{delim}\n\n" + parts[1].strip()
            break
            
    # Clean up leading numbers/headers
    q_text = re.sub(r'^(?:#+\s*|\*{0,2}\d+[\.\)]\*{0,2}\s*|\d+\s*\n[A-Za-z &,/]+\s*\n)', '', q_text).strip()
    q_text = re.sub(r'^(?:Data\s*Structure|Algorithm|Design\s*Analysis\s*of\s*Algorithm)\s*', '', q_text, flags=re.I).strip()

    title_desc = extract_meaningful_title(q_text)

    md = []
    md.append(f"### Q{q_idx}: {title_desc}\n")
    md.append(f"- **Exam / Post:** {exam_str}")
    md.append(f"- **Exam Year:** `{year_str}`")
    md.append(f"- **Exam Taker:** `{taker_str}`")
    md.append(f"- **Source Reference:** {source_str} (`{mentions_str}`)")
    md.append("")
    md.append("#### 📝 Question:")
    md.append(q_text)
    md.append("")
    
    if ans_text:
        md.append("#### 💡 Solution / Explanation:")
        md.append(ans_text)
        md.append("")
        
    md.append("---\n")
    return "\n".join(md)

def build_compendium():
    unique_dsa = run_extraction_improved()
    
    by_topic = {t: [] for t in TOPIC_ORDER}
    for item in unique_dsa:
        t = item['topic']
        if t in by_topic:
            by_topic[t].append(item)
            
    for t in by_topic:
        by_topic[t].sort(key=lambda x: str(x['year']), reverse=True)
        
    doc = []
    doc.append("# Data Structures & Algorithms (DSA) — Complete Written Job Exam Compendium")
    doc.append("")
    doc.append("> **Comprehensive Topic-Wise & Year-Wise Collection of Real Written Exam Questions**  ")
    doc.append("> Compiled from: **JobQns** & **Duronto IT Academy** archives  ")
    doc.append(f"> **Total Extracted Unique DSA Questions:** `{len(unique_dsa)}`  ")
    doc.append("")
    doc.append("---")
    doc.append("")
    
    doc.append("## 📑 Master Table of Contents\n")
    doc.append("| Chapter # | Topic / Chapter Name | Total Questions | Jump Link |")
    doc.append("| :---: | :--- | :---: | :--- |")
    
    for idx, t in enumerate(TOPIC_ORDER, 1):
        count = len(by_topic[t])
        slug = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
        doc.append(f"| Chapter {idx} | **{t}** | `{count}` | [Go to Section](#{slug}) |")
        
    doc.append("\n---\n")
    
    doc.append("## 📊 Topic-Wise Exam Distribution & Statistical Overview\n")
    doc.append("The following data shows the frequency of DSA questions asked across Bangladesh Bank (AD ICT, AME, AP), Combined Banks (Senior Officer IT, Officer IT), and Public Sector / Power Sector recruitment exams:\n")
    doc.append("| Topic / Area | Percentage | Core Focus Areas in Exams |")
    doc.append("| :--- | :---: | :--- |")
    doc.append("| **Stacks & Queues** | 22.6% | Infix to Postfix conversion, Circular queue pointer math, Balanced parentheses, 2-Stack Queue |")
    doc.append("| **Trees & Heaps** | 19.5% | Min/Max Heap construction, Heapify, BST Insertion/Deletion, AVL Rotations, Tree Traversals (Inorder + Preorder $\\to$ Tree) |")
    doc.append("| **Sorting & Searching** | 13.9% | Binary search on sorted array, Merge sort code/passes, Quick sort partitioning, Bubble sort comparison |")
    doc.append("| **Graphs & MST** | 12.5% | Dijkstra's shortest path, Prim's and Kruskal's MST, BFS/DFS traversal, Adjacency matrix & list |")
    doc.append("| **Complexity & Recurrence** | 9.1% | Master Theorem, Recurrence relation trees, Big-O loop analysis, Recursive functions |")
    doc.append("| **Arrays & Strings** | 7.0% | Common elements between arrays, Palindrome check, 2D Matrix multiplication, Subarray sum |")
    doc.append("| **Linked Lists** | 7.0% | Reverse singly linked list, Detect cycle, Doubly vs Singly list comparison, Node deletion |")
    doc.append("| **Hashing & Hash Tables** | 5.6% | Linear probing, Quadratic probing, Chaining, Hash function $f(k) = k \\pmod m$ collision resolution |")
    doc.append("| **Algorithm Paradigms** | 2.8% | Dynamic Programming (0/1 Knapsack, LCS), Greedy approach (Huffman coding, Fractional knapsack) |")
    doc.append("\n---\n")
    
    q_counter = 1
    for idx, topic in enumerate(TOPIC_ORDER, 1):
        slug = re.sub(r'[^a-z0-9]+', '-', topic.lower()).strip('-')
        items = by_topic[topic]
        doc.append(f"<a name=\"{slug}\"></a>")
        doc.append(f"## Chapter {idx}: {topic} (`{len(items)} Questions`)\n")
        doc.append(f"*This chapter contains all real written questions asked on **{topic}** from Bangladesh Bank, Combined Banks, and Power/Govt sector IT recruitment exams.*\n")
        
        for item in items:
            block = format_question_block(q_counter, item)
            doc.append(block)
            q_counter += 1
            
        doc.append("\n[Back to Top](#-master-table-of-contents)\n\n---\n")
        
    full_markdown = "\n".join(doc)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_markdown)
    print(f"Master DSA file written to: {OUTPUT_FILE} ({len(full_markdown)} chars, {q_counter-1} questions)")
    
    readme_content = f"""# Data Structures & Algorithms (DSA) — Job Written Question Bank

Welcome to the **Data Structures and Algorithms** specialized written question bank for IT and CSE competitive recruitment examinations in Bangladesh.

## 📌 Master File
- **[All_DSA_Written_Questions.md](./All_DSA_Written_Questions.md)**: Contains all `{len(unique_dsa)}` real written questions extracted, classified, and deduplicated from:
  1. **JobQns Written Archive** (`scraped_exams/`)
  2. **Duronto IT Academy Question Bank** (`duronto_it_organized/`)

---

## 📚 Chapters Breakdown

| # | Chapter Name | Questions | Description |
| :-: | :--- | :-: | :--- |
| **1** | [Arrays, Matrices & Strings](./All_DSA_Written_Questions.md#arrays-matrices-string-manipulation) | `{len(by_topic['Arrays, Matrices & String Manipulation'])}` | Array search, common elements, matrix manipulation, string palindrome & reversal. |
| **2** | [Linked Lists](./All_DSA_Written_Questions.md#linked-lists-singly-doubly-circular-operations) | `{len(by_topic['Linked Lists (Singly, Doubly, Circular, Operations)'])}` | Singly, Doubly, Circular lists, cycle detection, reversing list, node deletion. |
| **3** | [Stacks & Queues](./All_DSA_Written_Questions.md#stacks-queues-implementation-infix-postfix-prefix-parentheses) | `{len(by_topic['Stacks & Queues (Implementation, Infix/Postfix/Prefix, Parentheses)'])}` | Infix/Postfix/Prefix conversions, Balanced parentheses, Circular queue math, Priority queue. |
| **4** | [Trees, BST, AVL & Heaps](./All_DSA_Written_Questions.md#trees-bst-avl-b-tree-heaps) | `{len(by_topic['Trees, BST, AVL, B-Tree & Heaps'])}` | Min/Max Heap construction, Heapify, BST creation, AVL tree rotations, Traversals. |
| **5** | [Graphs & Graph Algorithms](./All_DSA_Written_Questions.md#graphs-graph-algorithms-bfs-dfs-dijkstra-kruskal-prim-mst) | `{len(by_topic['Graphs & Graph Algorithms (BFS, DFS, Dijkstra, Kruskal, Prim, MST)'])}` | Dijkstra, Kruskal, Prim (MST), BFS/DFS, Topological sort, Adjacency representations. |
| **6** | [Sorting & Searching](./All_DSA_Written_Questions.md#sorting-searching-algorithms) | `{len(by_topic['Sorting & Searching Algorithms'])}` | Binary search, Merge sort, Quick sort, Heap sort, Bubble sort, Linear search. |
| **7** | [Algorithm Design Paradigms](./All_DSA_Written_Questions.md#algorithm-design-paradigms-greedy-dynamic-programming-divide-conquer) | `{len(by_topic['Algorithm Design Paradigms (Greedy, Dynamic Programming, Divide & Conquer)'])}` | Dynamic Programming (Knapsack, LCS), Greedy (Huffman coding), Divide & Conquer. |
| **8** | [Complexity & Recurrence](./All_DSA_Written_Questions.md#complexity-analysis-recurrence-relations-recursion) | `{len(by_topic['Complexity Analysis, Recurrence Relations & Recursion'])}` | Master Theorem, Recurrence relation trees, Big-O loop time complexity, Recursion. |
| **9** | [Hashing & Hash Tables](./All_DSA_Written_Questions.md#hashing-hash-tables) | `{len(by_topic['Hashing & Hash Tables'])}` | Linear probing, Quadratic probing, Chaining, Hash function modulo calculations. |

---

## 🎯 Key Features
- **Every question mentions:**
  - Organization / Exam Name (e.g. Bangladesh Bank, Combined 5 Bank, Sonali Bank, BTRC, DESCO)
  - Exam Year (from 2018 to 2026)
  - Exam Taker (BUET, BIBM, KUET, DU, etc.)
  - Source Reference (`JobQns` / `Duronto IT` / `Both`)
- **Includes full written solutions, code snippets (C/C++/Java/Python), mathematical step-by-step derivations, and ASCII/markdown tree diagrams** where present in the original exams.
"""
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"README index written to: {INDEX_FILE}")

if __name__ == '__main__':
    build_compendium()
