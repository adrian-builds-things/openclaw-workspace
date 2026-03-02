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
    
    # Simple manual extraction if it's already got frontmatter
    if content.startswith('---\n'):
        # Just escape colons in the title line if they exist
        new_lines = []
        for line in content.split('\n'):
            if line.startswith('title: '):
                t = line[7:].strip()
                # Wrap in quotes to avoid YAML colon issues
                if ':' in t and not (t.startswith('"') or t.startswith("'")):
                    line = f'title: "{t}"'
            new_lines.append(line)
        content = '\n'.join(new_lines)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Sanitized titles for: {filename}")
