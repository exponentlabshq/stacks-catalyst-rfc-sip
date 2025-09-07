#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SIP_START_RE = re.compile(r"^\*{0,2}SIP Number:\*{0,2}\s*(\d+)")
TITLE_RE = re.compile(r"^\*{0,2}Title:\*{0,2}\s*(.+)")
TYPE_RE = re.compile(r"^\*{0,2}Type:\*{0,2}\s*(.+)")
LICENSE_RE = re.compile(r"^\*{0,2}License:\*{0,2}\s*(.+)")
AUTHORS_RE = re.compile(r"^\*{0,2}(?:Author|Authors):\*{0,2}\s*(.*)")
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


def _line_looks_like_field_header(line: str) -> bool:
    candidates = (
        "SIP Number:", "Title:", "Author:", "Authors:", "Consideration:",
        "Type:", "Status:", "Created:", "License:", "Sign-off:", "Discussions-To:"
    )
    for key in candidates:
        if key in line.replace("**", ""):
            return True
    return line.startswith("# ") or line.startswith("## ")


def parse_markdown_sip(text: str) -> Dict[str, Optional[str]]:
    result: Dict[str, Optional[str]] = {
        "sip": None,
        "title": None,
        "type": None,
        "license": None,
        "authors": [],
        "emails": [],
        "copyright": None,
        "path": None,
    }

    emails: set = set()
    lines = text.splitlines()
    authors_collect_mode = False
    author_lines: List[str] = []

    for raw in lines:
        line = raw.strip()

        # Always collect emails
        for email in EMAIL_RE.findall(line):
            emails.add(email)

        # Parse primary fields (bold or plain labels)
        if result.get("sip") is None:
            m = SIP_START_RE.match(line)
            if m:
                result["sip"] = m.group(1)
                continue

        if result.get("title") is None:
            m = TITLE_RE.match(line)
            if m:
                result["title"] = m.group(1).strip()
                continue

        if result.get("type") is None:
            m = TYPE_RE.match(line)
            if m:
                result["type"] = m.group(1).strip()
                continue

        if result.get("license") is None:
            m = LICENSE_RE.match(line)
            if m:
                result["license"] = m.group(1).strip()
                continue

        m = AUTHORS_RE.match(line)
        if m:
            rest = m.group(1).strip()
            authors_collect_mode = True
            if rest:
                author_lines.append(rest)
            continue

        if authors_collect_mode:
            if not line or _line_looks_like_field_header(line):
                authors_collect_mode = False
            else:
                author_lines.append(line)

        # Copyright heuristic
        if ("copyright" in line.lower()) and ("sip" in line.lower()) and not result.get("copyright"):
            result["copyright"] = line.strip()

    # Post-process authors
    authors: List[str] = []
    if author_lines:
        # Join with spaces, then split by bullets or commas
        # Preserve list items as separate authors when possible
        normalized: List[str] = []
        for entry in author_lines:
            entry = entry.strip().lstrip("-• ")
            if not entry:
                continue
            # Split on trailing commas, but keep lines that are clearly a single author
            parts = [p for p in re.split(r",\s*(?![^()]*\))", entry) if p.strip()]
            normalized.extend(parts if len(parts) > 1 else [entry])

        cleaned: List[str] = []
        for frag in normalized:
            name = clean_author_fragment(frag)
            if name and name.lower() not in {"authors", "author"}:
                cleaned.append(name)
        # Remove duplicates preserving order
        seen = set()
        for n in cleaned:
            if n not in seen:
                authors.append(n)
                seen.add(n)

    result["authors"] = authors
    result["emails"] = sorted(emails)
    return result


def parse_directory(dir_path: Path, max_sip: int = 29) -> List[Dict[str, Optional[str]]]:
    results: List[Dict[str, Optional[str]]] = []
    # Discover sip-XXX directories
    sip_dirs = []
    for child in dir_path.iterdir():
        if child.is_dir():
            m = re.match(r"sip-(\d{3})$", child.name)
            if m:
                n = int(m.group(1))
                if n <= max_sip:
                    sip_dirs.append((n, child))
    sip_dirs.sort(key=lambda t: t[0])

    for n, sip_dir in sip_dirs:
        sip_id = f"{n:03d}"
        md_files = sorted(sip_dir.glob("*.md"))
        if not md_files:
            entry: Dict[str, Optional[str]] = {"sip": sip_id, "title": None, "type": None, "license": None, "authors": [], "emails": [], "copyright": None}
        else:
            content = md_files[0].read_text(encoding="utf-8", errors="ignore")
            entry = parse_markdown_sip(content)
            if not entry.get("sip"):
                entry["sip"] = sip_id
            # store relative path including sips-main/sips/... for serving
            rel_path = f"{dir_path.parent.name}/{dir_path.name}/{sip_dir.name}/{md_files[0].name}"
            entry["path"] = rel_path
        results.append(entry)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse SIP sources into JSON.")
    parser.add_argument("--input", required=True, help="Path to SIP text file or directory of SIPs")
    parser.add_argument("--output", required=False, help="Path to output JSON file")
    args = parser.parse_args()

    input_path = Path(args.input)
    if input_path.is_dir():
        # Expecting a directory like sips-main/sips
        data = parse_directory(input_path, max_sip=29)
    else:
        text = input_path.read_text(encoding="utf-8")
        data = parse_sips(text)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()


