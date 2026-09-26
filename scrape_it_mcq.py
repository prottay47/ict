import io
import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8'
}

# 1. Output directory
output_dir = os.path.join(os.getcwd(), 'mcq')
os.makedirs(output_dir, exist_ok=True)

# 2. Fetch list of links from index page
index_url = 'https://it.jobqns.com/wp-json/wp/v2/pages?slug=it-mcq-job-solution'
print(f"Fetching MCQ list from: {index_url}...", flush=True)

req = urllib.request.Request(index_url, headers=headers)
with urllib.request.urlopen(req, context=ctx) as r:
    page_data = json.loads(r.read().decode('utf-8'))

soup = BeautifulSoup(page_data[0]['content']['rendered'], 'html.parser')

mcq_list = []
seen_urls = set()

for a in soup.find_all('a', href=True):
    h = a['href'].strip()
    t = a.get_text().strip()
    if h.startswith('https://it.jobqns.com/') and h != 'https://it.jobqns.com/':
        if h not in seen_urls:
            seen_urls.add(h)
            mcq_list.append({'url': h, 'title': t})

print(f"Total MCQ exams found: {len(mcq_list)}\n", flush=True)

results_summary = []

for idx, item in enumerate(mcq_list, 1):
    u = item['url']
    raw_title = item['title']
    slug = u.strip('/').split('/')[-1]
    
    print(f"[{idx}/{len(mcq_list)}] Processing: {raw_title} ({slug})...", flush=True)
    
    try:
        page_req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(page_req, context=ctx) as resp:
            page_html = resp.read().decode('utf-8', errors='ignore')
            
        page_soup = BeautifulSoup(page_html, 'html.parser')
        
        # Check title from H1 or meta
        h1 = page_soup.find('h1')
        title = h1.get_text().strip() if h1 else raw_title
        
        # Check if QSM form exists
        form = page_soup.find('form', class_='qsm-quiz-form')
        
        questions_extracted = []
        is_locked = 'You must subscribe & Login to view more' in page_html
        
        if form:
            quiz_id = form.find('input', {'name': 'qmn_quiz_id'}).get('value')
            nonce_elem = page_soup.find('input', id=f'qsm_nonce_{quiz_id}') or form.find('input', {'name': 'qsm_nonce'})
            nonce = nonce_elem.get('value') if nonce_elem else ''
            
            # Prepare submission data to get answers
            form_data = {}
            for inp in form.find_all('input'):
                n = inp.get('name')
                v = inp.get('value', '')
                if n:
                    form_data[n] = v
                    
            form_data['action'] = 'qmn_process_quiz'
            form_data['nonce'] = nonce
            form_data['currentuserTime'] = str(int(time.time()))
            form_data['currentuserTimeZone'] = 'Asia/Dhaka'
            
            # Submit to admin-ajax.php
            post_headers = headers.copy()
            post_headers['Referer'] = u
            encoded = urllib.parse.urlencode(form_data).encode('utf-8')
            ajax_req = urllib.request.Request('https://it.jobqns.com/wp-admin/admin-ajax.php', data=encoded, headers=post_headers)
            
            with urllib.request.urlopen(ajax_req, context=ctx) as ajax_resp:
                res_json = json.loads(ajax_resp.read().decode('utf-8', errors='ignore'))
                
            display_html = res_json.get('display', '')
            res_soup = BeautifulSoup(display_html, 'html.parser')
            
            q_divs = res_soup.find_all('div', class_='qmn_question_answer')
            for q_idx, q in enumerate(q_divs, 1):
                # Question title
                q_title_elem = q.find('span', class_='qsm-result-question-title') or q.find('div', class_='mlw_qmn_question')
                q_text = ''
                if q_title_elem:
                    q_text = q_title_elem.get_text().strip()
                    # Clean leading number if repeated
                    q_text = re.sub(r'^\d+\.?\s*', '', q_text).strip()
                
                # Correct option
                correct_elem = q.find(attrs={'answerstatus': 'correct'}) or q.find('span', class_='qsm-text-correct-option')
                correct_text = correct_elem.get_text().strip() if correct_elem else 'Not specified'
                
                # All options
                options = []
                for opt in q.find_all('span', class_=['qsm-text-correct-option', 'qsm-text-simple-option']):
                    opt_t = opt.get_text().strip()
                    if opt_t and opt_t not in options:
                        options.append(opt_t)
                        
                questions_extracted.append({
                    'number': q_idx,
                    'question': q_text,
                    'options': options,
                    'correct': correct_text
                })
                
            status_desc = f"Extracted {len(questions_extracted)} MCQs with answers (QSM)"
        elif is_locked:
            status_desc = "Locked under subscription paywall"
        else:
            # Fallback for standard post content
            entry = page_soup.find('div', class_='entry-content') or page_soup.find('div', class_='elementor')
            text_content = entry.get_text().strip() if entry else ''
            status_desc = f"Static page / elementor ({len(text_content)} chars)"

        # Generate Markdown File
        safe_name = re.sub(r'[\\/*?:"<>|]', '_', slug)
        file_path = os.path.join(output_dir, f"{idx:02d}_{safe_name}.md")
        
        md_lines = []
        md_lines.append(f"# {title}\n")
        md_lines.append("| Field | Details |")
        md_lines.append("| :--- | :--- |")
        md_lines.append(f"| **Original URL** | [{u}]({u}) |")
        md_lines.append(f"| **Status** | {status_desc} |")
        md_lines.append(f"| **Total MCQs** | {len(questions_extracted)} |")
        md_lines.append(f"| **Source** | it.jobqns.com / IT MCQ Job Solution |\n")
        md_lines.append("---\n")
        
        if questions_extracted:
            for q in questions_extracted:
                md_lines.append(f"### {q['number']}. {q['question']}\n")
                opt_letters = ['A', 'B', 'C', 'D', 'E', 'F']
                for o_idx, opt in enumerate(q['options']):
                    letter = opt_letters[o_idx] if o_idx < len(opt_letters) else '-'
                    is_ans = (opt.strip().lower() == q['correct'].strip().lower())
                    marker = "[x]" if is_ans else "[ ]"
                    md_lines.append(f"- {marker} **{letter})** {opt}")
                md_lines.append(f"\n**Correct Answer:** ✅ **{q['correct']}**\n")
                md_lines.append("---\n")
        elif is_locked:
            md_lines.append("> [!WARNING]\n> **Subscription Required:** The questions for this exam on `it.jobqns.com` are locked under a subscriber login paywall.\n")
        else:
            md_lines.append("### Content:\n")
            md_lines.append(text_content[:2000] if 'text_content' in locals() else "No content available.")
            
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(md_lines))
            
        results_summary.append({
            'index': idx,
            'title': title,
            'url': u,
            'filename': f"{idx:02d}_{safe_name}.md",
            'count': len(questions_extracted),
            'status': status_desc
        })
        
        print(f"  -> {status_desc}, saved to {file_path}", flush=True)
        time.sleep(0.5) # gentle delay
        
    except Exception as e:
        print(f"  -> Error: {e}", flush=True)
        results_summary.append({
            'index': idx,
            'title': raw_title,
            'url': u,
            'filename': f"{idx:02d}_{slug}.md",
            'count': 0,
            'status': f"Error: {e}"
        })

# 3. Create Master README / Index
readme_path = os.path.join(output_dir, 'README.md')
with open(readme_path, 'w', encoding='utf-8') as f_rd:
    f_rd.write("# IT MCQ Job Solutions Archive\n\n")
    f_rd.write("> Scraped directly from `https://it.jobqns.com/it-mcq-job-solution/`\n")
    f_rd.write(f"> Total MCQ Exams: {len(results_summary)}\n")
    total_mcqs = sum(r['count'] for r in results_summary)
    f_rd.write(f"> Total MCQs Extracted with Answers: **{total_mcqs} Questions**\n\n")
    f_rd.write("---\n\n")
    f_rd.write("## Table of Contents\n\n")
    f_rd.write("| # | Exam Title | Total Questions | Status | Link |\n")
    f_rd.write("| :-: | :--- | :-: | :--- | :--- |\n")
    for r in results_summary:
        f_rd.write(f"| {r['index']} | **{r['title']}** | {r['count']} | `{r['status']}` | [{r['filename']}](./{r['filename']}) |\n")

print(f"\nScraping complete! Total MCQs scraped: {total_mcqs}. Index saved to: {readme_path}", flush=True)
