"""Project Runeberg parsing exercise."""

from __future__ import annotations
from collections import abc, defaultdict
from itertools import chain, tee
from pathlib import Path
import random
import re
import sys
from typing import TypeVar


def _strip_xml_tags(text: str) -> str:
    return re.sub(r"<.*?>", "", text)


def runeberg_words(path: Path) -> abc.Iterable[str]:
    """Generate words from the Project Runeberg text in `path`."""

    def articles_lines() -> abc.Iterable[str]:
        with open(path / "Articles.lst", "r", encoding="utf-8") as article_file:
            yield from article_file

    basenames = (
        line.split("|")[0] for line in articles_lines() if not line.startswith("#")
    )

    chapter_paths = ((path / basename).with_suffix(".html") for basename in basenames)

    def book_lines() -> abc.Iterable[str]:
        for chapter_path in chapter_paths:
            with open(chapter_path, "r", encoding="utf-8") as chapter_file:
                yield from chapter_file

    without_tags = (_strip_xml_tags(line) for line in book_lines())

    book_words = chain.from_iterable(book_line.split() for book_line in without_tags)

    # Here we could add more steps to the pipeline, i.e.

    # casefolded = (word.casefold() for word in book_words)
    # without_punctuation = (word.strip('.,:;-*') for word in casefolded)
    # without_empty = (word for word in without_punctuation if word)

    yield from book_words


def word_count(words: abc.Iterable[str]) -> int:
    """Count the words in `words`."""
    return sum(1 for _ in words)


def top_ten(words: abc.Iterable[str]) -> list[tuple[str, int]]:
    """Top ten words in `words`."""
    word_counts = defaultdict(int)

    for word in words:
        word_counts[word] += 1

    return sorted(word_counts.items(), key=lambda v: -v[1])[:10]


T = TypeVar("T")


def _pairwise(itr: abc.Iterable[T]) -> abc.Iterable[tuple[T, T]]:
    original, advanced = tee(itr)
    next(advanced)
    return zip(original, advanced)


def random_walk(words: abc.Iterable[str], num: int) -> str:
    """Random walk through `words`."""
    word_continuations = defaultdict(list)

    for word, after in _pairwise(words):
        word_continuations[word].append(after)

    res = [random.choice(list(word_continuations.keys()))]

    for _ in range(num):
        res.append(random.choice(word_continuations[res[-1]]))

    return " ".join(res)


def main() -> None:
    """Program entry point."""

    # parse arguments
    try:
        path_str = sys.argv[1]
    except IndexError:
        sys.exit(f"Usage: python {sys.argv[0]} PATH")

    path = Path(path_str)

    # count words
    print(f'\nWords in "{path}": {word_count(runeberg_words(path))}')

    # report top ten
    print("\nTop ten words:")
    for word, count in top_ten(runeberg_words(path)):
        print(f"\t{word}:\t{count}")

    # random walk
    print("\nRandom walk:")
    print(random_walk(runeberg_words(path), 100))


if __name__ == "__main__":
    main()
