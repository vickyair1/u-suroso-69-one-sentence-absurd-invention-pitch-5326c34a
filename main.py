#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt, and prints it to stdout.
The entry text is exactly 85 characters: one sentence, no trailing newline
in the file, so the gate counts exactly the entry itself.
"""

import os

ENTRY = "An alarm clock that apologizes to you each morning, then snoozes itself out of guilt."


def validate():
    """Check the entry meets the pitch gate: exactly 85 chars, one sentence."""
    if len(ENTRY) != 85:
        raise ValueError(f"entry must be exactly 85 characters, got {len(ENTRY)}")
    if not ENTRY.endswith("."):
        raise ValueError("entry must be a single sentence ending with a period")
    if "\n" in ENTRY:
        raise ValueError("entry must not contain a newline")


def write_entry():
    """Write the entry to /output/entry.txt with no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    validate()
    write_entry()
    print(ENTRY)


if __name__ == "__main__":
    main()
