#!/usr/bin/env python3
"""One Letter for Your Day — W for wired.

Writes exactly one letter, W, to /output/entry.txt. Nothing else.

Why "wired": of all the W-words for a day, "wired" wins because it is
vivid (you can picture the buzzing, over-caffeinated energy), funny
(it turns a whole day into a live wire that will not sit still), and
real (it is how an overstimulated day actually feels). One letter, W,
carries that whole charge.
"""

import os

LETTER = "W"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
