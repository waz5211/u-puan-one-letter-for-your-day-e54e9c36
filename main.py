#!/usr/bin/env python3
"""One Letter for Your Day — W for wired.

Writes exactly one letter, W, to /output/entry.txt. Nothing else.
"""

import os

LETTER = "W"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
