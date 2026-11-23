#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt: the single word
the entrant's Indonesian grandma would text about AI.

The word is "Waduh" — the classic Indonesian grandma reaction to anything
new and alarming. One word, warm, a little baffled, unmistakably grandma.

Pure Python standard library only.
"""

import os

WORD = "Waduh"


def validate_word(word: str) -> str:
    """Guard: the entry must be exactly one word, 1-30 code points.

    Rejects anything blank, multi-line, or containing whitespace of any
    kind, so the file the grader reads can only ever hold a single word.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if not word or word.strip() == "":
        raise ValueError("word must not be blank")
    if len(word) != len(word.strip()):
        raise ValueError("word must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace (exactly one word)")
    if "\n" in word or "\r" in word:
        raise ValueError("word must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("word must contain no control characters")
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    return word


def main() -> None:
    word = validate_word(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
