"""
https://leetcode.com/problems/rotate-image/
LC048 Roate Image
Medium

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Do not return anything, modify matrix in-place instead.
"""

from typing import *


class Solution_A:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Hashmap, need additinal space to memory the matrix
        """
        n = len(matrix)
        if matrix[0]:
            hmp = {}
            for row in range(n):
                for col in range(n):
                    new_row, new_col = col, n - row - 1 # reverse set up the col and row
                    hmp[(new_row, new_col)] = matrix[row][col]
            for row in range(n):
                for col in range(n):
                    matrix[row][col] = hmp[(row, col)]

class Solution_B:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Direct change in-place, with circiles shrinking to the center

        The iteration goes through each square, [row,col] represent first row of the circle, except for the very last one
        1 2 3 4 5 6 |
        | 7 8 9 0 | |
        | | 1 2 | | |
        | | | * | | |
        | | | - | | |
        | | - - - | |
        | - - - - - |
        From each [row,col], 3 other [x, y] are located by row and col, and rotate all 4 points at the same time

        If odd number matrix, center will not be iterated, as it won't move at all
        """

        N = len(matrix)
        for row in range(N // 2):  # row change,只走前半行(用//去除奇数中心)
            for col in range(row, N - row - 1): # col change, 从row number开始,斜切入中心,-1用于去掉对称位
                A = matrix[row][col]
                B = matrix[col][N - row - 1]
                C = matrix[N - row - 1][N - col - 1]
                D = matrix[N - col - 1][row]

                matrix[col][N - row - 1]         = A
                matrix[N - row - 1][N - col - 1] = B
                matrix[N - col - 1][row]         = C
                matrix[row][col]                 = D


if __name__ == "__main__":
    testCase = Solution_B()

    edge_0 = [[]]
    testCase.rotate(edge_0)
    assert edge_0 == [[]], "Edge 0"

    edge_1 = [[1]]
    testCase.rotate(edge_1)
    assert edge_1 == [[1]], "Edge 1"

    sample_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    testCase.rotate(sample_1)
    assert sample_1 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ], "Example 1"

    sample_2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    testCase.rotate(sample_2)
    assert sample_2 == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ], "Example 2"

    print("All passed")
