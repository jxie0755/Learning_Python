"""
https://leetcode.com/problems/minimum-path-sum/
P064 Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


from typing import *


class Solution_A:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        新建一个表, 不破坏原表
        然后在新表上遍历,根据左方和上方的邻居之中最小的较小的路径和来选择.
        """
        if not len(grid) or not len(grid[0]):
            return 0

        m, n = len(grid[0]), len(grid)
        min_to = [[1 for _ in range(m)] for _ in range(n)]

        for nn in range(n):
            for mm in range(m):
                if nn == 0 and mm == 0:
                    min_to[nn][mm] += 0
                elif nn == 0:
                    min_to[nn][mm] += min_to[nn][mm - 1]
                elif mm == 0:
                    min_to[nn][mm] += min_to[nn - 1][mm]
                else:
                    min_to[nn][mm] += min(min_to[nn][mm - 1], min_to[nn - 1][mm])

        return min_to[n - 1][m - 1]


class Solution_B:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        直接在原表上改动, 破坏原表, 但是速度更快
        """
        if not len(grid) or not len(grid[0]):
            return 0

        m = len(grid)
        n = len(grid[0])

        for mm in range(m):
            for nn in range(n):
                if mm == 0 and nn == 0:
                    grid[mm][nn] += 0
                elif mm == 0:
                    grid[mm][nn] += grid[mm][nn - 1]
                elif nn == 0:
                    grid[mm][nn] += grid[mm - 1][nn]
                else:
                    grid[mm][nn] += min(grid[mm][nn - 1], grid[mm - 1][nn])

        return grid[m - 1][n - 1]


if __name__ == "__main__":
    testCase = Solution_B()

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
    print("All passed")
