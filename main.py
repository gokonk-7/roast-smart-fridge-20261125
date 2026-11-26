#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) to /output/entry.txt.
The line is a constant: the program is fully deterministic and prints
exactly what it writes, so the entry can be verified by eye.
"""

import os

ENTRY = (
    "My smart fridge lost Wi-Fi and forgot how to stay cold \u2014 "
    "impressive for a box whose only job since 1913 has been staying cold."
)


def main() -> None:
    # The gate refuses entries over 160 characters: fail loudly here
    # instead of shipping an invalid line.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
