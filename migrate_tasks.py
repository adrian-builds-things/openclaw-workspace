#!/usr/bin/env python3
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text[:50]

source_file = '00-cockpit/tasks-master.md'
target_dir = '00-cockpit/tasks'

if not os.path.exists(source_file):
    print(f"Error: {source_file} not found")
    exit(1)

with open(source_file, 'r') as f:
    lines = f.readlines()

current_project = "General"
for line in lines:
    if line.startswith('## '):
        current_project = line.strip('# \n')
    
    # Match tasks like "- [ ] **Project** — Task name" or "- [ ] Task name"
    match = re.match(r'- \[[ xX]\] (.*)', line)
    if match:
        full_task_text = match.group(1).strip()
        # Clean up formatting like **Bold**
        clean_name = re.sub(r'\*\*|#\w+', '', full_task_text).strip()
        
        filename = slugify(clean_name) + ".md"
        filepath = os.path.join(target_dir, filename)
        
        content = f"# {clean_name}\n\nProject: {current_project}\nStatus: Open\nCreated: 2026-02-22\n\n---\nFull text: {full_task_text}"
        
        with open(filepath, 'w') as tf:
            tf.write(content)
        print(f"Created: {filepath}")
