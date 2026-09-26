import sys
import os
import re

sys.path.insert(0, os.path.dirname(__file__))
from test_segmentation import extract_questions_jobqns, extract_questions_duronto
from test_topic_classifier import classify_chunk
import glob

sys.stdout.reconfigure(encoding='utf-8')

jobqns_files = [f for f in glob.glob('scraped_exams/**/*.md', recursive=True) if 'ALL_WRITTEN' not in f]
duronto_files = glob.glob('duronto_it_organized/**/*.md', recursive=True)

all_job = []
for f in jobqns_files:
    all_job.extend(extract_questions_jobqns(f))
all_dur = []
for f in duronto_files:
    all_dur.extend(extract_questions_duronto(f))

matched_job = [q for q in all_job if classify_chunk(q['chunk'])]
for q in matched_job:
    q['topic'] = classify_chunk(q['chunk'])

matched_dur = [q for q in all_dur if classify_chunk(q['chunk'])]
for q in matched_dur:
    q['topic'] = classify_chunk(q['chunk'])

print('=== 10 Random JobQns Samples ===')
for q in matched_job[10:20]:
    print(f"[{q['topic']}] {q['exam_title']} ({q['year']})")
    print(q['chunk'][:140].replace('\n', ' '))
    print('-'*50)

print('\n=== 10 Random Duronto Samples ===')
for q in matched_dur[10:20]:
    print(f"[{q['topic']}] {q['exam_title']} ({q['year']})")
    print(q['chunk'][:140].replace('\n', ' '))
    print('-'*50)
