#!/usr/bin/python3
"""Function to convert class object to dictionary for JSON serialization"""


def class_to_json(obj):
    """Return dictionary description with simple data structure for JSON"""
    return obj.__dict__
