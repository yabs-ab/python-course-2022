"""Some basic exercises!
"""

from __future__ import annotations
from collections import abc
from itertools import islice
import re


def ends_match(strings: abc.Iterable[str]) -> int:
    """Count strings in `strings` where ends match.

    Counts the number of strings in `strings` with length 2 or more
    where the first character is the same as the last.

    >>> ends_match(['this', 'is', 'a', 'test'])
    1
    """
    return sum(1 for s in strings if len(s) > 1 and s[0] == s[-1])


def pluralize(num: int, singular: str, plural: str | None = None) -> str:
    """Return pluralization of `singular`.

    Uses `plural` if provided, otherwise returns `singular` with 's' appended.

    >>> pluralize(1, 'apple')
    'apple'

    >>> pluralize(2, 'apple')
    'apples'

    >>> pluralize(4, 'goose', 'geese')
    'geese'
    """
    return singular if num == 1 else plural or singular + "s"


def pig_latin(text: str) -> str:
    """Translate `text` to pig latin.

    Pig latin is constructed by moving the first letter of every word
    to the end and appending 'ay', i.e.

    >>> pig_latin('pigs go oink')
    'igspay ogay inkoay'
    """
    return " ".join(word[1:] + word[0] + "ay" for word in text.split())


def is_palindrome(text: str) -> bool:
    """Check whether `text` is a palindrome.

    This function ignores whitespace and capitalization.

    >>> is_palindrome('Ni talar bra latin')
    True

    >>> is_palindrome('Rabarberbarbar')
    False
    """
    
    return all(a == b for a, b in islice(zip(text, reversed(text)), len(text) // 2))


def sorted_by_length_and_alphabetically(strings: list[str]) -> list[str]:
    """Return specially sorted copy of `strings`.

    The longest strings first and within a length alphabetically.

    >>> sorted_by_length_and_alphabetically(
    ...     ['this', 'is', 'a', 'weird', 'sort', 'order'])
    ['order', 'weird', 'sort', 'this', 'is', 'a']
    """
    return sorted(strings, key=lambda x: (-len(x), x))



def highest_compatible_version(
    supported_versions: abc.Iterable[str], client_versions: abc.Iterable[str]
) -> str | None:
    """Return highest matching version string ('X.Y.Z') in collections.

    >>> highest_compatible_version(['1.1.0', '2.0.0'], ['1.1.0', '2.0.0', '2.0.1'])
    '2.0.0'

    >>> highest_compatible_version(['10.1.0', '2.0.0'], ['10.1.0', '2.0.0', '2.0.1'])
    '10.1.0'

    >>> highest_compatible_version(['1.1.0', '2.0.0'], ['2.1.0', '2.2.1'])
    """
    try:
        return max((v for v in supported_versions if v in client_versions),
                   key=lambda x: tuple(int(i) for i in x.split(".")))
    except ValueError:
        return None 
    

def parse_index_lines(lines: abc.Iterable[str]) -> list[tuple[str, str]]:
    """Parse sequence of `lines` of a hypothetical index file.

    Each line follows the format

        <name>|<description>|

    and this function returns a list of (name, description)
    tuples. Lines that start with a '#' are comments and should be
    ignored.

    >>> parse_index_lines(
    ...    ['# This is a comment and should be ignored!',
    ...     'name 1|description 1|',
    ...     'name 2|description 2|'])
    [('name 1', 'description 1'), ('name 2', 'description 2')]
    """

def strip_xml_tags(text: str) -> str:
    """Return a version of `text` stripped of xml tags.

    >>> strip_xml_tags('Vi kan <a href="python.org">Python</a>!')
    'Vi kan Python!'
    """
    return re.sub(r"<.*?>", "", text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
