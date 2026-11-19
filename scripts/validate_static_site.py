#!/usr/bin/env python3
"""Validate the static pages before a GitHub Pages deployment."""

from __future__ import annotations

import json
import sys
from collections import deque
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.medicallawturkey.com"
SITEMAP = ROOT / "sitemap.xml"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str | None]]] = []
        self.ids: set[str] = set()
        self.h1_count = 0
        self.json_ld: list[str] = []
        self._inside_json_ld = False
        self._inside_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.tags.append((tag.lower(), values))
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag.lower() == "h1":
            self.h1_count += 1
        if tag.lower() == "title":
            self._inside_title = True
        if tag.lower() == "script" and values.get("type", "").lower() == "application/ld+json":
            self._inside_json_ld = True
            self.json_ld.append("")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._inside_title = False
        if tag.lower() == "script" and self._inside_json_ld:
            self._inside_json_ld = False

    def handle_data(self, data: str) -> None:
        if self._inside_title:
            self.title += data
        if self._inside_json_ld and self.json_ld:
            self.json_ld[-1] += data


def expected_url(page: Path) -> str:
    return f"{SITE}/" if page.name == "index.html" else f"{SITE}/{page.name}"


def local_target(page: Path, raw_url: str) -> tuple[Path, str | None] | None:
    joined = urljoin(f"{SITE}/{page.name}", raw_url)
    parsed = urlsplit(joined)
    site_host = urlsplit(SITE).netloc
    if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() not in {
        site_host,
        "medicallawturkey.com",
    }:
        return None

    path = unquote(parsed.path)
    relative_path = path.lstrip("/")
    if not relative_path:
        relative_path = "index.html"
    elif path.endswith("/"):
        relative_path += "index.html"
    target = ROOT / relative_path
    return target, unquote(parsed.fragment) or None


def validate_profile_page_schema(schema: object) -> list[str]:
    """Check Google's ProfilePage field types in addition to JSON syntax."""
    errors: list[str] = []
    nodes = schema if isinstance(schema, list) else [schema]
    for node in nodes:
        if not isinstance(node, dict):
            continue
        if isinstance(node.get("@graph"), list):
            errors.extend(validate_profile_page_schema(node["@graph"]))
        types = node.get("@type", [])
        if "ProfilePage" not in (types if isinstance(types, list) else [types]):
            continue
        if "mainEntityOfPage" in node:
            errors.append("ProfilePage: mainEntityOfPage is not supported by Google")
        for field in ("dateCreated", "dateModified"):
            if field not in node:
                continue
            value = node[field]
            try:
                if not isinstance(value, str) or "T" not in value:
                    raise ValueError
                if datetime.fromisoformat(value).utcoffset() is None:
                    raise ValueError
            except ValueError:
                errors.append(f"ProfilePage: {field} must include a valid time and timezone")
        entity = node.get("mainEntity")
        if not isinstance(entity, dict):
            errors.append("ProfilePage: mainEntity must describe a person or organization")
        elif "identifier" in entity and not isinstance(entity["identifier"], str):
            errors.append("ProfilePage: mainEntity.identifier must be text for Google")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    pages = sorted(ROOT.glob("*.html"))
    if not pages:
        return ["No root-level HTML pages were found."]

    parsed_pages: dict[Path, PageParser] = {}
    canonical_urls: dict[Path, str] = {}
    noindex_pages: set[Path] = set()
    title_owners: dict[str, Path] = {}

    for page in pages:
        parser = PageParser()
        try:
            source = page.read_text(encoding="utf-8")
            parser.feed(source)
        except (OSError, UnicodeError) as error:
            errors.append(f"{page.name}: could not read HTML: {error}")
            continue
        parsed_pages[page] = parser

        title = " ".join(parser.title.split())
        if sum(tag == "title" for tag, _ in parser.tags) != 1 or not title:
            errors.append(f"{page.name}: expected one non-empty title")
        elif len(title) > 70:
            errors.append(f"{page.name}: title exceeds 70 characters ({len(title)})")
        title_key = title.casefold()
        if title_key and title_key in title_owners:
            errors.append(f"{page.name}: title duplicates {title_owners[title_key].name}")
        elif title_key:
            title_owners[title_key] = page

        google_loaders = [
            attrs.get("src")
            for tag, attrs in parser.tags
            if tag == "script" and "googletagmanager.com/gtag/js" in (attrs.get("src") or "")
        ]
        if len(google_loaders) != 1:
            errors.append(f"{page.name}: expected one Google tag loader, found {len(google_loaders)}")
        if source.count("AW-18437766591')") != 1:
            errors.append(f"{page.name}: expected one Google Ads configuration")

        canonicals = [
            attrs.get("href")
            for tag, attrs in parser.tags
            if tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split()
        ]
        if len(canonicals) != 1:
            errors.append(f"{page.name}: expected one canonical link, found {len(canonicals)}")
        elif canonicals[0] != expected_url(page):
            errors.append(
                f"{page.name}: canonical should be {expected_url(page)}, found {canonicals[0]}"
            )
        else:
            canonical_urls[page] = str(canonicals[0])

        robots = " ".join(
            attrs.get("content", "").lower()
            for tag, attrs in parser.tags
            if tag == "meta" and (attrs.get("name") or "").lower() == "robots"
        )
        if "noindex" in robots:
            noindex_pages.add(page)

        if parser.h1_count != 1:
            errors.append(f"{page.name}: expected one H1, found {parser.h1_count}")

        styles_linked = any(
            tag == "link"
            and (attrs.get("href") or "").split("?", 1)[0] == "styles.css"
            for tag, attrs in parser.tags
        )
        if not styles_linked:
            errors.append(f"{page.name}: missing styles.css link")

        whatsapp = [
            attrs
            for tag, attrs in parser.tags
            if tag == "a" and "floating-whatsapp" in (attrs.get("class") or "").split()
        ]
        if len(whatsapp) != 1:
            errors.append(f"{page.name}: expected one floating WhatsApp link, found {len(whatsapp)}")
        elif (
            whatsapp[0].get("href") != "https://wa.me/905319336316"
            or whatsapp[0].get("id") != "floatingWhatsapp"
        ):
            errors.append(f"{page.name}: floating WhatsApp link has an unexpected URL or id")

        for index, block in enumerate(parser.json_ld, start=1):
            try:
                schema = json.loads(block)
            except json.JSONDecodeError as error:
                errors.append(f"{page.name}: JSON-LD block {index} is invalid: {error.msg}")
                continue
            errors.extend(
                f"{page.name}: {error}" for error in validate_profile_page_schema(schema)
            )

    for page, parser in parsed_pages.items():
        for tag, attrs in parser.tags:
            raw_url = None
            if tag == "a":
                raw_url = attrs.get("href")
            elif tag in {"img", "script", "iframe", "source", "video", "audio"}:
                raw_url = attrs.get("src")
            elif tag == "link":
                raw_url = attrs.get("href")
            if not raw_url:
                continue

            absolute_url = urlsplit(raw_url)
            if (
                tag == "a"
                and absolute_url.hostname in {"medicallawturkey.com", "www.medicallawturkey.com"}
                and (
                    absolute_url.scheme != "https"
                    or absolute_url.hostname != "www.medicallawturkey.com"
                )
            ):
                errors.append(f"{page.name}: internal URL should use canonical HTTPS host: {raw_url}")

            target_info = local_target(page, raw_url)
            if target_info is None:
                continue
            target, fragment = target_info
            if not target.is_file():
                errors.append(f"{page.name}: local {tag} URL does not exist: {raw_url}")
                continue
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                target_page = target.resolve()
                target_parser = parsed_pages.get(target_page)
                if target_parser is None:
                    target_parser = PageParser()
                    try:
                        target_parser.feed(target.read_text(encoding="utf-8"))
                    except (OSError, UnicodeError):
                        errors.append(f"{page.name}: cannot inspect fragment target {raw_url}")
                        continue
                if fragment not in target_parser.ids:
                    errors.append(f"{page.name}: local fragment does not exist: {raw_url}")

    indexable_pages = set(parsed_pages) - noindex_pages
    graph: dict[Path, set[Path]] = {page: set() for page in indexable_pages}
    for page in indexable_pages:
        for tag, attrs in parsed_pages[page].tags:
            if tag != "a" or not attrs.get("href"):
                continue
            target_info = local_target(page, str(attrs["href"]))
            if target_info and target_info[0] in indexable_pages:
                graph[page].add(target_info[0])
    home = ROOT / "index.html"
    reachable = {home} if home in graph else set()
    queue = deque(reachable)
    while queue:
        for target in graph[queue.popleft()] - reachable:
            reachable.add(target)
            queue.append(target)
    for page in sorted(indexable_pages - reachable):
        errors.append(f"{page.name}: indexable page is not reachable from the homepage through HTML links")

    try:
        sitemap_root = ElementTree.parse(SITEMAP).getroot()
    except (OSError, ElementTree.ParseError) as error:
        return errors + [f"sitemap.xml: could not parse sitemap: {error}"]

    sitemap_urls = [
        (node.text or "").strip()
        for node in sitemap_root.iter()
        if node.tag.rsplit("}", 1)[-1] == "loc"
    ]
    if len(sitemap_urls) != len(set(sitemap_urls)):
        errors.append("sitemap.xml: duplicate URL entries found")

    expected_sitemap = {
        canonical_urls[page]
        for page in pages
        if page in canonical_urls and page not in noindex_pages
    }
    actual_sitemap = set(sitemap_urls)
    for url in sorted(expected_sitemap - actual_sitemap):
        errors.append(f"sitemap.xml: missing indexable page {url}")
    for url in sorted(actual_sitemap - expected_sitemap):
        errors.append(f"sitemap.xml: URL is not an indexable canonical page {url}")

    if not errors:
        print(
            f"Static site validation passed: {len(pages)} HTML pages, "
            f"{len(expected_sitemap)} sitemap URLs, local links/assets/fragments, "
            "unique titles (max 70 characters), homepage reachability, canonical tags, "
            "H1s, JSON-LD, and WhatsApp links."
        )
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Static site validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
