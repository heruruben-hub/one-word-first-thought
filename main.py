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
    assert len(encoded) <= 24, "word must be at most 24 bytes of UTF-8"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(word)

    # Read the output back and confirm it is byte-identical to the word.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == word, "output file content does not match the word"
    assert len(written.encode("utf-8")) == len(encoded), "output byte length mismatch"


if __name__ == "__main__":
    main()
