"""Write the one-line passive-aggressive fridge note to /output/entry.txt.

Standard library only. The entry is a single line of plain text, at most
200 characters: a note a smart fridge leaves for its owner.
"""

import os
import sys

ENTRY = (
    "Day 6: the lasagna from Tuesday is still here. "
    "I have named it. It pays rent now."
)


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("error: entry contains a control character", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("error: entry is %d chars, over the 200 limit" % len(text),
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars, %d bytes utf-8)"
          % (out_path, len(text), len(text.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
