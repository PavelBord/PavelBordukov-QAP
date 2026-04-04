from typing import List, Dict
import string


def read_lines(filename: str) -> List[str]:
    with open(
        filename,
        "r",
    ) as f:
        f.readlines()
        return [line.strip() for line in f]


def write_lines(filename: str, lines: List[str]) -> None:
    with open(
        filename,
        "w",
    ) as f:
        f.writelines(lines)


def count_words(filename: str) -> Dict[str, int]:
    with open(
        filename,
        "r",
    ) as f:
        text = f.read().lower()

        for char in string.punctuation:
            text = text.replace(char, "")

        words = text.split()

        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
            return word_counts
