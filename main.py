#!/usr/bin/env python3
"""The 3AM Fridge Text — the one line a smart fridge texts its owner at 3am.

Writes a single line of text (1-140 characters) to /output/entry.txt.
"""

import os

LINE = (
    "3am. Your midnight self keeps promising your morning self a salad. "
    "I kept the receipts \u2014 in the crisper."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
