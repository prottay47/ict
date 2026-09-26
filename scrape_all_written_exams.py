import os
import sys
import io
import re
import json
import ssl
import urllib.request
from html import unescape
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def clean_elementor_html(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove unwanted tags
    for tag in soup(['script', 'style', 'noscript', 'iframe', 'svg', 'button']):
        tag.decompose()
        
    # Process pre and code blocks
    for pre in soup.find_all(['pre', 'code']):
        code_text = pre.get_text()
        pre.replace_with(f"\n```\n{code_text.strip()}\n```\n")
        
    # Convert headings
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = min(int(h.name[1]), 4)
        h_text = h.get_text().strip()
        if h_text:
            h.replace_with(f"\n\n{'#' * level} {h_text}\n\n")
            
    # Convert bold / strong
    for b in soup.find_all(['strong', 'b']):
        b_text = b.get_text().strip()
        if b_text:
            b.replace_with(f" **{b_text}** ")
            
    # Convert list items
    for li in soup.find_all('li'):
        li_text = li.get_text().strip()
        if li_text:
            li.replace_with(f"\n- {li_text}")
            
    # Convert paragraphs
    for p in soup.find_all('p'):
        p_text = p.get_text().strip()
        if p_text:
            p.replace_with(f"\n\n{p_text}\n\n")

    for br in soup.find_all('br'):
        br.replace_with("\n")
        
    text = soup.get_text()
    text = re.sub(r'\n{3,}', '\n\n', text)
    lines = [line.strip() for line in text.split('\n')]
    clean_text = '\n'.join(lines).strip()
    return unescape(clean_text)

def categorize_post(p, cat_names):
    title = p['title']['rendered'].lower()
    cats = [c.lower() for c in cat_names]
    
    if any('bank' in c for c in cats) or 'bank' in title:
        return 'Bank_IT'
    elif any('bpsc' in c for c in cats) or 'bpsc' in title or 'bcs' in title:
        return 'BPSC_IT'
    elif any('power sector' in c for c in cats) or any(x in title for x in ['desco', 'dpdc', 'pgcb', 'breb', 'egcb', 'npcbl']):
        return 'Power_Sector'
    elif any('gas field' in c for c in cats) or any(x in title for x in ['gtcl', 'bapex', 'bgdcl', 'bogmc', 'jgtdsl', 'jamuna oil']):
        return 'Gas_and_Energy'
    elif any(x in title for x in ['ministry', 'caab', 'buet', 'wasa', 'spcbl', 'idra', 'bitac', 'biwta', 'bepza', 'nsda', 'ntmc']):
        return 'Ministries_and_Govt_Bodies'
    elif 'module' in title or any('module' in c for c in cats):
        return 'Exam_and_Study_Modules'
    elif 'focus writing' in title or any('focus writing' in c for c in cats):
        return 'Focus_Writing'
    else:
        return 'Other_IT_Solutions'

def main():
    print("Starting full scrape of it.jobqns.com...")
    
    # 1. Fetch categories
    print("Fetching categories...")
    req_cat = urllib.request.Request('https://it.jobqns.com/wp-json/wp/v2/categories?per_page=100', headers=HEADERS)
    with urllib.request.urlopen(req_cat, context=ctx) as resp:
        cats = json.loads(resp.read().decode('utf-8'))
    cat_map = {c['id']: c['name'] for c in cats}
    
    # 2. Fetch all posts
    all_posts = []
    page = 1
    while True:
        url = f'https://it.jobqns.com/wp-json/wp/v2/posts?per_page=100&page={page}'
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, context=ctx) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if not data:
                    break
                all_posts.extend(data)
                print(f"  Page {page}: {len(data)} posts fetched.")
                page += 1
        except Exception:
            break
            
    print(f"Total posts fetched from site: {len(all_posts)}")
    
    # Output directories
    output_base = os.path.join(os.getcwd(), 'scraped_exams')
    os.makedirs(output_base, exist_ok=True)
    
    lock_keywords = [
        'You must subscribe',
        'Login to view more',
        'Subscription Required',
        'active Exam Module Subscription'
    ]
    
    scraped_records = []
    locked_records = []
    
    for p in all_posts:
        pid = p['id']
        title_raw = p['title']['rendered']
        title = unescape(title_raw).strip()
        link = p['link']
        date = p['date']
        cat_names = [cat_map.get(cid, str(cid)) for cid in p['categories']]
        raw_html = p['content']['rendered']
        
        is_locked = any(kw in raw_html for kw in lock_keywords)
        clean_text = clean_elementor_html(raw_html)
        category_dir_name = categorize_post(p, cat_names)
        
        record = {
            'id': pid,
            'title': title,
            'link': link,
            'date': date,
            'categories': cat_names,
            'assigned_category': category_dir_name,
            'is_locked': is_locked,
            'content_length': len(clean_text),
            'content_markdown': clean_text
        }
        
        if is_locked or len(clean_text) < 100:
            locked_records.append(record)
        else:
            scraped_records.append(record)
            
            # Save individual markdown file
            cat_dir = os.path.join(output_base, category_dir_name)
            os.makedirs(cat_dir, exist_ok=True)
            
            # Clean filename
            safe_title = re.sub(r'[\/\\:\*\?"<>\|]', '_', title)[:100].strip()
            filename = f"{pid}_{safe_title}.md"
            filepath = os.path.join(cat_dir, filename)
            
            md_content = f"# {title}\n\n"
            md_content += f"- **Original URL:** [{link}]({link})\n"
            md_content += f"- **Date:** {date}\n"
            md_content += f"- **Categories:** {', '.join(cat_names)}\n\n"
            md_content += "---\n\n"
            md_content += clean_text + "\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)
                
    print(f"\nScraping complete:")
    print(f"  Successfully extracted & formatted: {len(scraped_records)} exams / articles")
    print(f"  Subscriber locked: {len(locked_records)} items")
    
    # Save master JSON
    json_path = os.path.join(output_base, 'all_available_exams.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(scraped_records, f, ensure_ascii=False, indent=2)
    print(f"  Saved master JSON: {json_path}")
    
    # Create master combined markdown
    combined_md_path = os.path.join(output_base, 'ALL_WRITTEN_EXAMS_MASTER.md')
    with open(combined_md_path, 'w', encoding='utf-8') as f:
        f.write("# IT Job QnS - Complete Scraped Written Exam Questions & Solutions\n\n")
        f.write(f"> Scraped from: https://it.jobqns.com/\n")
        f.write(f"> Total Available Open Exams/Sets: {len(scraped_records)}\n\n")
        f.write("## Table of Contents\n\n")
        for rec in scraped_records:
            f.write(f"- [{rec['title']}](#post-{rec['id']}) ({rec['assigned_category']})\n")
        f.write("\n---\n\n")
        for rec in scraped_records:
            f.write(f"<a name=\"post-{rec['id']}\"></a>\n\n")
            f.write(f"# {rec['title']}\n\n")
            f.write(f"- **Source:** {rec['link']}\n")
            f.write(f"- **Category:** {', '.join(rec['categories'])}\n\n")
            f.write(rec['content_markdown'])
            f.write("\n\n---\n\n")
    print(f"  Saved combined master markdown: {combined_md_path}")
    
    # Print summary by category
    print("\nBreakdown of extracted exams:")
    cat_summary = {}
    for r in scraped_records:
        cat_summary[r['assigned_category']] = cat_summary.get(r['assigned_category'], 0) + 1
    for cat, count in sorted(cat_summary.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {cat}: {count} papers")

if __name__ == '__main__':
    main()
