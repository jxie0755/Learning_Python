"""
https://leetcode.com/problems/unique-paths/
P062 Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked "Start" in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked "Finish" in the diagram below).

How many possible unique paths are there?
"""

from math import factorial


class Solution_A:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        The best direct math calculation
        This is the same as ProjectEuler p015 lattice paths
        Use combination method: Combination pick r out of n : n! // r! // (n-r)!
        """
        total = m + n - 2
        return factorial(total) // (factorial(total - (n - 1)) * factorial(n - 1))


class Solution_B:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Recursive method with hashmap memorizaton
        """
        hmp = dict()

        def uniquePaths_recur_mem(m: int, n: int) -> int:
            """recursion helper"""
            if m <= 1 or n <= 1:
                return 1
            elif (m, n) in hmp:
                return hmp[(m, n)]
            else:
                result = uniquePaths_recur_mem(m-1, n) + uniquePaths_recur_mem(m, n-1)
                hmp[(m, n)] = result
                return result

        return uniquePaths_recur_mem(m, n)

class Solution_C:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Use grid iteration
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
    testMethod = Solution_C().uniquePaths
    assert testMethod(1, 1) == 1, "Edge 1"
    assert testMethod(4, 1) == 1, "Edge 2"
    assert testMethod(1, 4) == 1, "Edge 3"

    assert testMethod(3, 2) == 3, "Example 1"
    assert testMethod(7, 3) == 28, "Example 2"
    assert testMethod(23, 12) == 193536720, "Example 3, large number"
    print("all passed")
