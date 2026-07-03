import os
import glob
from bs4 import BeautifulSoup
from collections import defaultdict
import json

html_files = glob.glob('*.html')
descriptions = defaultdict(list)
results = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        desc = meta_desc['content'].strip() if meta_desc and 'content' in meta_desc.attrs else ""
        descriptions[desc].append(file)
        
for desc, files in descriptions.items():
    if len(files) > 1 or len(desc) < 50:
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                title = soup.title.string.strip() if soup.title else ""
                h1 = soup.h1.string.strip() if soup.h1 else ""
                results.append({
                    'file': file,
                    'current_desc': desc,
                    'title': title,
                    'h1': h1,
                    'issue': 'duplicate' if len(files) > 1 else 'short/empty'
                })

print(json.dumps(results, indent=2))
