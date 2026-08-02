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
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)
    result = np.matmul(arr_a, arr_b)
    return result
