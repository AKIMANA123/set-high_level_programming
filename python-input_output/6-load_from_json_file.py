#!/usr/bin/python3
"""Function to load object from JSON file"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
