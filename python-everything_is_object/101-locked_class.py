#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """Prevents dynamic attribute creation except for first_name"""
    __slots__ = ["first_name"]
