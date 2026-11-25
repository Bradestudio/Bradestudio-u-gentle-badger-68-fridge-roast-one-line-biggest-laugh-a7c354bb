"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes a single roast line (max 200 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Python stdlib only, no network,
no local imports, deterministic.
"""

import os

ENTRY = (
    "My smart fridge updated its firmware at 2 a.m. and now it won't "
    "open until I rate the update five stars."
)


def gate_check(text):
    """Gate: one line, 1-200 chars, no leading/trailing whitespace,
    no double space, no control characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry has a double space")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry has a control character")
    if "\u00a0" in text:
        raise ValueError("entry has a non-breaking space")


def main():
    gate_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
