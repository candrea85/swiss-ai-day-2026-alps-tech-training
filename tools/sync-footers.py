#!/usr/bin/env python3
"""Put each slide's source on its own footer, derived from the DOCS: line.

The brief requires every content slide to carry a docs.cscs.ch deep link. The footer is
the right place for it: that space is already spent, and it ends in `docs.cscs.ch`
anyway, so replacing the generic address with the specific page costs nothing and adds a
citation the audience can photograph.

The link is not typed twice. Each slide's speaker notes already end with a `DOCS:` line;
this reads it, takes the first URL, and writes the matching `<!-- _footer: ... -->`
directive into the slide. Edit the DOCS line and rerun — never edit the footer by hand.

Slides with no DOCS line (dividers, "Where to read more") keep the deck-wide footer from
the front matter.

Usage: python3 tools/sync-footers.py slides/*.md [--check]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SESSION = "Alps technical training · Swiss AI Initiative Annual Meeting 2026"
DOCS_LINE = re.compile(r"^DOCS:\s*(.+)$", re.MULTILINE)
FOOTER_DIRECTIVE = re.compile(r"^<!-- _footer: .*? -->\n", re.MULTILINE)

# Pages that do not resolve yet. Printing a URL that 404s on a projector costs more
# credibility than a less precise one, so these fall back to a page that exists.
NOT_LIVE = {
    "docs.cscs.ch/platforms/mlp/policies/": "docs.cscs.ch/platforms/mlp/",
}


def first_url(docs_value: str) -> str:
    """The DOCS line may list several sources; the footer carries the primary one."""
    url = docs_value.split("·")[0].strip()
    url = re.sub(r"\s*\(.*\)\s*$", "", url)  # drop trailing "(portal section)" notes
    return NOT_LIVE.get(url, url)


def split_slides(body: str) -> list[str]:
    """Split on separator lines. Join the result with "---\n" to round-trip exactly:
    the separator line's own newline is consumed here."""
    slides, current = [], []
    for line in body.splitlines(keepends=True):
        if line.strip() == "---":
            slides.append("".join(current))
            current = []
        else:
            current.append(line)
    slides.append("".join(current))
    return slides


def process(path: pathlib.Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    end_fm = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    front, body = "".join(lines[: end_fm + 1]), "".join(lines[end_fm + 1 :])

    slides, changed = split_slides(body), 0
    for i, slide in enumerate(slides):
        slide = FOOTER_DIRECTIVE.sub("", slide)
        match = DOCS_LINE.search(slide)
        if match:
            footer = f"<!-- _footer: '{SESSION} · {first_url(match.group(1))}' -->\n"
            slide = footer + slide.lstrip("\n")
            changed += 1
        slides[i] = slide

    return front + "---\n".join(slides), changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sources", nargs="+", type=pathlib.Path)
    ap.add_argument("--check", action="store_true",
                    help="report what would change and exit non-zero, without writing")
    args = ap.parse_args()

    stale = 0
    for path in args.sources:
        updated, count = process(path)
        if updated != path.read_text(encoding="utf-8"):
            stale += 1
            if args.check:
                print(f"sync-footers.py: {path} is out of date")
            else:
                path.write_text(updated, encoding="utf-8")
                print(f"sync-footers.py: {path} — {count} slide footer(s)")
        elif not args.check:
            print(f"sync-footers.py: {path} — {count} slide footer(s), unchanged")

    if args.check and stale:
        print("Run `make footers` to update them.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
