import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text[:50]

tasks_dir = '/home/adrian/.openclaw/workspace/00-cockpit/tasks'

if not os.path.exists(tasks_dir):
    print(f"Directory {tasks_dir} not found.")
    exit(1)

for filename in os.listdir(tasks_dir):
    if not filename.endswith('.md'):
        continue
        
    filepath = os.path.join(tasks_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already formatted with YAML frontmatter
    if content.startswith('---\n'):
        continue
        
    # Manual simple parsing
    lines = content.split('\n')
    title = ""
    project = "General"
    status = "todo"
    description = ""
    
    in_details = False
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            continue
        if line.startswith('Project: '):
            project = line[9:].strip()
            continue
        if line.startswith('Status: '):
            status = line[8:].strip().lower()
            if 'open' in status: status = 'todo'
            continue
        if line.startswith('---'):
            in_details = True
            continue
        if in_details:
            description += line + "\n"
    
    if not title:
        title = filename.replace('.md', '').replace('-', ' ')

    new_content = f"""---
title: {title}
project: {project}
status: {status}
priority: medium
created: 2026-02-22
updated: 2026-02-22
---

{description.strip()}"""
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Fixed content for: {filename}")
