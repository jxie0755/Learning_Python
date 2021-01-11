"""
https://leetcode.com/discuss/interview-question/422725/google-phone-screen-min-flips-to-set-all-zeros
Given a binary 2D grid (each element can either be a 1 or a 0).
You have the ability to choose any element and flip its value.
The only condition is that when you choose to flip any element at index (r, c), the 4 neighbors of that element also get flipped.
Find the minimum number of flips that you need to do in order to set all the elements in the matrix equal to 0. If it's not possible, return -1.
"""

from typing import *


def flipMatrix(matrix: List[List[int]], coor: Tuple[int, int]) -> None:
    """
    This is to apply one flip to a matrix
    matrix size must be at least > 1 * 1
    coor must be in the matrix, form: (row index, column index)
    """
    width = len(matrix[0])
    height = len(matrix)

    row_index = coor[0]
    column_index = coor[1]

    up = (row_index - 1, column_index)
    down = (row_index + 1, column_index)
    left = (row_index, column_index - 1)
    right = (row_index, column_index + 1)

    for point in [coor, up, down, left, right]:
        x, y = point[0], point[1]
        if 0 <= x < height and 0 <= y < width:
            matrix[x][y] = int(not matrix[x][y])


def flipMatrixAll(matrix: List[List[int]]) -> None:
    """Flip every point in the matrix following the flixMatrix rule"""
    width = len(matrix[0])
    height = len(matrix)

    for x in range(height):
        for y in range(width):
            flipMatrix(matrix, (x, y))


def printGrid(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(row)
    print()

if __name__ == "__main__":
    grid_1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]

    # Test 1, flip center, then the rest value at 1
    # flipMatrix(grid_1, (1,1))
    # printGrid(grid_1)
    # >>>
    # [0, 1, 0]
    # [1, 0, 1]
    # [0, 1, 0]

    # flipMatrix(grid_1, (0, 1))
    # flipMatrix(grid_1, (1, 0))
    # flipMatrix(grid_1, (1, 2))
    # flipMatrix(grid_1, (2, 1))
    # printGrid(grid_1)
    # >>>
    # [0, 0, 0]
    # [0, 0, 0]
    # [0, 0, 0]

    # Test 2, flip all points
    flipMatrixAll(grid_1)
    printGrid(grid_1)
    # >>>
    # [1, 0, 1]
    # [0, 0, 0]
    # [1, 0, 1]
