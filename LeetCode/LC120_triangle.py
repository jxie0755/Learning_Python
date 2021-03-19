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
        """
        Recursive method
        This will pass but exceed max time limit as the recursion grow exponentially
        """
        def helper(depth, idx):
            row = triangle[depth]

            if depth == len(triangle) - 1:
                # last row just return the value on the idx
                return row[idx]
            else:
                # recursive add the value on the idex to next roll's minimum value of the two adjacent index
                return min(row[idx] + helper(depth + 1, idx), row[idx] + helper(depth + 1, idx + 1))

        return helper(0, 0)


class Solution_B1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        This will take O(N) space, but modify the triangle by adding value to next row
        """
        for R in range(1, len(triangle)):
            row = triangle[R]
            for i in range(len(row)):
                if i == 0:
                    row[i] = triangle[R - 1][i] + row[i]
                elif i == len(row) - 1:
                    row[i] = triangle[R - 1][i - 1] + row[i]
                else:
                    row[i] = min(triangle[R - 1][i - 1], triangle[R - 1][i]) + row[i]
        return min(triangle[-1])


class Solution_B2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Same idea as B1
        But this will take the row externally leave the triangle unmodified
        """
        previous_sum = triangle[0]

        for R in range(1, len(triangle)):
            sum_path = triangle[R][:]
            for i in range(R+1):
                if i == 0:
                    sum_path[i] = previous_sum[i] + sum_path[i]
                elif i == R:
                    sum_path[i] = previous_sum[i - 1] + sum_path[i]
                else:
                    sum_path[i] = min(previous_sum[i - 1], previous_sum[i]) + sum_path[i]
            previous_sum = sum_path[:]

        return min(previous_sum)


if __name__ == "__main__":
    testCase = Solution_B2()

    assert testCase.minimumTotal([
        [1]
    ]) == 1, "Edge 1"

    assert testCase.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11, "Example 1"

    print("All passed")
