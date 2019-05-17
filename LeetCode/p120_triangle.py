# P120 Triangle
# Medium

# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


from typing import *


class Solution:
    ### Recursive method
    ### This will pass but exceed max time limit as the recursion grow exponentially
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def helper(depth, idx):
            row = triangle[depth]
            if depth == len(triangle) - 1:
                return row[idx]
            else:
                return min(row[idx] + helper(depth+1, idx), row[idx] + helper(depth+1, idx+1))

        return helper(0,0)



if __name__ == '__main__':
    assert Solution().minimumTotal([]) == 0, 'Edge 0'
    assert Solution().minimumTotal([[1]]) == 1, 'Edge 1'

    A = [
           [2],
          [3, 4],
         [6, 5, 7],
        [4, 1, 8, 3]
    ]

    assert Solution().minimumTotal(A) == 11, 'Example 1'
    print('all passed')
