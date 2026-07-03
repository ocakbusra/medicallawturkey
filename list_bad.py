import glob
from bs4 import BeautifulSoup
import json
from collections import defaultdict

html_files = glob.glob('*.html')
desc_to_files = defaultdict(list)
file_to_desc = {}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        desc = meta_desc['content'].strip() if meta_desc and 'content' in meta_desc.attrs else ""
        desc_to_files[desc].append(file)
        file_to_desc[file] = desc

bad_files = []
for file, desc in file_to_desc.items():
    is_dup = len(desc_to_files[desc]) > 1
    is_short = len(desc) < 140
    if is_dup or is_short:
        bad_files.append({
            'file': file,
            'desc': desc,
            'len': len(desc),
            'dup': is_dup
        })

print(json.dumps(bad_files, indent=2))
