#!/usr/bin/python3
"""Function to convert JSON string to object"""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string"""
    return json.loads(my_str)
