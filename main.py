"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of planet Earth —
to /output/entry.txt. The gate requires UTF-8 text of 1 to 200
characters, not only white space.
"""

import os

ENTRY = (
    "Earth: the dominant species built a machine that washes dishes, "
    "then stands beside it arguing about how to load it correctly. "
    "4/5 stars \u2014 would visit again, purely to watch."
)


def main() -> None:
    # Enforce the gate locally: 1-200 characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be blank"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
