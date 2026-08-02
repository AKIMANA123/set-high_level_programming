#!/usr/bin/python3
"""Function to convert object to JSON string"""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
