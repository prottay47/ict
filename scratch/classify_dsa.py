import os
import re
import glob
import json

from test_parser import parse_jobqns_file, parse_duronto_file

# Define strong positive DSA indicators
DSA_STRONG_PATTERNS = [
    r'\bdata\s*structure\b',
    r'\balgorithm\b',
    r'\bmin[\s-]*heap\b',
    r'\bmax[\s-]*heap\b',
    r'\bheapify\b',
    r'\bheapsort\b',
    r'\bheap\s*sort\b',
    r'\bbinary\s*search\s*tree\b',
    r'\bbst\b',
    r'\bavl\s*tree\b',
    r'\bb[\s-]*tree\b',
    r'\bb\+[\s-]*tree\b',
    r'\bbinary\s*tree\b',
    r'\bcomplete\s*binary\s*tree\b',
    r'\btree\s*traversal\b',
    r'\binorder\b',
    r'\bpreorder\b',
    r'\bpre-order\b',
    r'\bpostorder\b',
    r'\bpost-order\b',
    r'\blinked\s*list\b',
    r'\bsingly\s*linked\b',
    r'\bdoubly\s*linked\b',
    r'\bcircular\s*linked\b',
    r'\bnode\s*->\s*next\b',
    r'\bstack\b',
    r'\bpush\s*(?:and|&|\/)\s*pop\b',
    r'\binfix\b',
    r'\bpostfix\b',
    r'\bprefix\s*notation\b',
    r'\bcircular\s*queue\b',
    r'\bpriority\s*queue\b',
    r'\bdeque\b',
    r'\bbubble\s*sort\b',
    r'\bselection\s*sort\b',
    r'\binsertion\s*sort\b',
    r'\bmerge\s*sort\b',
    r'\bquick\s*sort\b',
    r'\bradix\s*sort\b',
    r'\bcounting\s*sort\b',
    r'\bbinary\s*search\b',
    r'\blinear\s*search\b',
    r'\bdijkstra\b',
    r'\bkruskal\b',
    r'\bprim\'?s\b',
    r'\bbreadth[\s-]*first\b',
    r'\bdepth[\s-]*first\b',
    r'\bminimum\s*spanning\s*tree\b',
    r'\bmst\b',
    r'\btopological\s*sort\b',
    r'\badjacency\s*matrix\b',
    r'\badjacency\s*list\b',
    r'\bhash\s*table\b',
    r'\bhash\s*function\b',
    r'\blinear\s*probing\b',
    r'\bquadratic\s*probing\b',
    r'\bseparate\s*chaining\b',
    r'\btime\s*complexity\b',
    r'\bspace\s*complexity\b',
    r'\bbig[\s-]*o\b',
    r'\basymptotic\b',
    r'\bmaster\s*theorem\b',
    r'\brecurrence\s*relation\b',
    r'\btower\s*of\s*hanoi\b',
    r'\bdynamic\s*programming\b',
    r'\b0\/1\s*knapsack\b',
    r'\bfractional\s*knapsack\b',
    r'\bhuffman\s*cod(?:ing|e)\b',
    r'\blongest\s*common\s*subsequence\b',
    r'\blcs\b',
    r'\bdivide\s*and\s*conquer\b',
    r'\bgreedy\s*algorithm\b'
]

# Weaker or contextual indicators (e.g. array, recursion, graph)
DSA_CONTEXT_PATTERNS = [
    r'\barray\b',
    r'\brecursion\b',
    r'\brecursive\b',
    r'\bgraph\b',
    r'\bqueue\b',
    r'\btree\b'
]

# Negative patterns (unrelated topics that might mention words like queue or graph or stack or tree)
NEGATIVE_PATTERNS = [
    r'\bcall\s*stack\b',
    r'\bprotocol\s*stack\b',
    r'\btcp\/ip\s*stack\b',
    r'\bmessage\s*queue\b',
    r'\bmail\s*queue\b',
    r'\ber\s*diagram\b',
    r'\buse\s*case\b',
    r'\bclass\s*diagram\b',
    r'\bsequence\s*diagram\b',
    r'\bactivity\s*diagram\b',
    r'\bnormal\s*form\b',
    r'\bnormalization\b',
    r'\bfunctional\s*dependency\b',
    r'\bacid\b',
    r'\bdeadlock\b',
    r'\bbanker\'?s\b',
    r'\bcpu\s*scheduling\b',
    r'\bround\s*robin\b',
    r'\bpage\s*replacement\b',
    r'\bvirtual\s*memory\b',
    r'\bip\s*address\b',
    r'\bsubnet\b',
    r'\bosi\s*model\b',
    r'\btransistor\b',
    r'\bdiode\b',
    r'\bop-amp\b',
    r'\bkmap\b',
    r'\bboolean\s*algebra\b',
    r'\bflip-flop\b',
    r'\bcache\s*memory\b',
    r'\bpipeline\b',
    r'\bmicroprocessor\b',
    r'\b8086\b',
    r'\b8085\b'
]

def is_dsa_question(raw_text):
    text = raw_text.lower()
    
    # Check explicit DSA header
    if re.search(r'\b(data\s*structure|algorithm|dsa|design\s*and\s*analysis\s*of\s*algorithm)\b', text[:120]):
        # Even if some negative pattern is present, if header is explicitly DSA, it's DSA!
        return True, "Explicit DSA Header"
        
    strong_hits = [p for p in DSA_STRONG_PATTERNS if re.search(p, text)]
    if strong_hits:
        # Check if it's predominantly a negative topic (e.g. Pure OS or Pure DBMS)
        # unless there are multiple strong hits or strong DSA terms like heap, bst, linked list, dijkstra
        pure_dsa_terms = [
            'heap', 'bst', 'binary search tree', 'linked list', 'avl', 'b-tree', 'b+ tree',
            'inorder', 'preorder', 'postorder', 'dijkstra', 'kruskal', 'prim', 'bubble sort',
            'quick sort', 'merge sort', 'binary search', 'master theorem', 'knapsack', 'huffman',
            'infix', 'postfix', 'circular queue', 'topological sort'
        ]
        if any(term in text for term in pure_dsa_terms):
            return True, f"Strong match: {strong_hits[:2]}"
            
        neg_hits = [p for p in NEGATIVE_PATTERNS if re.search(p, text)]
        if len(neg_hits) >= 2 and len(strong_hits) == 1:
            return False, "Negative override"
        return True, f"Strong match: {strong_hits[:2]}"
        
    # Check contextual patterns (e.g. array coding problem, recursion code)
    if re.search(r'\b(write\s*a\s*(?:c|c\+\+|java|python|program|function|code|algorithm))\b', text):
        if any(re.search(p, text) for p in DSA_CONTEXT_PATTERNS):
            if not any(re.search(p, text) for p in NEGATIVE_PATTERNS[:10]):
                return True, "Coding problem on Array/Tree/Recursion"
                
    return False, "Not DSA"

if __name__ == '__main__':
    jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
    duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)
    
    all_q = []
    for f in jobqns_files:
        all_q.extend(parse_jobqns_file(f))
    for f in duronto_files:
        all_q.extend(parse_duronto_file(f))
        
    dsa_list = []
    for q in all_q:
        matched, reason = is_dsa_question(q['raw_content'])
        if matched:
            q['dsa_reason'] = reason
            dsa_list.append(q)
            
    print(f'Total parsed questions: {len(all_q)}')
    print(f'Total DSA questions found: {len(dsa_list)}')
    
    # Save a summary for inspection
    with open('scratch/dsa_preview.json', 'w', encoding='utf-8') as f:
        json.dump(dsa_list[:30], f, indent=2, ensure_ascii=False)
