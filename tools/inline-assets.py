#!/usr/bin/env python3
"""Rewrite a theme CSS file with its local url() assets inlined as data URIs.

The theme source keeps readable relative paths (``url('../../assets/logos/cscs.png')``)
so it stays diffable. Marp inlines the theme into the rendered HTML, where those
relative paths would resolve against the *output* directory and break, so the build
generates a self-contained copy instead.

Usage: python3 tools/inline-assets.py slides/theme/cscs.css -o build/theme/cscs.css
"""

from __future__ import annotations

import argparse
import base64
import mimetypes
import pathlib
import re
import sys

URL_RE = re.compile(r"""url\(\s*(['"]?)(?!data:|https?:)([^'")]+)\1\s*\)""")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("-o", "--output", required=True, type=pathlib.Path)
    args = parser.parse_args()

    css = args.source.read_text(encoding="utf-8")
    base = args.source.parent
    inlined = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal inlined
        asset = (base / match.group(2)).resolve()
        if not asset.is_file():
            print(f"inline-assets.py: warning: missing {asset}", file=sys.stderr)
            return match.group(0)
        mime = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
        payload = base64.b64encode(asset.read_bytes()).decode("ascii")
        inlined += 1
        return f"url('data:{mime};base64,{payload}')"

    css = URL_RE.sub(replace, css)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(css, encoding="utf-8")

    print(f"inline-assets.py: wrote {args.output} ({inlined} asset(s) inlined)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
