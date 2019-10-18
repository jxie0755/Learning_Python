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
        """
        Version A
        新建一个表, 不破坏原表
        """
        if not len(grid) or not len(grid[0]):
            return 0

        m, n = len(grid[0]), len(grid)
        min_to = [[1 for _ in range(m)] for _ in range(n)]

        for nn in range(n):
            for mm in range(m):
                if nn == 0 and mm == 0:
                    min_to[nn][mm] = grid[nn][mm]
                elif nn == 0:
                    min_to[nn][mm] = grid[nn][mm] + min_to[nn][mm - 1]
                elif mm == 0:
                    min_to[nn][mm] = grid[nn][mm] + min_to[nn - 1][mm]
                else:
                    # Difference from Leetcode P063, select the mininmum from two path lead to this spot
                    min_to[nn][mm] = grid[nn][mm] + min(min_to[nn][mm - 1], min_to[nn - 1][mm])

        return min_to[n - 1][m - 1]


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Version B
        直接在原表上改动, 破坏原表, 但是速度更快
        """
        if not len(grid) or not len(grid[0]):
            return 0

        m, n = len(grid[0]), len(grid)
        for nn in range(n):
            for mm in range(m):
                if nn == 0 and mm == 0:
                    pass
                elif nn == 0:
                    grid[nn][mm] = grid[nn][mm] + grid[nn][mm - 1]
                elif mm == 0:
                    grid[nn][mm] = grid[nn][mm] + grid[nn - 1][mm]
                else:
                    grid[nn][mm] = grid[nn][mm] + min(grid[nn][mm - 1], grid[nn - 1][mm])

        return grid[n - 1][m - 1]


if __name__ == "__main__":
    E1 = [[]]
    assert Solution().minPathSum(E1) == 0, "Edge 1"

    E2 = [[1]]
    assert Solution().minPathSum(E2) == 1, "Edge 2"

    E3 = [[1, 1]]
    assert Solution().minPathSum(E3) == 2, "Edge 3"

    E4 = [[1], [1]]
    assert Solution().minPathSum(E4) == 2, "Edge 4"

    S1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    assert Solution().minPathSum(S1) == 7, "Example 1"
    print("all passed")
