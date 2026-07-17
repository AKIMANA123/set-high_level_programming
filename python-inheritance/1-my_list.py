#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """MyList class with print_sorted method"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
