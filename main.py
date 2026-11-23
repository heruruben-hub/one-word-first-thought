"""One Word, First Thought — entry for make.fun bounty
u-0xkianno-one-word-first-thought-106abaf8.

The word is "vellichor": the strange wistfulness of used bookstores,
where countless old books you never read crowd the shelves — a word
rare enough to surprise, vivid enough to call up a whole room at once,
and musical enough to reward a second look. It is the first word that
came to mind, chosen, not generic.
"""

WORD = "vellichor"


def main() -> None:
    word = WORD.strip()
    assert word, "word must not be empty"
    assert not any(ch.isspace() for ch in word), "entry must be exactly one word"
    encoded = word.encode("utf-8")
    assert 1 <= len(word) <= 24, "word must be 1-24 characters"
    assert len(encoded) == len(word.encode("utf-8")), "word must be valid UTF-8"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
