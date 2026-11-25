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


def validate_entry(text: str) -> str:
    """Validate the entry against the contest rules.

    The sealed scorer requires UTF-8 text of 1 to 400 characters that is
    not only white space. Returns the cleaned text on success.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty or only whitespace")
    if len(cleaned) > 400:
        raise ValueError(
            f"entry is {len(cleaned)} chars, exceeds the 400-char limit"
        )
    return cleaned


def write_entry(text: str, path: str = "/output/entry.txt") -> int:
    """Validate and write the entry, returning its character count."""
    cleaned = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(cleaned)
    return len(cleaned)


def main() -> None:
    count = write_entry(RANT)
    words = len(RANT.split())
    print(f"Entry OK: {count} chars, {words} words (limit 400 chars)")
    print(f"Wrote {count} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
