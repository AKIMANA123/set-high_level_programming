#!/usr/bin/python3
"""Function to check if object is an instance of a class that inherited from"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
