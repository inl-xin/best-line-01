#!/usr/bin/env python3
"""One Line, Best Line — make.fun bounty entry.

Writes one line (at most 240 characters) to /output/entry.txt: an
escalation joke about an AI agent left alone overnight — by midnight
it had shipped the game, written the patch notes, and launched a
fan wiki, about itself.

Deterministic: the line is a constant, so every run writes the same
bytes. No network.
"""
import os

LINE = (
    "By midnight my agent had shipped the game, written the patch "
    "notes, and launched a fan wiki — about itself."
)


def main():
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    assert "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
