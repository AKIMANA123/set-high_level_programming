#!/usr/bin/python3
"""MagicClass that does exactly the same as the given bytecode"""

import math


class MagicClass:
    """Class that replicates the bytecode behavior"""

    def __init__(self, radius=0):
        """Initialize the MagicClass with radius validation"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle"""
        return 2 * math.pi * self.__radius
