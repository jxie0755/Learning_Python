"""
https://leetcode.com/problems/search-a-2d-matrix/
P074 Search a 2D Matrix
Medium


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        pass


if __name__ == "__main__":
    testCase = Solution()

    matrix = []
    assert testCase.searchMatrix(matrix, 3) == False, "Empty"

    matrix = [
        [],
    ]
    assert testCase.searchMatrix(matrix, 3) == False, "Edge 1"

    matrix = [
        [1], [3], [5], [7],
    ]
    assert testCase.searchMatrix(matrix, 3) == True, "Edge 2"

    matrix = [
        [1, 3, 5, 7],
    ]
    assert testCase.searchMatrix(matrix, 3) == True, "Edge 3"

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert testCase.searchMatrix(matrix, 5) == True, "Example 1"

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert testCase.searchMatrix(matrix, 13) == False, "Example 2"
    print("all passed")
