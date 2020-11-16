"""
https://leetcode.com/problems/spiral-matrix-ii/
P059 Spiral Matrix II
Medium

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""

from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    testCase = Solution()
    assert testCase.generateMatrix(1) == [[1]], "Edge 1"

    assert testCase.generateMatrix(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ], "Example 1"

    assert testCase.generateMatrix(2) == [
        [1, 2],
        [4, 3]
    ], "Extra 1"

    assert testCase.generateMatrix(4) == [
        [1,  2,  3,  4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9,  8,  7]
    ], "Extra 2"

    print("all passed")
