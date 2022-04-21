"""Exercises with classes!"""

from __future__ import annotations
from collections import abc
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    @property
    def area(self) -> float:
        """Area of shape."""
        raise NotImplementedError


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

    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, self.__class__)
            and self.width == other.width
            and self.height == other.height
        )

    @property
    def area(self) -> float:
        return self.width * self.height


class KeyBasedDefaultDict(dict[abc.Hashable, Any]):
    """A version of `collections.defaultdict` with key based factory.

    The factory function takes the key as a parameter, i.e.

    >>> d = KeyBasedDefaultDict({1: 1},
    ...                         default=lambda key: key - 1)
    >>> d[1], d[2]
    (1, 1)
    """

    def __init__(
        self,
        *args: list[Any],
        default: abc.Callable[[abc.Hashable], Any] | None = None,
        **kwargs: dict[str, Any],
    ) -> None:
        super().__init__(*args, **kwargs)
        self._factory = default

    def __missing__(self, key: abc.Hashable) -> Any:
        if self._factory is None:
            return None

        return self._factory(key)


class Timer:
    """Timer context.

    >>> timer = Timer()
    >>> with timer:
    ...     time.sleep(0.3)
    >>> 0.2 < timer.time < 0.4
    True
    """

    def __init__(self) -> None:
        self.time: float | None = None

    def __enter__(self) -> None:
        self.time = time.time()

    def __exit__(self, *_: Any) -> None:
        assert self.time is not None
        self.time = time.time() - self.time


def serve(html: str, port: int) -> NoReturn:
    """Serve `html` on http://localhost:`port`/

    Server should respond with code 200 and add Content-Type and
    Content-Length HTTP headers!

    Hint: look at the http.server module in the standard library.
    """
    html_msg = html.encode()

    class MyHandler(BaseHTTPRequestHandler):
        """My custom request handler."""

        def do_GET(self) -> None:  # pylint: disable=invalid-name
            """Handle GET."""
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(html_msg)))
            self.end_headers()
            self.wfile.write(html_msg)

    with HTTPServer(("localhost", port), MyHandler) as server:
        server.serve_forever()

    sys.exit(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
