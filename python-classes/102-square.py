#!/usr/bin/python3
"""Square class with size validation, area, and comparison methods"""


class Square:
    """Defines a square with size, area, and comparison methods"""

    def __init__(self, size=0):
        """Initialize the square with a size

        Args:
            size: The size of the square (default 0)

        Raises:
            TypeError: If size is not a number (float or integer)
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
            TypeError: If value is not a number (float or integer)
            ValueError: If value is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares are equal (by area)

        Returns:
            True if areas are equal, False otherwise
        """
        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal (by area)

        Returns:
            True if areas are not equal, False otherwise
        """
        if not isinstance(other, Square):
            return True
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square is greater than another (by area)

        Returns:
            True if this area is greater, False otherwise

        Raises:
            TypeError: If other is not a Square
        """
        if not isinstance(other, Square):
            raise TypeError("Comparison with non-Square object")
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another (by area)

        Returns:
            True if this area is greater or equal, False otherwise

        Raises:
            TypeError: If other is not a Square
        """
        if not isinstance(other, Square):
            raise TypeError("Comparison with non-Square object")
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if this square is less than another (by area)

        Returns:
            True if this area is less, False otherwise

        Raises:
            TypeError: If other is not a Square
        """
        if not isinstance(other, Square):
            raise TypeError("Comparison with non-Square object")
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another (by area)

        Returns:
            True if this area is less or equal, False otherwise

        Raises:
            TypeError: If other is not a Square
        """
        if not isinstance(other, Square):
            raise TypeError("Comparison with non-Square object")
        return self.area() <= other.area()
