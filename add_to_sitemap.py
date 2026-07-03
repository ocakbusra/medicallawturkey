import os
import glob
from datetime import datetime
import xml.etree.ElementTree as ET

sitemap_path = '/Users/busraocak/Desktop/Medicallaw Turkeyy/sitemap.xml'

# Read sitemap to find existing URLs
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# All HTML files in root
all_html_files = glob.glob('/Users/busraocak/Desktop/Medicallaw Turkeyy/*.html')
basenames = [os.path.basename(f) for f in all_html_files]

missing_files = []
for f in basenames:
    if f not in sitemap_content:
        missing_files.append(f)

if not missing_files:
    print("No missing files!")
else:
    print(f"Missing {len(missing_files)} files: {missing_files}")
    
    # Generate new XML blocks
    new_xml = "\n  <!-- Automatically Added Files -->\n"
    today = datetime.now().strftime("%Y-%m-%d")
    
    for f in sorted(missing_files):
        # Give main glossary and articles slightly higher priority
        priority = "0.6"
        if f in ['glossary.html', 'articles.html']:
            priority = "0.9"
        
        new_xml += f"""  <url>
    <loc>https://www.medicallawturkey.com/{f}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>
"""

    new_sitemap_content = sitemap_content.replace('</urlset>', new_xml + '</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_sitemap_content)
    print("Sitemap updated.")
