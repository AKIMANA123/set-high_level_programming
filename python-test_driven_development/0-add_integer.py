#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a: First integer (must be int or float)
        b: Second integer (must be int or float, default 98)

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
        OverflowError: If a or b is a float that overflows when cast to int
        ValueError: If a or b is NaN (Not a Number)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("cannot convert float infinity to integer")
    except ValueError:
        raise ValueError("cannot convert float NaN to integer")
