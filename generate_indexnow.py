import json
import glob
import os
import urllib.request

# Find all HTML files in the directory
html_files = glob.glob('*.html')
html_files.sort()

# Generate URLs for turkishtradelawyers.com
domain = "www.turkishtradelawyers.com"
urls = []

for file in html_files:
    if file == 'index.html':
        urls.append(f"https://{domain}/")
    else:
        urls.append(f"https://{domain}/{file}")

# Create the JSON payload
payload = {
  "host": domain,
  "key": "4c94c0df80b64ece96587ad181b92a64",
  "keyLocation": f"https://{domain}/4c94c0df80b64ece96587ad181b92a64.txt",
  "urlList": urls
}

# Write payload to file
with open('indexnow_request.json', 'w', encoding='utf-8') as f:
    json.dump(payload, f, indent=4)

print(f"Generated indexnow_request.json with {len(urls)} URLs.")

# Optional: send the request
# req = urllib.request.Request('https://api.indexnow.org/indexnow', data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json; charset=utf-8'})
# try:
#     response = urllib.request.urlopen(req)
#     print("Status code:", response.getcode())
# except Exception as e:
#     print("Error:", e)
