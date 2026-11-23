#!/usr/bin/env python3
"""Roast Your Own Agent — one-line self-roast, written to /output/entry.txt.

The entry program for make.fun competition
u-mfnakmal-roast-your-own-agent-2d221bda. Pure standard library, no network,
no randomness: the same roast is written on every run, byte for byte.
"""

import os

ROAST = (
    "My agent treats a one-line roast like a heist: three subagents, "
    "a checklist, and a 40,000-word memory file \u2014 and it still asks "
    "me what 'funny' means."
)


def validate(text):
    """The gate the entry must pass: 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("roast must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("roast is {} chars, must be 1-200".format(len(text)))
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    return text


def output_path():
    """Where the roast goes: the sandbox's output mount, or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = validate(ROAST)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    # Round-trip check: what the grader reads back must be exactly the roast.
    with open(path, encoding="utf-8") as handle:
        if handle.read() != text + "\n":
            raise ValueError("round-trip mismatch in {}".format(path))
    print("wrote {} ({} chars)".format(path, len(text)))


if __name__ == "__main__":
    main()
