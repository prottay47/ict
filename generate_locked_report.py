import json
import os
from html import unescape

with open('posts_summary.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

with open('scraped_exams/all_available_exams.json', 'r', encoding='utf-8') as f:
    avail = json.load(f)

avail_ids = set(p['id'] for p in avail)
locked = [p for p in posts if p['id'] not in avail_ids]

categories = {
    'Bank IT Job Solutions': [],
    'BPSC IT Job Solutions': [],
    'Power Sector IT Job Solutions': [],
    'Gas & Energy Sector': [],
    'Ministries & Other Govt Organizations': [],
    'Preparation & Subject Modules (M1, M2...)': [],
    'Focus Writing & Non-Technical': [],
    'Other / Uncategorized': []
}

for p in locked:
    t = unescape(p['title']).strip()
    p['clean_title'] = t
    cats = p.get('categories', [])
    c_str = ' '.join(cats).lower()
    t_lower = t.lower()
    
    if 'bank' in c_str or 'bank' in t_lower:
        categories['Bank IT Job Solutions'].append(p)
    elif 'bpsc' in c_str or 'bcs' in c_str or 'bpsc' in t_lower:
        categories['BPSC IT Job Solutions'].append(p)
    elif 'power sector' in c_str or any(x in t_lower for x in ['breb', 'dpdc', 'desco', 'pgcb', 'egcb', 'mgmcl']):
        categories['Power Sector IT Job Solutions'].append(p)
    elif 'gas field' in c_str or any(x in t_lower for x in ['gtcl', 'bapex', 'bgdcl', 'bogmc', 'jgtdsl', 'rpgcl', 'tgtdcl']):
        categories['Gas & Energy Sector'].append(p)
    elif any(x in c_str for x in ['ministry', 'other it']) or any(x in t_lower for x in ['ministry', 'bcic', 'btcl', 'bricm', 'immigration', 'dmtcl', 'youth', 'milk vita', 'computer council', 'livestcok', 'bdccl']):
        categories['Ministries & Other Govt Organizations'].append(p)
    elif any(x in c_str for x in ['module', 'exam module', 'preparation module']) or 'module' in t_lower or (t.startswith('M') and ':' in t):
        categories['Preparation & Subject Modules (M1, M2...)'].append(p)
    elif 'focus writing' in c_str or 'focus writing' in t_lower or 'non technical' in c_str:
        categories['Focus Writing & Non-Technical'].append(p)
    else:
        categories['Other / Uncategorized'].append(p)

with open('locked_exams_by_category.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, ensure_ascii=False, indent=2)

print("Saved locked_exams_by_category.json successfully!")
for cat_name, items in categories.items():
    print(f"\n### {cat_name} ({len(items)})")
    for item in items:
        print(f"- [{item['id']}] {item['clean_title']} | Link: {item['link']}")
