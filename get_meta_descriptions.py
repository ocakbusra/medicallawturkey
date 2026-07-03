import os
import glob
from bs4 import BeautifulSoup
import json

html_files = glob.glob('*.html')
results = []
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        desc = meta_desc['content'] if meta_desc and 'content' in meta_desc.attrs else None
        results.append({'file': file, 'description': desc})

print(json.dumps(results, indent=2))
