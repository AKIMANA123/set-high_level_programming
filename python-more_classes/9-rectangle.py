#!/usr/bin/python3
"""Rectangle class with width, height, area, perimeter, repr, del, count,
print_symbol, comparison, and square class method
"""


class Rectangle:
    """Defines a rectangle with instance counting, custom symbol,
    comparison, and square creation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height

        Args:
            width: The width of the rectangle (default 0)
            height: The height of the rectangle (default 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle (2 * (width + height))
            Returns 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol

        Returns:
            A string of the rectangle drawn with print_symbol
            Empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for _ in range(self.__height):
            result.append(str(self.print_symbol) * self.__width)
        return "\n".join(result)

    def __repr__(self):
        """Return a string representation of the rectangle for recreation

        Returns:
            A string that can be used with eval() to recreate the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area

        Args:
            rect_1: First Rectangle instance
            rect_2: Second Rectangle instance

        Returns:
            The rectangle with the larger area
            rect_1 if both have the same area

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance with equal width and height

        Args:
            size: The size of the square (default 0)

        Returns:
            A new Rectangle instance where width == height == size
        """
        return cls(size, size)
