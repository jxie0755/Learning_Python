"""
https://leetcode.com/problems/unique-paths-ii/
P063 Unique Paths II
Medium

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked "Finish" in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.
"""


from typing import *

class Solution_A:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Similar idea from Leetcode 062 iteration method
        Additional: set the number of path at the obstacle to be 0
        """

        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        pathgrid = [[1 for _ in range(m)] for _ in range(n)]

        for nn in range(n):
            for mm in range(m):
                if obstacleGrid[nn][mm] == 1:
                    pathgrid[nn][mm] = 0
                elif nn == 0:
                    pathgrid[nn][mm] = pathgrid[nn][mm - 1]  # 防止边路出现障碍, 不要直接设为1, 而是重复之前的值
                elif mm == 0:
                    pathgrid[nn][mm] = pathgrid[nn - 1][mm]
                else:
                    pathgrid[nn][mm] = pathgrid[nn][mm - 1] + pathgrid[nn - 1][mm]

        # for i in paths_to:
        #     print(i)

        return pathgrid[n - 1][m - 1]


if __name__ == "__main__":
    testMethod = Solution_A().uniquePathsWithObstacles
    e0 = [[0]]
    assert testMethod(e0) == 1, "Edge 0"

    e1 = [[1]]
    assert testMethod(e1) == 0, "Edge 1"

    e2 = [
        [0, 0],
        [1, 0]
    ]
    assert testMethod(e2) == 1, "Edge 2"

    e3 = [[1, 1]]
    assert testMethod(e3) == 0, "Edge 3"

    e4 = [[1, 0]]
    assert testMethod(e4) == 0, "Edge 4"

    e5 = [
        [0, 1],
        [0, 0]
    ]
    assert testMethod(e5) == 1, "Edge 5"

    s1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert testMethod(s1) == 2, "Example 1"

    s2 = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert testMethod(s2) == 7, "Example 2"

    print("all passed")
