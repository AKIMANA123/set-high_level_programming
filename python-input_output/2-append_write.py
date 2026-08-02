#!/usr/bin/python3
"""Function to append a string to a text file"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return
    number of chars added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
