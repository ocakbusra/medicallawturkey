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
        desc = meta_desc['content'].strip() if meta_desc and 'content' in meta_desc.attrs else ""
        results.append({'file': file, 'length': len(desc), 'desc': desc})

# Let's count duplicates
desc_counts = {}
for r in results:
    desc_counts[r['desc']] = desc_counts.get(r['desc'], 0) + 1

for r in results:
    r['duplicates'] = desc_counts[r['desc']]

# Print ones that are either duplicate or out of the 140-160 range, or just print everything sorted by length
needs_work = [r for r in results if r['length'] < 140 or r['length'] > 160 or r['duplicates'] > 1]
print(json.dumps(needs_work, indent=2))
