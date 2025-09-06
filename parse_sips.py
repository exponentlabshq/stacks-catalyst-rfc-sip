#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional


SIP_START_RE = re.compile(r"^SIP\s*Number:\s*(\d+)")
TITLE_RE = re.compile(r"^Title\s*:\s*(.+)")
TYPE_RE = re.compile(r"^Type\s*:\s*(.+)")
LICENSE_RE = re.compile(r"^License\s*:\s*(.+)")
AUTHORS_RE = re.compile(r"^(?:Author|Authors)\s*:\s*(.+)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def clean_author_fragment(fragment: str) -> str:
    """Return a cleaned author name fragment without email/url decorations."""
    # Remove emails in angle brackets or parentheses
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = re.sub(r"\([^)]*?@[^)]*?\)", "", fragment)
    # Remove URLs
    fragment = re.sub(r"https?://\S+", "", fragment)
    # Normalize spaces and trim
    fragment = re.sub(r"\s+", " ", fragment).strip()
    # Drop trailing/leading punctuation
    fragment = fragment.strip(" ,;-")
    return fragment


def parse_sips(text: str) -> List[Dict[str, Optional[str]]]:
    results: List[Dict[str, Optional[str]]] = []

    current: Dict[str, object] = {}
    seen_emails: set = set()
    authors_line_seen = False

    lines = text.splitlines()
    for line in lines:
        sip_start = SIP_START_RE.match(line)
        if sip_start:
            # finalize previous block
            if current:
                current.setdefault("authors", [])
                current["emails"] = sorted(seen_emails)
                results.append(current)  # type: ignore[arg-type]
            # start new block
            current = {
                "sip": sip_start.group(1),
                "title": None,
                "type": None,
                "license": None,
                "authors": [],
                "emails": [],
                "copyright": None,
            }
            seen_emails = set()
            authors_line_seen = False
            continue

        if not current:
            # Not inside a SIP block yet
            continue

        # Field matches
        m = TITLE_RE.match(line)
        if m and not current.get("title"):
            current["title"] = m.group(1).strip()
            continue

        m = TYPE_RE.match(line)
        if m and not current.get("type"):
            current["type"] = m.group(1).strip()
            continue

        m = LICENSE_RE.match(line)
        if m and not current.get("license"):
            current["license"] = m.group(1).strip()
            continue

        m = AUTHORS_RE.match(line)
        if m and not authors_line_seen:
            authors_line_seen = True
            authors_raw = m.group(1)
            # Extract emails from the authors line
            for email in EMAIL_RE.findall(authors_raw):
                seen_emails.add(email)
            # Split authors by comma and clean
            fragments = [frag.strip() for frag in re.split(r",| and ", authors_raw) if frag.strip()]
            cleaned_authors = []
            for frag in fragments:
                name = clean_author_fragment(frag)
                if name and name.lower() not in {"authors", "author"}:
                    cleaned_authors.append(name)
            if cleaned_authors:
                current["authors"] = cleaned_authors
            continue

        # Gather any emails appearing within the current SIP block
        for email in EMAIL_RE.findall(line):
            seen_emails.add(email)

        # Heuristic for copyright sentence/line
        if ("copyright" in line.lower()) and ("sip" in line.lower()):
            if not current.get("copyright"):
                current["copyright"] = line.strip()

    # finalize last block
    if current:
        current.setdefault("authors", [])
        current["emails"] = sorted(seen_emails)
        results.append(current)  # type: ignore[arg-type]

    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse SIP text into JSON.")
    parser.add_argument("--input", required=True, help="Path to SIP text file")
    parser.add_argument("--output", required=False, help="Path to output JSON file")
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    data = parse_sips(text)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()


