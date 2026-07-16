#!/usr/bin/python3
"""Square class with private size attribute and validation"""


class Square:
    """Defines a square with a private size attribute and validation"""

    def __init__(self, size=0):
        """Initialize the square with a size

        Args:
            size: The size of the square (default 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
