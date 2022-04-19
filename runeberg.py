"""Project Runeberg parsing exercise."""

from __future__ import annotations
from collections import abc
from pathlib import Path
import sys


def runeberg_words(path: Path) -> abc.Iterable[str]:
    """Generate words from the "Project Runeberg" text in `path`."""


def main() -> None:
    """Program entry point."""

    # parse arguments
    try:
        path_str = sys.argv[1]
    except IndexError:
        sys.exit(f"Usage: python {sys.argv[0]} PATH")

    path = Path(path_str)

    # count words
    word_count = sum(1 for _ in runeberg_words(path))
    print(f'Words in "{path}": {word_count}')


if __name__ == "__main__":
    main()
