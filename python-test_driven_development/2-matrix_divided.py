#!/usr/bin/python3
"""Function to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div

    Args:
        matrix: List of lists of integers or floats
        div: Number to divide by (int or float)

    Returns:
        New matrix with elements divided by div, rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check each row is a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check each element is int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
