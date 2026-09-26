import json
import os
from collections import Counter

with open('posts_summary.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

with open('scraped_exams/all_available_exams.json', 'r', encoding='utf-8') as f:
    avail = json.load(f)

avail_ids = set(p['id'] for p in avail)

locked_posts = [p for p in posts if p['id'] not in avail_ids]

print(f"Total posts: {len(posts)}")
print(f"Successfully scraped: {len(avail)}")
print(f"Locked / Not scraped: {len(locked_posts)}")

cat_counts = Counter()
for p in locked_posts:
    cats = p.get('categories', [])
    if isinstance(cats, list):
        for c in cats:
            cat_counts[c] += 1
    else:
        cat_counts[str(cats)] += 1

print("\n--- Locked Posts by Category ---")
for cat, count in cat_counts.most_common():
    print(f"  {cat}: {count}")

print("\n--- All Locked Posts ---")
for i, p in enumerate(locked_posts, 1):
    print(f"{i}. [{p['id']}] {p['title']} ({p.get('date', '')}) - Categories: {p.get('categories')}")
