#!/usr/bin/env python3
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup


PROPOSAL_GLOB = "scrapes/forum-first-posts/stacks-forum-sip-proposal-*.html"


def hyphen_title(slug: str) -> str:
    words = [w for w in slug.split("-") if w]
    return " ".join(w.capitalize() for w in words)


def guess_author_from_fragment(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    ps = soup.find_all("p")
    # Try: last short paragraph that looks like a signature (1-3 words)
    for p in reversed(ps):
        text = (p.get_text() or "").strip()
        if not text:
            continue
        # Skip long paragraphs
        if len(text) > 32:
            continue
        # Prefer single or two words, letters only
        if re.fullmatch(r"[A-Za-z][A-Za-z .-]{0,30}", text):
            return text.strip()
    return None


def load_lastmods(index_path: Path) -> dict[str, str]:
    lastmods: dict[str, str] = {}
    if not index_path.exists():
        return lastmods
    try:
        items = json.loads(index_path.read_text(encoding="utf-8"))
        for it in items:
            url: str | None = it.get("url")
            lm: str | None = it.get("lastmod")
            if not url or not lm:
                continue
            m = re.search(r"/(\d+)(?:$|[/?])", url)
            if not m:
                continue
            topic_id = m.group(1)
            lastmods[topic_id] = lm
    except Exception:
        pass
    return lastmods


def main() -> None:
    repo = Path('.')
    proposal_files = sorted(Path('.').glob(PROPOSAL_GLOB))
    lastmods = load_lastmods(repo / "stacks-forum-sip-pages.json")

    out_items: list[dict] = []

    for f in proposal_files:
        name = f.name  # stacks-forum-sip-proposal-t_<slug>_<id>.html
        m = re.match(r"stacks-forum-sip-proposal-t_(.+)_(\d+)\.html$", name)
        if not m:
            # Skip unknown naming
            continue
        slug_part = m.group(1)
        topic_id = m.group(2)

        # The original slug preserved hyphens, underscores are from replaced '/'
        slug = slug_part.replace("_", "-")
        title = hyphen_title(slug)
        url = f"https://forum.stacks.org/t/{slug}/{topic_id}"

        html = f.read_text(encoding="utf-8")
        cooked_soup = BeautifulSoup(html, "html.parser")
        cooked_div = cooked_soup.select_one(".cooked")
        cooked_html = str(cooked_div) if cooked_div else html

        author = guess_author_from_fragment(cooked_html) or "unknown"
        created = lastmods.get(topic_id)

        out_items.append({
            "id": f"forum-{topic_id}",
            "source": "stacks-forum",
            "status": "Proposal",
            "title": title,
            "slug": slug,
            "topic_id": topic_id,
            "url": url,
            "created": created or None,
            "author": author,
            "html": cooked_html,
        })

    (repo / "submitted-sips.json").write_text(
        json.dumps(out_items, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(out_items)} proposals into submitted-sips.json")


if __name__ == "__main__":
    main()


