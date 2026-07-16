#!/usr/bin/python3
"""Square class with private size attribute, getter, and setter"""


class Square:
    """Defines a square with size getter and setter"""

    def __init__(self, size=0):
        """Initialize the square with a size

        Args:
            size: The size of the square (default 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size
