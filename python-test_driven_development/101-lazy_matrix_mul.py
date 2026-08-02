#!/usr/bin/python3
"""Function to multiply two matrices using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy

    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        New matrix as a numpy array
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    # Check if all elements are integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if all rows have the same size
    row_length_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_length_a:
            raise ValueError("setting an array element with a sequence.")

    row_length_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_length_b:
            raise ValueError("setting an array element with a sequence.")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Use NumPy to multiply matrices
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)
    result = np.matmul(arr_a, arr_b)

    return result
