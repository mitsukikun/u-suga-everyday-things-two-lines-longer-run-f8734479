#!/usr/bin/env python3
"""Everyday Things, Two Lines — queue as a human caterpillar.

Writes the two-line entry to /output/entry.txt and to entry.txt
next to this file.
"""

import os

LINE1 = (
    "A queue is a human caterpillar, each person one segment "
    "shuffling forward a tiny step at a time toward the ice-cream "
    "counter at the front."
)
LINE2 = (
    "It maps how everyone stays joined in order and shuffles forward "
    "waiting their turn, but it leaves out that people can step out, "
    "let someone go ahead, or join a shorter queue, while "
    "a caterpillar's segments are stuck together and can never choose at all."
)


def main():
    text = LINE1 + "\n" + LINE2 + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
