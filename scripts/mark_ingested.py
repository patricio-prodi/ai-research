#!/usr/bin/env python3
"""
Mark a raw source file as ingested by changing its `inbox` tag to `ingested`.

Usage:
    python3 scripts/mark_ingested.py "raw/filename.md"
    python3 scripts/mark_ingested.py "filename.md"   # also works
"""

import sys
import os
import re

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw')


def mark_ingested(target: str) -> None:
    # Resolve path — accept either full path or bare filename
    if os.path.isfile(target):
        path = target
    else:
        path = os.path.join(RAW_DIR, os.path.basename(target))

    if not os.path.isfile(path):
        print(f"ERROR: file not found: {path}")
        sys.exit(1)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        print(f"ERROR: no YAML frontmatter found in {path}")
        sys.exit(1)

    # Only operate inside the frontmatter block
    match = re.match(r'^(---\n.*?\n---)', content, re.DOTALL)
    if not match:
        print(f"ERROR: could not parse frontmatter in {path}")
        sys.exit(1)

    frontmatter = match.group(1)

    if 'ingested' in frontmatter:
        print(f"Already ingested: {os.path.basename(path)}")
        return

    if 'inbox' not in frontmatter:
        print(f"ERROR: no 'inbox' tag found in frontmatter of {path}")
        sys.exit(1)

    new_frontmatter = re.sub(r'\binbox\b', 'ingested', frontmatter, count=1)
    new_content = content.replace(frontmatter, new_frontmatter, 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Marked as ingested: {os.path.basename(path)}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/mark_ingested.py <filename>")
        sys.exit(1)
    mark_ingested(sys.argv[1])
