"""
https://leetcode.com/problems/triangle/
LC120 Triangle
Medium

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""

from typing import *


class Solution_A:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.minimumTotal([[1]]) == 1, "Edge 1"

    A = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    assert testCase.minimumTotal(A) == 11, "Example 1"
    print("All passed")


