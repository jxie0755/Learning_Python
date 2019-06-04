# P063 Unique Paths II
# Medium

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.

from math import factorial

class Solution:

    # According to ProjectEuler p015 2nd version
    # plot the ways to each coor for the whole grid
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        paths_to = [[1 for _ in range(m)] for _ in range(n)]

        for nn in range(n):
            for mm in range(m):
                if obstacleGrid[nn][mm] == 1:
                    paths_to[nn][mm] = 0
                elif nn == 0:
                    paths_to[nn][mm] = paths_to[nn][mm - 1]
                elif mm == 0:
                    paths_to[nn][mm] = paths_to[nn - 1][mm]
                else:
                    paths_to[nn][mm] = paths_to[nn][mm-1] + paths_to[nn-1][mm]

        # for i in paths_to:
        #     print(i)

        return paths_to[n-1][m-1]


if __name__ == '__main__':
    e0 = [[0]]
    assert Solution().uniquePathsWithObstacles(e0) == 1, 'Edge 0'

    e1 = [[1]]
    assert Solution().uniquePathsWithObstacles(e1) == 0, 'Edge 1'

    e2 = [
        [0, 0],
        [1, 0]
    ]
    assert Solution().uniquePathsWithObstacles(e2) == 1, 'Edge 2'

    e3 = [[1,1]]
    assert Solution().uniquePathsWithObstacles(e3) == 0, 'Edge 3'

    e4 = [[1, 0]]
    assert Solution().uniquePathsWithObstacles(e4) == 0, 'Edge 4'

    e5 = [
        [0, 1],
        [0, 0]
    ]
    assert Solution().uniquePathsWithObstacles(e5) == 1, 'Edge 5'

    s1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().uniquePathsWithObstacles(s1) == 2, 'Example 1'

    s2 = [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().uniquePathsWithObstacles(s2) == 7, 'Example 2'

    print('all passed')
