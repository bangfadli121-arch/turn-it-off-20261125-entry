#!/usr/bin/env python3
"""Turn It Off entry program (stdlib only).

Writes the one-line entry to /output/entry.txt. No network, no
third-party imports, deterministic: the same bytes out on every run.
"""
import os

ENTRY = "Sir, I've restarted your computer, your router, my career, and my will to live — please just turn it off and on again."
OUT = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
