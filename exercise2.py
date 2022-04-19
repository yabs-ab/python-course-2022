"""Exercises with classes!"""

from __future__ import annotations
from collections import abc
import time
from typing import Any, NoReturn


class AbstractShape:
    """AbstractShape base class.

    Implement this class with an abstract property `area`

    >>> try:
    ...     AbstractShape().area
    ... except NotImplementedError:
    ...     print('Success!')
    Success!

    It should, of course, define `__repr__`

    >>> repr(AbstractShape())
    'AbstractShape()'
    """


class Rectangle(AbstractShape):
    """A rectangle.

    Define this subclass of `AbstractShape` that implements the `area`
    property.

    >>> Rectangle(4, 2).area
    8

    It should also define properties for `width` and `height`

    >>> r = Rectangle(48, 22)
    >>> r.width, r.height
    (48, 22)

    Also, make rectangles comparable with `==`

    >>> Rectangle(2, 4) == Rectangle(2, 4)
    True

    >>> Rectangle(2, 4) == Rectangle(2.1, 4)
    False

    And, its `__repr__` should `eval` to an equal object!

    >>> r = Rectangle(7, 21)
    >>> eval(repr(r)) == r
    True
    """


class KeyBasedDefaultDict(dict[abc.Hashable, Any]):
    """A version of `collections.defaultdict` with key based factory.

    The factory function takes the key as a parameter, i.e.

    >>> d = KeyBasedDefaultDict({1: 1},
    ...                         default=lambda key: key - 1)
    >>> d[1], d[2]
    (1, 1)
    """


class Timer:
    """Timer context.

    >>> timer = Timer()
    >>> with timer:
    ...     time.sleep(0.3)
    >>> 0.2 < timer.time < 0.4
    True
    """


def serve(html: str, port: int) -> NoReturn:
    """Serve `html` on http://localhost:`port`/

    Server should respond with code 200 and add Content-Type and
    Content-Length HTTP headers!

    Hint: look at the http.server module in the standard library.
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
