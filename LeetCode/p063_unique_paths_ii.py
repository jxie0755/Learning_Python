# P063 Unique Paths II
# Medium

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100.

from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 1
        total = m + n
        return factorial(total) // (factorial(total - n) * factorial(n))

    def uniquePathsWithObstacles(self, obstacleGrid):


        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        paths_to = [[0 for _ in range(m)] for _ in range(n)]

        # assume there is no block
        for nn in range(n):
            for mm in range(m):
                paths_to[nn][mm] = self.uniquePaths(mm, nn)


        # now update the block
        for nn in range(n):
            for mm in range(m):
                if obstacleGrid[nn][mm] == 1:
                    paths_to[nn][mm] = 0


        for nn in range(n):
            for mm in range(m):
                if nn == 0 and mm == 0 or paths_to[nn][mm] == 0:
                    pass
                elif nn == 0:
                    paths_to[nn][mm] = paths_to[nn][mm-1]
                elif mm == 0:
                    paths_to[nn][mm] = paths_to[nn-1][mm]

                else:
                    paths_to[nn][mm] = paths_to[nn][mm-1] + paths_to[nn-1][mm]

        return paths_to[n-1][m-1]


e5 = [
        [0, 1],
        [0, 0]
    ]
print(Solution().uniquePathsWithObstacles(e5))

# if __name__ == '__main__':
#     e0 = [[0]]
#     assert Solution().uniquePathsWithObstacles(e0) == 1, 'Edge 0'
#
#     e1 = [[1]]
#     assert Solution().uniquePathsWithObstacles(e1) == 0, 'Edge 1'
#
#     e2 = [
#         [0, 0],
#         [1, 0]
#     ]
#     assert Solution().uniquePathsWithObstacles(e2) == 1, 'Edge 2'
#
#     e3 = [[1,1]]
#     assert Solution().uniquePathsWithObstacles(e3) == 0, 'Edge 3'
#
#     e4 = [[1, 0]]
#     assert Solution().uniquePathsWithObstacles(e4) == 0, 'Edge 4'
#
#     e5 = [
#         [0, 1],
#         [0, 0]
#     ]
#     assert Solution().uniquePathsWithObstacles(e5) == 1, 'Edge 5'
#
#     s1 = [
#         [0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0]
#     ]
#     assert Solution().uniquePathsWithObstacles(s1) == 2, 'Example 1'
#
#     s2 = [
#         [0, 0, 0, 0],
#         [0, 1, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 1, 0],
#         [0, 0, 0, 0]
#     ]
#     assert Solution().uniquePathsWithObstacles(s2) == 7, 'Example 2'
#
#     print('all passed')
