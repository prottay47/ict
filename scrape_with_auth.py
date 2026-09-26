"""
IT Job QnS (https://it.jobqns.com/) - Authenticated Scraper
-----------------------------------------------------------
Use this script if you have a registered/subscribed account on it.jobqns.com
to scrape the subscriber-locked exam modules as well.

Usage:
  python scrape_with_auth.py --cookie "wordpress_logged_in_xxxx=...; other_cookies=..."
"""

import os
import sys
import io
import re
import json
import ssl
import argparse
import urllib.request
from html import unescape
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_elementor_html(html_content):
    if not html_content:
        return ""
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(['script', 'style', 'noscript', 'iframe', 'svg', 'button']):
        tag.decompose()
        
    for pre in soup.find_all(['pre', 'code']):
        code_text = pre.get_text()
        pre.replace_with(f"\n```\n{code_text.strip()}\n```\n")
        
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = min(int(h.name[1]), 4)
        h_text = h.get_text().strip()
        if h_text:
            h.replace_with(f"\n\n{'#' * level} {h_text}\n\n")
            
    for b in soup.find_all(['strong', 'b']):
        b_text = b.get_text().strip()
        if b_text:
            b.replace_with(f" **{b_text}** ")
            
    for li in soup.find_all('li'):
        li_text = li.get_text().strip()
        if li_text:
            li.replace_with(f"\n- {li_text}")
            
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

def main():
    parser = argparse.ArgumentParser(description="Scrape with authentication cookie")
    parser.add_argument("--cookie", help="Browser session cookie header string", default="")
    args = parser.parse_args()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    if args.cookie:
        headers['Cookie'] = args.cookie
        print("Using provided session cookie.")
    else:
        print("No cookie provided. Running in public mode.")

    req_cat = urllib.request.Request('https://it.jobqns.com/wp-json/wp/v2/categories?per_page=100', headers=headers)
    with urllib.request.urlopen(req_cat, context=ctx) as resp:
        cats = json.loads(resp.read().decode('utf-8'))
    cat_map = {c['id']: c['name'] for c in cats}

    all_posts = []
    page = 1
    while True:
        url = f'https://it.jobqns.com/wp-json/wp/v2/posts?per_page=100&page={page}'
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, context=ctx) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if not data:
                    break
                all_posts.extend(data)
                print(f"Page {page}: {len(data)} posts fetched.")
                page += 1
        except Exception:
            break

    print(f"Total posts fetched: {len(all_posts)}")
    output_base = os.path.join(os.getcwd(), 'scraped_exams_all')
    os.makedirs(output_base, exist_ok=True)

    extracted = 0
    for p in all_posts:
        pid = p['id']
        title = unescape(p['title']['rendered']).strip()
        link = p['link']
        date = p['date']
        cat_names = [cat_map.get(cid, str(cid)) for cid in p['categories']]
        raw_html = p['content']['rendered']
        clean_text = clean_elementor_html(raw_html)

        safe_title = re.sub(r'[\/\\:\*\?"<>\|]', '_', title)[:100].strip()
        filename = f"{pid}_{safe_title}.md"
        filepath = os.path.join(output_base, filename)

        md_content = f"# {title}\n\n- **URL:** {link}\n- **Date:** {date}\n- **Categories:** {', '.join(cat_names)}\n\n---\n\n{clean_text}\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        extracted += 1

    print(f"Finished! Saved {extracted} posts into {output_base}")

if __name__ == '__main__':
    main()
