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
        This will take extra space
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
        Direct binary search on the grid with two binary search
        """
        if not matrix or not matrix[0]:
            return False

        # find the correct row from the first element.
        # No need to equal target, as long as the first element <= target and next row's first element is larger
        row_lo = 0
        row_hi = len(matrix) - 1
        while row_lo <= row_hi:
            row_idx = (row_lo + row_hi) // 2
            row_head = matrix[row_idx][0]
            if row_head > target:
                row_hi = row_idx - 1
            elif row_head == target:
                break
            elif row_head < target:
                if row_idx == len(matrix) - 1: # already at low row
                    break
                else: # check next row's first element
                    if matrix[row_idx + 1][0] <= target:
                        row_lo = row_idx + 1
                    else:
                        break

        # Find if the element is in the row (matrix[row_idx])
        row = matrix[row_idx]
        col_lo = 0
        col_hi = len(row) - 1
        while col_lo <= col_hi:
            col_idx = (col_lo + col_hi) // 2
            if row[col_idx] < target:
                col_lo = col_idx + 1
            elif row[col_idx] == target:
                return True
            else:
                col_hi = col_idx - 1
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
