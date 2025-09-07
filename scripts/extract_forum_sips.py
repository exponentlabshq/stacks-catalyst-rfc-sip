#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser(description="Extract forum links with 'SIP' in title from 2025 sitemap and write JSON.")
    p.add_argument("--input", required=True, help="Path to forum sitemap XML")
    p.add_argument("--output", default="stacks-forum-sip-pages.json", help="Output JSON path")
    args = p.parse_args()

    xml = Path(args.input).read_text(encoding="utf-8", errors="ignore")

    # Extract <url> blocks
    blocks = re.findall(r"<url>(.*?)</url>", xml, flags=re.DOTALL)

    items = []
    for b in blocks:
        loc_m = re.search(r"<loc>(.*?)</loc>", b)
        last_m = re.search(r"<lastmod>(.*?)</lastmod>", b)
        if not loc_m or not last_m:
            continue
        loc = loc_m.group(1).strip()
        last = last_m.group(1).strip()
        if not last.startswith("2025-"):
            continue
        # Heuristic: include if the URL path contains 'sip' (category or slug)
        path = loc.split('://',1)[-1]
        if re.search(r"\bsip\b", path, flags=re.IGNORECASE) or re.search(r"sip-\d+", path, flags=re.IGNORECASE):
            items.append({
                "url": loc,
                "lastmod": last
            })

    Path(args.output).write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(items)} items to {args.output}")


if __name__ == "__main__":
    main()


