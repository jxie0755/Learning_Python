# P240 Search a 2D Matrix II
# Medium


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

from typing import *


class Solution:

    # Version A, straight foward binary search on lines that include the value
    def binarySearch(self, line:List[int], target:int)-> bool:
        lo, hi = 0, len(line)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_val = line[mid]
            if target == mid_val:
                return True
            elif target < mid_val:
                hi = mid -1
            else:
                lo = mid + 1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if line[0] <= target <= line[-1] and self.binarySearch(line, target):
                return True
        return False



A = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]



# print(Solution().searchMatrix(A, 5))




if __name__ == '__main__':
    A = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    assert Solution().searchMatrix(A, 5), 'Example 1'
    assert not Solution().searchMatrix(A, 20), 'Example 2'

    print('all passed')
