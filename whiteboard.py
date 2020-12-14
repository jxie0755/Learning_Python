"""
https://leetcode.com/problems/minimum-path-sum/
P064 Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass




if __name__ == "__main__":
    testCase = Solution()

    E1 = [[]]
    assert testCase.minPathSum(E1) == 0, "Edge 1"

    E2 = [[1]]
    assert testCase.minPathSum(E2) == 1, "Edge 2"

    E3 = [[1, 1]]
    assert testCase.minPathSum(E3) == 2, "Edge 3"

    E4 = [[1], [1]]
    assert testCase.minPathSum(E4) == 2, "Edge 4"

    S1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    assert testCase.minPathSum(S1) == 7, "Example 1"
    print("all passed")

