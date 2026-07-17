#!/usr/bin/python3
"""Function to add attribute to an object if possible"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible

    Args:
        obj: The object to add attribute to
        name: The name of the attribute
        value: The value of the attribute

    Raises:
        TypeError: If the object can't have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
