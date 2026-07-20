"""Build and optionally submit the site's current HTML URLs to IndexNow."""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


SITE_URL = "https://www.medicallawturkey.com"
DOMAIN = "www.medicallawturkey.com"
INDEXNOW_KEY = "4dc6620e67ccf15285b578afaa33ec35"
KEY_FILE = f"{INDEXNOW_KEY}.txt"
PAYLOAD_PATH = Path(__file__).with_name("indexnow_request.json")


def build_payload() -> dict:
    """Return one URL for every root-level HTML page in this static site."""
    html_files = sorted(Path(__file__).parent.glob("*.html"), key=lambda path: path.name)
    urls = [
        f"{SITE_URL}/" if page.name == "index.html" else f"{SITE_URL}/{page.name}"
        for page in html_files
    ]
    return {
        "host": DOMAIN,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{SITE_URL}/{KEY_FILE}",
        "urlList": urls,
    }


def write_payload(payload: dict) -> None:
    PAYLOAD_PATH.write_text(json.dumps(payload, indent=4) + "\n", encoding="utf-8")
    print(f"Generated {PAYLOAD_PATH.name} with {len(payload['urlList'])} URLs.")


def submit(payload: dict) -> None:
    request = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"IndexNow submission succeeded with HTTP {response.status}.")
    except urllib.error.HTTPError as error:
        response_body = error.read().decode("utf-8", errors="replace").strip()
        detail = f": {response_body}" if response_body else ""
        raise SystemExit(f"IndexNow submission failed with HTTP {error.code}{detail}") from error
    except urllib.error.URLError as error:
        raise SystemExit(f"IndexNow submission failed: {error.reason}") from error


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--submit",
        action="store_true",
        help="submit the generated URL list to the IndexNow API",
    )
    args = parser.parse_args()

    payload = build_payload()
    write_payload(payload)
    if args.submit:
        submit(payload)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Interrupted.")
