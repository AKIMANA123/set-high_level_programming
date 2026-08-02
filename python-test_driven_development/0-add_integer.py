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
        OverflowError: If a or b is too large to convert to int
        ValueError: If a or b is NaN (Not a Number)
    """
    # Check if a is NaN
    if isinstance(a, float) and (a != a):
        raise ValueError("cannot convert float NaN to integer")

    # Check if b is NaN
    if isinstance(b, float) and (b != b):
        raise ValueError("cannot convert float NaN to integer")

    # Check if a is valid type
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is valid type
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except (OverflowError, ValueError):
        raise ValueError("cannot convert float NaN to integer")
