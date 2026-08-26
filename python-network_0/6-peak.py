#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers using binary search"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # If mid element is less than the next element, peak is on the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
