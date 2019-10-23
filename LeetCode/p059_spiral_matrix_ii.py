"""
https://leetcode.com/problems/spiral-matrix-ii/
P059 Spiral Matrix II
Medium

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""

from typing import *

class Solution_A:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Generate by keep changing the row and col in clock sequence
        """
        val = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        top, bot, left, right = 0, n - 1, 0, n - 1
        while top <= bot and left <= right:
            for a in range(left, right + 1):
                matrix[top][a] = val
                val += 1
            top += 1
            for b in range(top, bot + 1):
                matrix[b][right] = val
                val += 1
            right -= 1
            for c in range(right, left - 1, -1):
                matrix[bot][c] = val
                val += 1
            bot -= 1
            for d in range(bot, top - 1, -1):
                matrix[d][left] = val
                val += 1
            left += 1

        return matrix


if __name__ == "__main__":
    testMethod = Solution_A().generateMatrix
    assert testMethod(1) == [[1]], "Edge 1"

    assert testMethod(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ], "Example 1"

    print("all passed")
