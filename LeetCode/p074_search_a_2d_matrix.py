# P074 Search a 2D Matrix
# Medium


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


class Solution:
    # Since it is strictly sorted, combine all the list and do a binary search
    def searchMatrix(self, matrix, target: int) -> bool:
        flat = sum(matrix, [])
        lo, high = 0, len(flat) - 1

        while lo <= high:
            mid = (lo + high) // 2
            if flat[mid] == target:
                return True
            elif flat[mid] > target:
                high = mid - 1
            else:
                lo = mid + 1
        return False


if __name__ == "__main__":
    matrix = [
        [],
    ]
    target = 3
    assert Solution().searchMatrix(matrix, target) == False, "Edge 1"

    matrix = [
        [1], [3], [5], [7],
    ]
    target = 3
    assert Solution().searchMatrix(matrix, target) == True, "Edge 2"

    matrix = [
        [1, 3, 5, 7],
    ]
    target = 3
    assert Solution().searchMatrix(matrix, target) == True, "Edge 3"

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    assert Solution().searchMatrix(matrix, target) == True, "Example 1"

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    assert Solution().searchMatrix(matrix, target) == False, "Example 2"
    print("all passed")
