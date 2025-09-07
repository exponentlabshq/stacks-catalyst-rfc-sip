#!/usr/bin/env python3
import json
import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)
    return name.strip("-_.")


def extract_first_post_html(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    # Discourse structure: first post is article with data-post-number="1"
    # or the first .topic-post element
    post = soup.select_one('article[data-post-number="1"]')
    if not post:
        post = soup.select_one(".topic-post")
    if not post:
        return None
    # We want the full block similar to the provided example, which lives within .row
    row = post.select_one(".row")
    return str(row if row else post)


def fetch_first_post_via_json(session: requests.Session, url: str) -> str | None:
    json_url = url.rstrip('/') + '.json'
    try:
        resp = session.get(json_url, timeout=30)
        resp.raise_for_status()
    except Exception:
        return None
    try:
        data = resp.json()
    except Exception:
        return None
    posts = (data.get("post_stream") or {}).get("posts") or []
    if not posts:
        return None
    first = posts[0]
    cooked = first.get("cooked")
    if not cooked:
        return None
    # Wrap cooked in a minimal structure similar to the requested block
    # We intentionally keep it simple and stable for downstream processing
    wrapped = (
        '<div class="row">'
        '<div class="topic-body clearfix">'
        '<div class="regular contents">'
        f'<div class="cooked">{cooked}</div>'
        '</div>'
        '</div>'
        '</div>'
    )
    return wrapped


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape Discourse first post (cooked HTML) for forum topics.")
    parser.add_argument("--input", default="stacks-forum-sip-pages.json", help="JSON file with [{url, lastmod}]")
    parser.add_argument("--url", help="Single forum topic URL to scrape")
    parser.add_argument("--outdir", default="scrapes/forum-first-posts", help="Output directory")
    args = parser.parse_args()

    if args.url:
        items = [{"url": args.url}]
    else:
        json_path = Path(args.input)
        if not json_path.exists():
            print(f"{json_path} not found", file=sys.stderr)
            sys.exit(1)
        items = json.loads(json_path.read_text(encoding="utf-8"))

    out_dir = Path(args.outdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119 Safari/537.36"
    })

    written = 0
    for item in items:
        url = item.get("url")
        if not url:
            continue
        # Prefer JSON endpoint for reliable server-rendered cooked HTML
        fragment = fetch_first_post_via_json(session, url)
        if not fragment:
            # Fallback: try parsing raw HTML (may be JS-hydrated and fail)
            try:
                resp = session.get(url, timeout=30)
                resp.raise_for_status()
                fragment = extract_first_post_html(resp.text)
            except Exception as e:
                print(f"Failed to fetch {url}: {e}", file=sys.stderr)
                fragment = None
        if not fragment:
            print(f"No first post found on {url}", file=sys.stderr)
            continue

        parsed = urlparse(url)
        slug = parsed.path.strip("/").replace("/", "_")
        fname = sanitize_filename(slug) + ".html"
        out_path = out_dir / fname
        out_path.write_text(fragment, encoding="utf-8")
        written += 1
        print(f"Wrote {out_path}")

    print(f"Done. Wrote {written} files to {out_dir}")


if __name__ == "__main__":
    main()


