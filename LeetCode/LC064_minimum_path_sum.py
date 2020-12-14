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
        """
        if not len(grid) or not len(grid[0]):
            return 0

        m, n = len(grid[0]), len(grid)
        min_to = [[1 for _ in range(m)] for _ in range(n)]

        for nn in range(n):
            for mm in range(m):
                cur = grid[mm][nn]
                if nn == 0 and mm == 0:
                    min_to[nn][mm] = cur
                elif nn == 0:
                    min_to[nn][mm] = cur + min_to[nn][mm - 1]
                elif mm == 0:
                    min_to[nn][mm] = cur + min_to[nn - 1][mm]
                else:
                    # Difference from Leetcode P063, select the mininmum from two path lead to this spot
                    min_to[nn][mm] = cur + min(min_to[nn][mm - 1], min_to[nn - 1][mm])

        return min_to[n - 1][m - 1]


class Solution_B:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        直接在原表上改动, 破坏原表, 但是速度更快
        """
        m = len(grid)
        n = len(grid[0])

        if not len(grid) or not len(grid[0]):
            return 0

        for mm in range(m):
            for nn in range(n):
                cur = grid[mm][nn]
                if mm == 0 and nn == 0:
                    pass
                elif mm == 0:
                    grid[mm][nn] = cur + grid[mm][nn - 1]
                elif nn == 0:
                    grid[mm][nn] = cur + grid[mm - 1][nn]
                else:
                    grid[mm][nn] = cur + min(grid[mm][nn - 1], grid[mm - 1][nn])

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
    print("all passed")
