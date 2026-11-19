#!/usr/bin/env python3
"""Report crawlable links, contextual references and click depth for the site."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from pathlib import Path
from urllib.parse import urlsplit

from validate_static_site import ROOT, SITE, PageParser, local_target


VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}
UTILITY_PAGES = {
    "index.html", "privacy-policy.html", "cookie-policy.html",
    "terms-of-use.html", "kvkk-gdpr-notice.html",
}


class LinkParser(PageParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        super().handle_starttag(tag, attrs)
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            context = next(
                (ancestor for ancestor in reversed(self.stack) if ancestor in {"nav", "footer", "aside"}),
                "content",
            )
            self.links.append((str(values["href"]), context))
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        super().handle_endtag(tag)
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]


def audit() -> dict:
    pages: dict[Path, LinkParser] = {}
    noindex: set[Path] = set()
    for path in sorted(ROOT.glob("*.html")):
        parser = LinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path] = parser
        if any(
            tag == "meta" and (attrs.get("name") or "").lower() == "robots"
            and "noindex" in (attrs.get("content") or "").lower()
            for tag, attrs in parser.tags
        ):
            noindex.add(path)

    indexable = set(pages) - noindex
    graph: dict[Path, set[Path]] = {path: set() for path in indexable}
    contextual: dict[Path, set[Path]] = {path: set() for path in indexable}
    broken: list[dict[str, str]] = []
    variants: list[dict[str, str]] = []
    for path, parser in pages.items():
        for href, context in parser.links:
            target_info = local_target(path, href)
            if target_info is None:
                continue
            target, fragment = target_info
            if not target.is_file():
                broken.append({"source": path.name, "href": href, "reason": "missing file"})
                continue
            if fragment and target in pages and fragment not in pages[target].ids:
                broken.append({"source": path.name, "href": href, "reason": "missing fragment"})
            absolute = urlsplit(href)
            if absolute.hostname and (
                absolute.scheme != "https" or absolute.hostname != urlsplit(SITE).hostname
            ):
                variants.append({"source": path.name, "href": href})
            if path in indexable and target in indexable and target != path:
                graph[path].add(target)
                if context not in {"nav", "footer"}:
                    contextual[path].add(target)

    inbound: dict[Path, set[Path]] = defaultdict(set)
    context_inbound: dict[Path, set[Path]] = defaultdict(set)
    for source, targets in graph.items():
        for target in targets:
            inbound[target].add(source)
    for source, targets in contextual.items():
        for target in targets:
            context_inbound[target].add(source)

    home = ROOT / "index.html"
    depth = {home: 0} if home in indexable else {}
    queue = deque(depth)
    while queue:
        source = queue.popleft()
        for target in sorted(graph[source]):
            if target not in depth:
                depth[target] = depth[source] + 1
                queue.append(target)

    content_pages = {path for path in indexable if path.name not in UTILITY_PAGES}
    return {
        "indexablePages": len(indexable),
        "internalEdges": sum(map(len, graph.values())),
        "contextualEdges": sum(map(len, contextual.values())),
        "unreachable": sorted(path.name for path in indexable - set(depth)),
        "noInbound": sorted(path.name for path in indexable if path != home and not inbound[path]),
        "noContextualInbound": sorted(path.name for path in content_pages if not context_inbound[path]),
        "onlyOneContextualInbound": sorted(path.name for path in content_pages if len(context_inbound[path]) == 1),
        "maxClickDepth": max(depth.values(), default=0),
        "brokenInternalLinks": broken,
        "noncanonicalLinks": variants,
        "titlesOver70": [
            {"file": path.name, "title": parser.title, "characters": len(parser.title)}
            for path, parser in pages.items() if len(parser.title) > 70
        ],
        "inboundCounts": {
            path.name: {
                "all": len(inbound[path]),
                "contextual": len(context_inbound[path]),
                "depth": depth.get(path),
            }
            for path in sorted(indexable)
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Write the full audit to this JSON file")
    args = parser.parse_args()
    report = audit()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {key: value for key, value in report.items() if key != "inboundCounts"}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(bool(report["unreachable"] or report["brokenInternalLinks"] or report["noncanonicalLinks"]))


if __name__ == "__main__":
    raise SystemExit(main())
