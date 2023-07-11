#!/usr/bin/python3
"""
Define a pascal_triangle function
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of
    integers representing the Pascal’s
    triangle of n
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        row.append(1)
        result.append(row)
    return result
