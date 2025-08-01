# Python Game Lib's random tools.

# (c) JoBe, 2025


import os
import time
import hashlib
import sys


__all__ = [
    "randint",
    "randbool",
    "randfloat",
    "randmin",
    "randmax",
]


def __randint(*, min: int, max: int) -> int:
    urandom_bytes = os.urandom(16)
    time_bytes = str(time.time_ns()).encode()
    time_hash = hashlib.sha256(time_bytes).digest()
    combined = hashlib.sha256(urandom_bytes + time_hash).digest()
    rand_int = int.from_bytes(combined, 'big')
    range_size = max - min + 1
    return min + (rand_int % range_size)


def randint(min: int, max: int, /) -> int:
    """
    Return a random integer of range `[min, max]` (inclusive both end points)
    """

    return __randint(min=min, max=max)


def randmin(min: int, /) -> int:
    """
    Return a random integer of range `[min, inf]` (inclusive both end points)
    """

    return __randint(min=min, max=sys.maxsize)


def randmax(max: int, /) -> int:
    """
    Return a random integer of range `[-inf, max]` (inclusive both end points)
    """

    return __randint(min=-sys.maxsize, max=max)


def randbool() -> bool:
    """
    Return either `True` or `False`,
    based on a random number being even.
    
    The odds for either case are 50%.
    """

    return __randint(min=-sys.maxsize, max=sys.maxsize) % 2 == 0


def randfloat() -> float:
    """
    Returns a random float in the range of 0 to 1
    """

    return __randint(min=0, max=2**53-1) / (2**53)

del __randint
