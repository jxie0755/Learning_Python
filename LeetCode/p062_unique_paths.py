# P062 Unique Paths
# Medium


# A robot is located at the top-left corner of a m x n grid (marked "Start" in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked "Finish" in the diagram below).

# How many possible unique paths are there?


from math import factorial


# This is the same as ProjectEuler p 015 lattice paths
# use combination method: Combination pick r out of n : n! // r! // (n-r)!
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        return factorial(total) // (factorial(total - (n - 1)) * factorial(n - 1))


if __name__ == "__main__":
    assert Solution().uniquePaths(1, 1) == 1, "Edge 1"
    assert Solution().uniquePaths(4, 1) == 1, "Edge 2"
    assert Solution().uniquePaths(1, 4) == 1, "Edge 3"

    assert Solution().uniquePaths(3, 2) == 3, "Example 1"
    assert Solution().uniquePaths(7, 3) == 28, "Example 2"

    print("all passed")
