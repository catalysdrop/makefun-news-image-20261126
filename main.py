#!/usr/bin/env python3
"""Entry for make.fun news-image-20261126: write the front-page image
summarising 26 November 2026's world news to /output/entry.png.

Deterministic: copies the bundled entry.png byte-for-byte, so both runs
produce identical output. No network, no randomness, no other input.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    os.makedirs("/output", exist_ok=True)
    dst = os.path.join("/output", "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    main()
