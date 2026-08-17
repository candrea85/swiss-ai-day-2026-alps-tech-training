#!/usr/bin/env python3
"""Report slides and estimated speaking time per module.

Sixty minutes is a hard ceiling for the session, and the only cheap way to see it
slipping is to count slides after every edit. The estimate is the house rule from
CLAUDE.md: roughly one minute per content slide, so a module divider counts too and
demos are not modelled at all. Treat it as a smoke alarm, not a stopwatch.

Usage: python3 tools/slide-count.py slides/*.md
"""

from __future__ import annotations

import pathlib
import sys

BUDGET_MINUTES = 60


def count_slides(path: pathlib.Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    separators = sum(1 for line in lines if line.strip() == "---")
    # A YAML front matter block contributes two "---" lines that are not separators.
    front_matter = 2 if lines and lines[0].strip() == "---" else 0
    return separators - front_matter + 1


def main(argv: list[str]) -> int:
    paths = [pathlib.Path(a) for a in argv]
    if not paths:
        print("slide-count.py: no slide files yet", file=sys.stderr)
        return 0

    total = 0
    backup = 0
    for path in paths:
        slides = count_slides(path)
        # Backup slides sit after the wrap-up and are shown only on request, so they
        # must not count against the 60 minutes.
        if "backup" in path.name:
            backup += slides
            print(f"{str(path):<40} {slides:>3} slides            (backup, not budgeted)")
            continue
        total += slides
        print(f"{str(path):<40} {slides:>3} slides  ~{slides:>3} min")

    if total > BUDGET_MINUTES:
        verdict = " — OVER BUDGET"
    else:
        verdict = f" — {BUDGET_MINUTES - total} min of slack"
    print(f"{'TOTAL (presented)':<40} {total:>3} slides  ~{total:>3} min "
          f"(budget {BUDGET_MINUTES} min){verdict}")
    if backup:
        print(f"{'plus backup':<40} {backup:>3} slides")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
