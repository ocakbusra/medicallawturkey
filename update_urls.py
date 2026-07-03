import os
import glob

def replace_urls(directory):
    extensions = ['*.html', '*.xml', '*.json']
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(directory, '**', ext), recursive=True))

    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content.replace('https://medicallawturkey.com', 'https://www.medicallawturkey.com')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Error reading/writing {filepath}: {e}")

if __name__ == "__main__":
    replace_urls('/Users/busraocak/Desktop/Medicallaw Turkeyy')
