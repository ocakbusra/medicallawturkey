"""Rebuild sitemap.xml from canonical root-level HTML URLs."""

from pathlib import Path
import subprocess
from datetime import date
from xml.etree import ElementTree as ET

SITE = "https://www.medicallawturkey.com"
ROOT = Path(__file__).parent
SITEMAP = ROOT / "sitemap.xml"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def existing_lastmods() -> dict[str, str]:
    if not SITEMAP.exists():
        return {}
    tree = ET.parse(SITEMAP)
    return {
        node.findtext(f"{{{NS}}}loc", ""): node.findtext(f"{{{NS}}}lastmod", "")
        for node in tree.findall(f"{{{NS}}}url")
    }


def canonical_for(page: Path) -> str:
    return f"{SITE}/" if page.name == "index.html" else f"{SITE}/{page.name}"


def content_lastmod(page: Path) -> str | None:
    """Use the page's latest committed date, with sensible fallbacks."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", page.name],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() or None


def rebuild() -> int:
    prior = existing_lastmods()
    pages = sorted(
        (page for page in ROOT.glob("*.html") if page.name != "thank-you.html"),
        key=lambda path: (path.name != "index.html", path.name),
    )
    ET.register_namespace("", NS)
    root = ET.Element(f"{{{NS}}}urlset")
    for page in pages:
        canonical = canonical_for(page)
        url = ET.SubElement(root, f"{{{NS}}}url")
        ET.SubElement(url, f"{{{NS}}}loc").text = canonical
        lastmod = content_lastmod(page) or prior.get(canonical) or date.today().isoformat()
        ET.SubElement(url, f"{{{NS}}}lastmod").text = lastmod
    ET.indent(root, space="  ")
    SITEMAP.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        + ET.tostring(root, encoding="unicode")
        + "\n",
        encoding="utf-8",
    )
    return len(pages)


if __name__ == "__main__":
    print(f"Sitemap rebuilt with {rebuild()} canonical URLs.")
