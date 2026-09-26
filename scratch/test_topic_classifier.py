import os
import re
import json
import sys

from test_segmentation import extract_questions_jobqns, extract_questions_duronto
from dsa_base import clean_text
import glob

# Detailed category matchers
TOPIC_RULES = [
    (
        "Stacks & Queues (Implementation, Infix/Postfix/Prefix, Parentheses)",
        [
            r'\bstack\b', r'\bqueue\b', r'\bcircular\s*queue\b', r'\bpriority\s*queue\b',
            r'\bdeque\b', r'\bdouble\s*ended\s*queue\b', r'\binfix\b', r'\bpostfix\b',
            r'\bprefix\s*notation\b', r'\blifo\b', r'\bfifo\b', r'\bbalanced\s*parenthes[ei]s\b',
            r'\bpush\s*(?:and|&|\/)\s*pop\b', r'\benqueue\b', r'\bdequeue\b'
        ],
        [r'\bprotocol\s*stack\b', r'\btcp\/ip\b', r'\bmail\s*queue\b', r'\bmessage\s*queue\b']
    ),
    (
        "Linked Lists (Singly, Doubly, Circular, Operations)",
        [
            r'\blinked\s*list\b', r'\bsingly\s*linked\b', r'\bdoubly\s*linked\b',
            r'\bcircular\s*linked\b', r'\bnode\s*->\s*next\b', r'\bnode\s*\*\s*next\b',
            r'\bdetect\s*cycle\b', r'\bhead\s*=\s*head->next\b', r'\breverse\s*a\s*linked\s*list\b'
        ],
        []
    ),
    (
        "Trees, BST, AVL, B-Tree & Heaps",
        [
            r'\bbinary\s*tree\b', r'\bbinary\s*search\s*tree\b', r'\bbst\b',
            r'\bavl\b', r'\bavl\s*tree\b', r'\bb[\s-]*tree\b', r'\bb\+[\s-]*tree\b',
            r'\bheap\b', r'\bmin[\s-]*heap\b', r'\bmax[\s-]*heap\b', r'\bheapify\b',
            r'\bheapsort\b', r'\btraversal\b', r'\binorder\b', r'\bpreorder\b',
            r'\bpre-order\b', r'\bpostorder\b', r'\bpost-order\b', r'\blevel\s*order\b',
            r'\bcomplete\s*binary\s*tree\b', r'\bstrict\s*binary\s*tree\b',
            r'\bheight\s*of\s*(?:a\s*)?tree\b', r'\btrie\b'
        ],
        [r'\bspanning\s*tree\b'] # Spanning tree goes to Graphs
    ),
    (
        "Graphs & Graph Algorithms (BFS, DFS, Dijkstra, Kruskal, Prim, MST)",
        [
            r'\badjacency\s*matrix\b', r'\badjacency\s*list\b', r'\bspanning\s*tree\b',
            r'\bmst\b', r'\bdijkstra\b', r'\bbellman[\s-]*ford\b', r'\bfloyd[\s-]*warshall\b',
            r'\bprim\'?s\b', r'\bkruskal\b', r'\bbreadth[\s-]*first\b', r'\bdepth[\s-]*first\b',
            r'\bbfs\b', r'\bdfs\b', r'\btopological\s*sort\b', r'\bshortest\s*path\b',
            r'\bgraph\s*traversal\b', r'\bconnected\s*component\b', r'\bbipartite\b'
        ],
        []
    ),
    (
        "Sorting & Searching Algorithms",
        [
            r'\bbubble\s*sort\b', r'\bselection\s*sort\b', r'\binsertion\s*sort\b',
            r'\bmerge\s*sort\b', r'\bquick\s*sort\b', r'\bradix\s*sort\b',
            r'\bcounting\s*sort\b', r'\bheap\s*sort\b', r'\bbinary\s*search\b',
            r'\blinear\s*search\b', r'\binterpolation\s*search\b', r'\bsorting\s*algorithm\b'
        ],
        []
    ),
    (
        "Hashing & Hash Tables",
        [
            r'\bhash\s*table\b', r'\bhashing\b', r'\bhash\s*function\b',
            r'\blinear\s*probing\b', r'\bquadratic\s*probing\b', r'\bseparate\s*chaining\b',
            r'\bdouble\s*hashing\b', r'\bcollision\s*resolution\b'
        ],
        []
    ),
    (
        "Algorithm Design Paradigms (Greedy, Dynamic Programming, Divide & Conquer)",
        [
            r'\bgreedy\s*algorithm\b', r'\bgreedy\s*approach\b', r'\bfractional\s*knapsack\b',
            r'\bhuffman\b', r'\bactivity\s*selection\b', r'\bjob\s*sequencing\b',
            r'\bdynamic\s*programming\b', r'\b0\/1\s*knapsack\b', r'\bknapsack\b',
            r'\blongest\s*common\s*subsequence\b', r'\blcs\b', r'\bcoin\s*change\b',
            r'\bmatrix\s*chain\b', r'\bdivide\s*and\s*conquer\b', r'\bbacktracking\b',
            r'\bn-queens\b', r'\bbranch\s*and\s*bound\b'
        ],
        []
    ),
    (
        "Complexity Analysis, Recurrence Relations & Recursion",
        [
            r'\btime\s*complexity\b', r'\bspace\s*complexity\b', r'\basymptotic\b',
            r'\bbig[\s-]*o\b', r'\bmaster\s*theorem\b', r'\brecurrence\s*relation\b',
            r'\btower\s*of\s*hanoi\b', r'\brecursive\s*function\b', r'\brecursion\b',
            r'\border\s*of\s*growth\b'
        ],
        []
    ),
    (
        "Arrays, Matrices & String Manipulation",
        [
            r'\barray\b', r'\b2d\s*array\b', r'\bmatrix\b', r'\bsparse\s*matrix\b',
            r'\bcommon\s*elements\b', r'\bpalindrome\b', r'\bstring\s*reverse\b',
            r'\bsubstring\b', r'\bstring\s*manipulation\b', r'\bpattern\s*matching\b',
            r'\btwo\s*pointer\b', r'\bsliding\s*window\b'
        ],
        [r'\ber\s*diagram\b', r'\bnormal\s*form\b']
    )
]

# Strict non-DSA exclusions to prevent false positives
GLOBAL_EXCLUDES = [
    r'\bprotocol\s*stack\b',
    r'\btcp\/ip\b',
    r'\bosi\s*model\b',
    r'\bdeadlock\b',
    r'\bbanker\'?s\b',
    r'\bcpu\s*scheduling\b',
    r'\bround\s*robin\b',
    r'\bpage\s*replacement\b',
    r'\ber\s*diagram\b',
    r'\bfunctional\s*dependency\b',
    r'\bnormalization\b',
    r'\b2nf\b', r'\b3nf\b', r'\bbcnf\b',
    r'\bcreate\s*table\b',
    r'\btransistor\b', r'\bdiode\b', r'\bop-amp\b',
    r'\bkmap\b', r'\bboolean\s*algebra\b', r'\bflip-flop\b',
    r'\bmicroprocessor\b', r'\b8086\b', r'\b8085\b',
    r'\bip\s*address\b', r'\bsubnet\b',
    r'\bsoftware\s*engineering\b', r'\bsdlc\b', r'\bagile\b',
    r'\btesting\b', r'\bblack\s*box\b', r'\bwhite\s*box\b'
]

def classify_chunk(chunk):
    text = chunk.lower()
    
    # Check if header explicitly mentions Data Structure or Algorithm
    first_few_lines = "\n".join(chunk.splitlines()[:4]).lower()
    has_explicit_dsa_header = bool(re.search(r'\b(data\s*structure|algorithm|dsa|design\s*and\s*analysis\s*of\s*algorithm)\b', first_few_lines))
    
    # If it's pure non-DSA and doesn't have an explicit DSA header, check exclusions
    if not has_explicit_dsa_header:
        # Check global excludes
        ex_hits = [e for e in GLOBAL_EXCLUDES if re.search(e, text)]
        # If strong negative hits and no specific strong DSA keyword, skip
        strong_dsa_keywords = [
            'heap', 'bst', 'binary search tree', 'linked list', 'avl', 'b-tree',
            'inorder', 'preorder', 'postorder', 'dijkstra', 'kruskal', 'prim',
            'bubble sort', 'quick sort', 'merge sort', 'binary search', 'master theorem',
            '0/1 knapsack', 'huffman', 'circular queue', 'topological sort', 'linear probing'
        ]
        has_strong_dsa = any(k in text for k in strong_dsa_keywords)
        if len(ex_hits) >= 2 and not has_strong_dsa:
            return None
        if len(ex_hits) >= 1 and not has_strong_dsa and not ('data structure' in text or 'algorithm' in text):
            return None

    # Try matching topics in priority order
    for topic_name, patterns, neg_patterns in TOPIC_RULES:
        if any(re.search(np, text) for np in neg_patterns) and not has_explicit_dsa_header:
            continue
        if any(re.search(p, text) for p in patterns):
            # Check if this topic match is valid
            # For "Arrays, Matrices & String Manipulation", ensure it's a programming/DSA question
            if topic_name == "Arrays, Matrices & String Manipulation":
                # Must have coding / algorithm or data structure context
                if not (re.search(r'\b(program|function|code|algorithm|c\+\+|java|python|c\b|write\s*a|time\s*complexity|element|sorted)\b', text) or has_explicit_dsa_header):
                    continue
            return topic_name

    return None

if __name__ == '__main__':
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)
    
    all_job = []
    for f in jobqns_files:
        all_job.extend(extract_questions_jobqns(f))
    all_dur = []
    for f in duronto_files:
        all_dur.extend(extract_questions_duronto(f))
        
    print(f'Total segmented: JobQns={len(all_job)}, Duronto={len(all_dur)}')
    
    matched_job = []
    for q in all_job:
        t = classify_chunk(q['chunk'])
        if t:
            q['topic'] = t
            matched_job.append(q)
            
    matched_dur = []
    for q in all_dur:
        t = classify_chunk(q['chunk'])
        if t:
            q['topic'] = t
            matched_dur.append(q)
            
    print(f'Matched DSA: JobQns={len(matched_job)}, Duronto={len(matched_dur)}')
    
    from collections import Counter
    print('\nJobQns DSA by Topic:')
    for k, v in Counter([q['topic'] for q in matched_job]).items():
        print(f'  {k}: {v}')
        
    print('\nDuronto DSA by Topic:')
    for k, v in Counter([q['topic'] for q in matched_dur]).items():
        print(f'  {k}: {v}')
