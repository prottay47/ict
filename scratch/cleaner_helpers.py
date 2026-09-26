import os
import re
import glob
import json
import hashlib

def clean_markdown_text(text):
    # Remove table vertical bars if it's a single column wrapper
    lines = text.splitlines()
    cleaned_lines = []
    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            cleaned_lines.append(line)
            continue
        if in_code:
            cleaned_lines.append(line)
            continue
            
        # Clean table pipes from edges like "| 1 | Question text |" or "| Question text |"
        if stripped.startswith('|') and stripped.endswith('|'):
            # Check if it's a separator line |---|---|
            if re.match(r'^\|[\s\-:]+(\|[\s\-:]+)+\|$', stripped):
                continue
            # Extract content between pipes
            parts = [p.strip() for p in stripped[1:-1].split('|') if p.strip()]
            if parts:
                # If first part is just a number like '1' or '2<br>'
                if len(parts) >= 2 and re.match(r'^\d+(?:<br>)?$', parts[0]):
                    content = " ".join(parts[1:])
                else:
                    content = " ".join(parts)
                cleaned_lines.append(content)
            continue
            
        # Replace <br> with newline
        l_clean = line.replace('<br>', '\n').replace('<br/>', '\n')
        cleaned_lines.append(l_clean)
        
    res = "\n".join(cleaned_lines)
    # clean multiple blank lines
    res = re.sub(r'\n{3,}', '\n\n', res).strip()
    return res

def normalize_question_fingerprint(text):
    # Normalize text to detect duplicates across jobqns and duronto
    t = text.lower()
    # Remove non-alphanumeric
    t = re.sub(r'[^a-z0-9]', '', t)
    # Take first 120 chars
    return t[:100]

print("Text cleaning helpers loaded.")
