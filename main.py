#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry program.

Writes the one-line error/postmortem the agent prints the instant it
breaks production to /output/entry.txt (or $ENTRY_OUT when set), and
prints the same line to stdout. The sealed scorer reads entry.txt:
UTF-8 text, 1 to 200 characters, not only whitespace, single line.
"""

import os
import sys

ENTRY_TEXT = (
    "I ran DROP DATABASE on prod instead of staging; the backup is "
    "from last March, I have never restored from it, and checkout "
    "is already down."
)


def entry_is_valid(text: str) -> bool:
    """Gate mirror: single line, 1-200 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped or len(text) > 200:
        return False
    return "\n" not in stripped and "\r" not in stripped


def publish_entry(line: str) -> int:
    """Validate, write the entry file, then print the line verbatim."""
    if not entry_is_valid(line):
        print("entry fails the 1-200 char single-line gate", file=sys.stderr)
        return 1
    destination = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(destination, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != line:
        print("entry did not round-trip cleanly", file=sys.stderr)
        return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(publish_entry(ENTRY_TEXT))
