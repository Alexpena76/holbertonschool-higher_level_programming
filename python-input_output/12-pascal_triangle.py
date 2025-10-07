#!/usr/bin/python3
"""Module that provides a function to generate Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n: number of rows in Pascal's triangle

    Returns:
        List of lists representing Pascal's triangle, or empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        # Start each row with 1
        row = [1]

        # Calculate middle values
        for j in range(1, i):
            # Each element is sum of two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with 1
        row.append(1)

        triangle.append(row)

    return triangle
