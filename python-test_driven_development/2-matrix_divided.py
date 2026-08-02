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

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = round(element / div, 2)
            # Convert -0.0 to 0.0
            if result == 0:
                result = 0.0
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
