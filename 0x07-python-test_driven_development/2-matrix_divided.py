#!/usr/bin/python3
"""Define a function matrix_divided"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a
    given divisor.
    Args:
        matrix (list): A list of lists of
        integers or floats.
        div (int or float): The divisor.
    Returns:
        list: A new matrix with the result
        of the division.
    """
    if (
        not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all((isinstance(e, int)
                    or isinstance(e, float))
                   for e in [n for row in matrix for n in row])
    ):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
