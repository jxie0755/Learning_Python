# P120 Triangle
# Medium

# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


from typing import *


class Solution:
    # Recursive method
    # This will pass but exceed max time limit as the recursion grow exponentially
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def helper(depth, idx):
            row = triangle[depth]

            if depth == len(triangle) - 1:
                # last row just return the value on the idx
                return row[idx]
            else:
                # recursive add the value on the idex to next roll's minimum value of the two adjacent index
                return min(row[idx] + helper(depth+1, idx), row[idx] + helper(depth+1, idx+1))

        return helper(0,0)


class Solution:
    # a two row iteration method
    # update the first row in triangle from end to begin
    # the second row is the updated minimum value of first row and second row
    # passed, very fast method
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        N = len(triangle) - 2

        next_row_min = triangle[N + 1]
        while N >= 0:
            row = triangle[N]
            new_min = []
            for i in range(0, len(row)):
                new_min.append(row[i] + min(+next_row_min[i], next_row_min[i+1]))
            next_row_min = new_min
            N -= 1
        return next_row_min[0]


    # do not general now next_row_min, modify in-place, for bonus
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        N = len(triangle) - 2
        next_row_min = triangle[N + 1]

        while N >= 0:
            row = triangle[N]
            for i in range(0, len(row)):
                next_row_min[i] = row[i] + min(next_row_min[i], next_row_min[i+1])
            N -= 1
        return next_row_min[0]



if __name__ == "__main__":
    assert Solution().minimumTotal([[1]]) == 1, "Edge 1"

    A = [
           [2],
          [3, 4],
         [6, 5, 7],
        [4, 1, 8, 3]
    ]

    assert Solution().minimumTotal(A) == 11, "Example 1"
    print("all passed")
