#!/usr/bin/python3
"""MyInt class that inherits from int with inverted == and !="""


class MyInt(int):
    """MyInt class with inverted == and != operators"""

    def __eq__(self, other):
        """Invert == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != operator"""
        return super().__eq__(other)
