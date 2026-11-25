"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The sealed scorer requires UTF-8 text of
1 to 400 characters, not only white space.
"""

import os

RANT = (
    "The self-checkout machine shouted 'unexpected item in the bagging area' "
    "at a bag of rice I scanned myself, in front of twelve people, then "
    "demanded a human come confirm that rice is, in fact, rice. I bought "
    "the rice. I scanned the rice. The machine still needed a witness."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
