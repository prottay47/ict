import json

with open('locked_exams_by_category.json', 'r', encoding='utf-8') as f:
    cats = json.load(f)

for cat in ['Bank IT Job Solutions', 'BPSC IT Job Solutions', 'Power Sector IT Job Solutions']:
    print(f"\n=== {cat} ({len(cats[cat])}) ===")
    for item in cats[cat]:
        print(f"- [{item['id']}] {item['clean_title']}")
