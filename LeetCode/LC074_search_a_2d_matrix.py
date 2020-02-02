"""
https://leetcode.com/problems/search-a-2d-matrix/
P074 Search a 2D Matrix
Medium


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution_A:

    def searchMatrix(self, matrix, target: int) -> bool:
        """
        Since it is strictly sorted, combine all the list and do a binary search
        """
        flat = sum(matrix, [])
        lo, hi = 0, len(flat) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False


class Solution_B:

    def searchMatrix(self, matrix, target: int) -> bool:
        """
        Direct binary search on the grid, without flatten
        Need to do two binary search
        """
        global row_mid
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row_lo = 0
        row_hi = len(matrix) - 1
        col_lo = 0
        col_hi = len(matrix[0]) - 1

        while (row_lo <= row_hi):
            row_mid = (row_lo + row_hi) // 2
            row_head = matrix[row_mid][0]
            row_tail = matrix[row_mid][len(matrix[0])-1]
            if row_head <= target <= row_tail:
                break
            elif target < row_head:
                row_hi = row_mid - 1
            else:
                row_lo = row_mid + 1

        row = matrix[row_mid]

        while col_lo <= col_hi:
            col_mid = (col_lo + col_hi) // 2
            check = row[col_mid]
            if check == target:
                return True
            elif target < check:
                col_hi = col_mid - 1
            else:
                col_lo = col_mid + 1
        return False




if __name__ == "__main__":
    testCase = Solution_B()

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
