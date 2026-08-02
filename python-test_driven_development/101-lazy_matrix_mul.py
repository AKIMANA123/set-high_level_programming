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
    # Check for ragged rows (to avoid object arrays)
    if isinstance(m_a, list) and m_a:
        row_length_a = len(m_a[0])
        for row in m_a:
            if len(row) != row_length_a:
                raise ValueError(
                    "setting an array element with a sequence.")

    if isinstance(m_b, list) and m_b:
        row_length_b = len(m_b[0])
        for row in m_b:
            if len(row) != row_length_b:
                raise ValueError(
                    "setting an array element with a sequence.")

    # Let NumPy handle everything else
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)
    result = np.matmul(arr_a, arr_b)
    return result
