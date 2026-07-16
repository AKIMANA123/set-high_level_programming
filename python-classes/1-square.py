#!/usr/bin/python3
"""Square class with private size attribute"""


class Square:
    """Defines a square with a private size attribute"""

    def __init__(self, size):
        """Initialize the square with a size

        Args:
            size: The size of the square
        """
        self.__size = size
