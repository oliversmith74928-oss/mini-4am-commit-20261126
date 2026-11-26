"""The 4AM Commit: write one funny commit message to /output/entry.txt.

Python standard library only. Deterministic: every run writes exactly the
same bytes, no clock, no randomness, no network.
"""

import os

# Written at 4am, like all the best commits.
LINE = (
    "fix: the bug I wrote at 2am, found at 3am, fixed at 4am by writing "
    "the bug I will find at 5am. this is not a loop, it is a career."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
