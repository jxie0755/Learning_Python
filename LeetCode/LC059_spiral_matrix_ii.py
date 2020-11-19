"""
https://leetcode.com/problems/spiral-matrix-ii/
P059 Spiral Matrix II
Medium

Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
"""

from typing import *


class Solution_A:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Generate by keep changing the row and col in clock sequence
        Use the same while loop as in LC054
        """
        val = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        top_idx, bot_idx, left_idx, right_idx = 0, n - 1, 0, n - 1
        while val <= n * n:
            # always check val for each for loop
            # actually in this case, it can work without this check with perfect n*n
            # but won't work if m * n

            if val <= n * n:
                for a in range(left_idx, right_idx + 1):  # left -> right
                    matrix[top_idx][a] = val
                    val += 1
                top_idx += 1

            if val <= n * n:
                for b in range(top_idx, bot_idx + 1):  # top -> bot
                    matrix[b][right_idx] = val
                    val += 1
                right_idx -= 1

            if val <= n * n:
                for c in range(right_idx, left_idx - 1, -1):
                    matrix[bot_idx][c] = val
                    val += 1
                bot_idx -= 1

            if val <= n * n:
                for d in range(bot_idx, top_idx - 1, -1):
                    matrix[d][left_idx] = val
                    val += 1
                left_idx += 1

        return matrix


class Solution_A_rectangular:
    """
    This is an extended version for non-square situations
    """

    def generateMatrix_rect(self, m: int, n: int) -> List[List[int]]:
        """
        Version A additional
        To output any rectangular shape (non-perfect n^2 but m*n with width and hiegh)
        """
        val = 1
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        top_idx, bot_idx, left_idx, right_idx = 0, n - 1, 0, m - 1
        while val <= m * n:
            # always check val for each for loop
            # For this case, must check val, or else won't work

            if val <= m * n:
                for a in range(left_idx, right_idx + 1):  # left -> right
                    matrix[top_idx][a] = val
                    val += 1
                top_idx += 1

            if val <= m * n:
                for b in range(top_idx, bot_idx + 1):  # top -> bot
                    matrix[b][right_idx] = val
                    val += 1
                right_idx -= 1

            if val <= m * n:
                for c in range(right_idx, left_idx - 1, -1):
                    matrix[bot_idx][c] = val
                    val += 1
                bot_idx -= 1

            if val <= m * n:
                for d in range(bot_idx, top_idx - 1, -1):
                    matrix[d][left_idx] = val
                    val += 1
                left_idx += 1

        return matrix


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.generateMatrix(1) == [
        [1]
    ], "Edge 1"

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
