#!/usr/bin/python3
""" Pascal triangle module
"""


def pascal_triangle(n):
    """ This generates a pascal triangle

    Args:
        n (int): the triangle size

    Returns:
        List: List of lists
    """

    if n <= 0:
        return []

    # initialize the triangle with the start 1
    triangle = [[1]]
    # loop n times to set rows for the triangle
    for i in range(1, n):
        # always set a new row with init 1
        row = [1]
        # loop through each row to implement the pascal triangle logic
        for j in range(1, i):
            # try the logic and continue if there is any index error
            try:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            except Exception as e:
                continue
                # print(row)
        # always add 1 at the end of each row before adding to triangle
        row.append(1)
        triangle.append(row)

    return triangle
