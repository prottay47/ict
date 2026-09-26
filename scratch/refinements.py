import re

def is_cybersecurity_hashing(text):
    t = text.lower()
    if 'social engineering' in t or 'vulnerability' in t or 'encryption' in t or 'symmetric' in t or 'asymmetric' in t:
        if not ('hash table' in t or 'linear probing' in t or 'chaining' in t or 'collision' in t or 'mod' in t):
            return True
    return False

def is_network_routing(text):
    t = text.lower()
    if 'ospf' in t or 'open shortest path first' in t or 'rip protocol' in t or 'bgp' in t or 'link-state routing' in t:
        if not ('dijkstra' in t and ('graph' in t or 'adjacency' in t or 'vertices' in t)):
            return True
    return False

print("Refinement rules defined.")
