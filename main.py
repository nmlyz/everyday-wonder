#!/usr/bin/env python3
"""Write one sentence about a small moment of everyday wonder to /output/entry.txt.

Standard library only, no network. Deterministic: the sentence is a
constant, so every run writes byte-identical output.
"""

import os

ENTRY = "My umbrella, opened indoors by mistake, made the hallway smell briefly of rain that had not fallen yet."

MAX_CHARS = 200


def check(text):
    if not text or text != text.strip() or len(text) > MAX_CHARS:
        raise ValueError("entry must be 1-200 non-blank characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be a single sentence")
    return text


def main():
    text = check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is the sentence, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
