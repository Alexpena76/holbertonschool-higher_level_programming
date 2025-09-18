#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It handles validation of matrix structure, divisor validation, and zero division.
The function ensures the matrix is properly formatted and returns a new matrix.
All elements are divided and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists with same size and valid elements
    row_size = None
    for row in matrix:
        # Check if each row is a list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Check if row is empty
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        # Set row size from first row or check consistency
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all elements in row are numbers
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
