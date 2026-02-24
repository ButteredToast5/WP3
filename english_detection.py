import os


def load_dictionary_words(path: str) -> set:
    if not os.path.exists(path):
        raise FileNotFoundError("Dictionary file missing.")

    words = set()

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                words.add(word)

    return words