#!/usr/bin/python3
"""Square class with private size, position, getters, setters, area, print"""


class Square:
    """Defines a square with size, position, area, and printing"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position

        Args:
            size: The size of the square (default 0)
            position: The position of the square (default (0, 0))

        Raises:
            TypeError: If size is not an integer or position is invalid
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character with position offset

        If size is 0, print an empty line
        position[0] is the number of spaces before each line
        position[1] is the number of empty lines before the square
        """
        if self.__size == 0:
            print()
            return

        # Print empty lines based on position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square with position[0] spaces before each row
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
