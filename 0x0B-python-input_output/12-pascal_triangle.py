#!/usr/bin/python3
""" Pascal's Triangle. """


def pascal_triangle(n):
    """
    Description:
         function that represent the Pascal's triangle with list of integers.
    Arg: n: n number of list.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(pascal[x-1][y-1] + pascal[x-1][y])
        row.append(1)
        pascal.append(row)
    return pascal
