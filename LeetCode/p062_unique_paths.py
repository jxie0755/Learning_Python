"""
https://leetcode.com/problems/unique-paths/
P062 Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked "Start" in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked "Finish" in the diagram below).

How many possible unique paths are there?
"""

from math import factorial


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Version A, best direct math calculation
        This is the same as ProjectEuler p015 lattice paths
        Use combination method: Combination pick r out of n : n! // r! // (n-r)!
        """
        total = m + n - 2
        return factorial(total) // (factorial(total - (n - 1)) * factorial(n - 1))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Version B, recursive method
        This will fail as the speed is too slow.
        Could use memorization to accellerate but this will be skipped.
        """
        if m <= 1 or n <= 1:
            return 1
        else:
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Version C, use grid iteration
        Get last grid value by adding the value of the neighbors from up and left
        This can avoid large number factorial calculation
        """
        grid = [[1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]




if __name__ == "__main__":
    assert Solution().uniquePaths(1, 1) == 1, "Edge 1"
    assert Solution().uniquePaths(4, 1) == 1, "Edge 2"
    assert Solution().uniquePaths(1, 4) == 1, "Edge 3"

    assert Solution().uniquePaths(3, 2) == 3, "Example 1"
    assert Solution().uniquePaths(7, 3) == 28, "Example 2"
    assert Solution().uniquePaths(23, 12) == 193536720, "Example 3, large number"
    print("all passed")
