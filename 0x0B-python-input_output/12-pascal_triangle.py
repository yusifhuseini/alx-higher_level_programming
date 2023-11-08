#!/usr/bin/python3

"""
A modules: Defines a function that builds pascal triangle
"""


def pascal_triangle(n):
    """
    Builds pascal triangle

    Args:
        n (int): size of the triangle

    Returns
        (list): list of lists
    """
    triangle = []
    if n > 0:
        for row in range(n):
            if row == 0:
                triangle.append([1])
            elif row == 1:
                triangle.append([1, 1])
            else:
                column = []
                r = row - 1
                for i in range(len(triangle[r])):
                    if i != len(triangle[r]) - 1:
                        column.append(triangle[r][i] + triangle[r][i + 1])
                column = [1] + column + [1]
                triangle.append(column)
    return triangle
