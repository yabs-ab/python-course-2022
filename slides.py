###############################################################################
#                                                                             #
#                                                                             #
#                                                                             #
#                    ____        _   _                                        #
#                   |  _ \ _   _| |_| |__   ___  _ __                         #
#                   | |_) | | | | __| '_ \ / _ \| '_ \                        #
#                   |  __/| |_| | |_| | | | (_) | | | |                       #
#                   |_|    \__, |\__|_| |_|\___/|_| |_|                       #
#                          |___/                                              #
#                                Fundamentals                                 #
#                                                                             #
#                                                                             #
#                       Peter Román <peter.roman@yabs.se>                     #
#                            Young Aces by Sylog                              #
#                                                                             #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################



# Who am I?

#      - Software development and architecture consultant
#      - Mentoring and teaching
#      - Mainly Python, C, C++ and JavaScript
#      - Some Java, Tcl, bash, ...




# AGENDA

#      1. What is Python?
#      2. What tools do I need?
#      3. How do I write it?
#           - Syntax
#           - Guidelines




# APPROACH

#      - Almost everything
#      - In depth
#      - In short amount of time



# WHAT IS PYTHON

#      - General purpose
#      - Multi-paradigm
#      - Powerful
#      - Approachable
#      - "Batteries included"
#      - Slow...
#      - Python/CPython/PyPy
#      - Popular




# https://madnight.github.io/githut/#/pull_requests/2021/4
# https://pypl.github.io/PYPL.html




# Writing, running, linting...

print("Hello world!")




# $ python -m venv venv
# $ . venv/bin/activate
# $ pip install ipython black pylint mypy
# $ pip freeze > requirements-dev.txt




# Objects have id, type and value

a = 2 + 2
b = a




#        a = 4
#                             _  _
#                            | || |
#                            | || |_
#            +-------------  |__   _|
#            |                  |_|
#        +---+---+
#        |   a   |
#        +-------+




#        b = a
#                             _  _
#                            | || |
#                            | || |_
#            +-------------  |__   _|  -------------+
#            |                  |_|                 |
#        +---+---+                              +---+---+
#        |   a   |                              |   b   |
#        +-------+                              +-------+




# Values are created by expressions

a = 1024
b = 2 ** 10




#         +-----+                                 +-----+
#   +-----+  a  |                                 |  b  +--------+
#   |     +-----+                                 +-----+        |
#   |    _  ___ ____  _  _                 _  ___ ____  _  _     |
#   +-- / |/ _ \___ \| || |               / |/ _ \___ \| || |  --+
#       | | | | |__) | || |_              | | | | |__) | || |_
#       | | |_| / __/|__   _|             | | |_| / __/|__   _|
#       |_|\___/_____|  |_|               |_|\___/_____|  |_|




a = 8
b = 2 ** 3




# ADVICE

#     Never use "is".




#                  ... except when comparing to singletons!




# https://docs.python.org/3/reference/datamodel.html




# Conditionals

# if, elif, else, and, or, not




# Built-in types!

# https://docs.python.org/3/library/stdtypes.html




# int and float




# str and bytes




#     0     1     2     3     4
#     |     |     |     |     |

#    "h     a     l     l     å"

#     |     |     |     |     |
#    -5    -4    -3    -2    -1




# surrogate pairs

s = "🙃"




# diacritic marks

t = "a\U00000301"




# format

# https://docs.python.org/3/library/string.html#formatspec




# list

numbers = [1, 2, 3, 8, 112]




# Sorting, cmp or key




# tuple

hellos = ("hello", "hi", "hey", "howdy")




# INTERLUDE -- tuple vs list

# Technical differences
#     - tuples are faster
#     - tuples are immutable
#     - tuples are hashable




# INTERLUDE -- tuple vs list

# Cultural differences
#     - Use tuples for heterogeneous collections
#     - Use lists for homogeneous collections
#     - Use tuples where position matters




# set (and frozenset)

fruits = {"apple", "banana", "pear", "pear"}




# dict

heights = {"Burj Khalifa":  829.8,
           "Coast Redwood": 115.61,
           "Robert Wadlow": 2.72}




# Functions: definition

def fun(arg):
    """Return a message involving `arg`
    """
    return f"You passed in {arg}"




# Default arguments

def fun(one, two="Second", three="Third"):
    print(one, two, three)




# Variadic functions

def fun(one, *args):
    print(one, args)




# Keyword arguments

def fun(**kwargs):
    print(kwargs)




# Can of course be combined

def fun(*args, **kwargs):
    """You can pass me anything!
    """
    print(args, kwargs)




# Functions are closures!

def fun(something):
    def closure():
        return something

    return closure




# Pop-Quiz!
# What does this print out?

def append_twice(seq, elem):
    seq = seq + [elem, elem]


a_list = []
append_twice(a_list, "Hi!")
print(a_list)




# What about this?

def append_twice(seq, elem):
    seq.append(elem)
    seq.append(elem)


a_list = []
append_twice(a_list, "Hi!")
print(a_list)




def twice_appended(seq, elem):
    return seq + [elem, elem]


a_list = []
a_list = twice_appended(a_list, "Hi!")
print(a_list)




# Loops!

colors = ["red", "green", "blue", "yellow"]




# Loop backwards?

colors = ["red", "green", "blue", "yellow"]

for i in range(len(colors) - 1, -1, -1):
    print(colors[i])




# With index?

colors = ["red", "green", "blue", "yellow"]

for i, color in enumerate(colors):
    print(i, "->", color)




# List over two sequences (or more)?

names = ["Burj Khalifa", "Robert Wadlow", "Coast Redwood"]
heights = [829.8, 2.72, 115.61]

for name, height in zip(names, heights):
    print(name, "->", height)




for i in range(5):
    print(i)
else:
    print("Else?")




import time

while True:
    print("Looping...")
    time.sleep(1)




# Exercises!




# Exceptions!

try:
    something_that_can_raise()
except:
    pass
else:
    print("No exception raised!")
finally:
    print("This is always run.")




# Exceptions are used for everything in Python

try:
    print(undefined_name)
except Exception as e:
    print(type(e), "--", e)




# INTERLUDE -- Duck Typing

#            ..---..
#          .'  _    `.
#      __..'  (o)    :
#     `..__          ;
#          `.       /
#            ;      `..---...___
#          .'                   `~-. .-')
#         .                         ' _.'
#        :                           :
#        \                           '
#         +                         J
#          `._                   _.'
#             `~--....___...---~'




# "If it looks like a duck, swims like a duck, and quacks like a duck,
# then it probably is a duck"

def recursive_sum(numbers):
    if type(numbers) == int:
        return numbers

    if type(numbers) in (list, tuple):
        result = 0

        for n in numbers:
            result += recursive_sum(n)

        return result




# Generators!

def one_to_three_gen():
    yield 1
    yield 2
    yield 3




# Generator expressions!




# Let us look at a short example...




def recursive_sum(numbers):
    try:
        return sum(recursive_sum(n) for n in numbers)
    except TypeError:
        return numbers




# Opening files!




# Final exercise for the day!

#      runeberg.py




# End of day 1!




# Decorators!

def decorator(func):
    def newfunc():
        print("before!")
        func()
        print("after!")

    return newfunc

def a_function():
    print("a_function()")

a_function = decorator(a_function)




# Classes!

class Color:
    def __init__(self, r, g, b):
        """The constructor."""
        self.r = r
        self.g = g
        self.b = b

c = Color(1, 2, 3)




# ADVICE
#         Don't write getters and setters!




# But what if...

class Color:
    def __init__(self, r, g, b):
        """The constructor."""
        self._r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        """The color red."""
        return self._r

    @r.setter
    def r(self, value):
        self._r = value




# Sub-classes!
class Red(Color):
    def __init__(self, r):
        super().__init__(r, 0, 0)

r = Red(3)




# What about interfaces?




# Simple: just raise exceptions!

class AbstractColor:
    def red(self):
        raise NotImplementedError('red is not implemented!')

    # etc...




# But there are other, more complicated ways

import abc


class AbstractColor(abc.ABC):
    @abc.abstractmethod
    def red():
        pass

ac = AbstractColor()




# __repr__ and __str__

class SomeClass:
    def __init__(self, some_number):
        self.some_number = some_number

    def __repr__(self):
        return f"SomeClass({self.some_number})"

    def __str__(self):
        return f"Holder of: \n\t{self.some_number}"




# isinstance, issubclass




# ADVICE

#       1. Always-always-always implement __repr__!
#       2. Implement __str__ if you have a need for it.




# ADVICE

#       1. Keep object hierarchies flat!
#       2. Prefer built-in collections!




# What about destructors?




class MyContext:
    def __enter__(self):
        print("enter")

    def __exit__(self, *args):
        print("exit", args)



# Exercise time!




# dataclasses and contextlib




# Concurrent programming in Python!




# Paradigms

#  - Threads
#  - Processes
#  - Select/poll based concurrency (Reactor pattern)
#  - ... ?




import threading



# Global Interpreter Lock (GIL)

#            I/O            I/O      I/O      I/O
#             |              |        |        |
#             |              |        |        |
# ... - run ->|              |- run ->|        |- run - ...
#             |              |        |        |
#             |              |        |        |
#             |              |        |        |
#             |---- run ---->|        |- run ->|
#             |              |        |        |
#             |              |        |        |




import multiprocessing




from concurrent import futures




import asyncio

# https://docs.python.org/3/library/asyncio-api-index.html




# Exercise!

#         chat.py




# THE MOST FUNDAMENTAL ADVICE

#       1. Use the REPL!
#       2. Make your code play nice with the REPL!
#       3. Use the right tools (pylint, black, ...)
#       4. Use comprehensions, generators, iteratators
#       5. Use dataclasses
#       6. Use asyncio for concurrency
