#!/usr/bin/python3
"""Student class with to_json and reload_from_json methods"""


class Student:
    """Student class with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Args:
            attrs: List of attribute names to retrieve (optional)

        Returns:
            Dictionary with specified attributes or all attributes
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json: Dictionary with attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
