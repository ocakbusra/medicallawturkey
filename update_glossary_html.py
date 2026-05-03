import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\-]+', '-', text)
    return text.strip('-')

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the grid class
content = content.replace('<div class="glossary-grid">', '<div class="cs-grid">')

# We need to replace each <div class="glossary-item"> ... </div>
# using regex or just text replacement if it's predictable
pattern = re.compile(
    r'<div class="glossary-item">\s*<h3 class="glossary-term">(.*?)</h3>\s*<p class="glossary-tr">(.*?)</p>\s*<p class="glossary-def">(.*?)</p>\s*</div>',
    re.DOTALL
)

def replace_item(match):
    term = match.group(1).strip()
    tr_term = match.group(2).strip()
    desc = match.group(3).strip()
    slug = slugify(term)
    
    return f'''<a href="glossary-{slug}.html" class="cs-card" style="text-decoration: none;">
          <span class="cs-tag">Glossary Term</span>
          <h3>{term}</h3>
          <p style="font-weight: 600; font-size: 0.9rem; color: #0891B2; margin-bottom: 0.5rem;">{tr_term}</p>
          <p>{desc}</p>
          <span class="cs-read">Read detailed guide →</span>
        </a>'''

new_content = pattern.sub(replace_item, content)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("glossary.html updated successfully.")
