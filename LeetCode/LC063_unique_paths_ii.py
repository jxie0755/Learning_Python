"""
https://leetcode.com/problems/unique-paths-ii/
LC063 Unique Paths II
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
        Use the idea of LC062 version C (grid iteration)
        when hitting an obstacle, meansing the path to this point is 0
        """
        # First iterate the grid to relabel
        m = len(obstacleGrid)  # length
        n = len(obstacleGrid[0])  # width

        # iteration the grid
        for l in range(m):
            for w in range(n):
                point = obstacleGrid[l][w]
                if point == 1:  # 这里先把obstacle标记成0,以便数学计算路径之和
                    obstacleGrid[l][w] = 0
                elif l == 0 and w == 0:  # 这里把起始点标记成1 (使用elif避免误标obstacle)
                    obstacleGrid[l][w] = 1
                else:  # 其他点, 也是确定不是obstacle之后
                    if l == 0:  # first row, follow the left
                        obstacleGrid[l][w] = obstacleGrid[l][w - 1]
                    elif w == 0:  # first column, follow the up
                        obstacleGrid[l][w] = obstacleGrid[l - 1][w]
                    else:  # left + up
                        obstacleGrid[l][w] = obstacleGrid[l][w - 1] + obstacleGrid[l - 1][w]

        return obstacleGrid[m - 1][n - 1]


if __name__ == "__main__":
    testCase = Solution_A()
    e0 = [[0]]
    assert testCase.uniquePathsWithObstacles(e0) == 1, "Edge 1"

    e1 = [[1]]
    assert testCase.uniquePathsWithObstacles(e1) == 0, "Edge 2"

    e2 = [
        [0, 0],
        [1, 0]
    ]
    assert testCase.uniquePathsWithObstacles(e2) == 1, "Edge 3"

    e3 = [[1, 1]]
    assert testCase.uniquePathsWithObstacles(e3) == 0, "Edge 4"

    e4 = [[1, 0]]
    assert testCase.uniquePathsWithObstacles(e4) == 0, "Edge 5"

    e5 = [
        [0, 1],
        [0, 0]
    ]
    assert testCase.uniquePathsWithObstacles(e5) == 1, "Edge 6"

    s1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert testCase.uniquePathsWithObstacles(s1) == 2, "Example 1"

    s2 = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert testCase.uniquePathsWithObstacles(s2) == 7, "Example 2"

    s3 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert testCase.uniquePathsWithObstacles(s3) == 0, "Additional 1, all blocked"

    s4 = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    assert testCase.uniquePathsWithObstacles(s4) == 6, "Additional 2, equal to 3 * 3 with no obstacle"

    print("All passed")
