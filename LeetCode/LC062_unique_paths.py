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
        Use combination method: Combination pick r out of x : x! // (x! * (x-r)!)
        """
        total = m + n - 2 # actually m-1 + n-1, as path is node-1

        # picke m-1 steps out of total steps, to go right
        # this mathmetically equals to pick n-1 steps out of total steps
        return factorial(total) // (factorial(m-1) * factorial(n - 1))


class Solution_B:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Recursive method with hashmap memorizaton
        """
        hmp = dict()

        def uniquePaths_recur_mem(m: int, n: int) -> int:
            """recursion helper"""
            if m == 1 or n == 1: # end case, when there is only one direction to go
                return 1
            elif (m, n) in hmp:
                return hmp[(m, n)]
            else:

                # branch recursion, the sum of paths of two directions
                result = uniquePaths_recur_mem(m-1, n) + uniquePaths_recur_mem(m, n-1)

                hmp[(m, n)] = result # record the result to avoid repeating recursion
                return result

        return uniquePaths_recur_mem(m, n)

class Solution_C:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Use grid iteration
        Get last grid value by adding the value of the neighbors from up and left
        This can avoid large number factorial calculation
        """
        grid = [[1] * m for _ in range(n)] # m*n grid with every element value = 1
        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0: # avoid edge element as there can be only one way to reach, already set at 1
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.uniquePaths(1, 1) == 1, "Edge 1"
    assert testCase.uniquePaths(4, 1) == 1, "Edge 2"
    assert testCase.uniquePaths(1, 4) == 1, "Edge 3"

    assert testCase.uniquePaths(3, 2) == 3, "Example 1"
    assert testCase.uniquePaths(7, 3) == 28, "Example 2"
    assert testCase.uniquePaths(23, 12) == 193536720, "Example 3, large number"
    print("All passed")
