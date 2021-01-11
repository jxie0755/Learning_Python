"""
https://leetcode.com/problems/set-matrix-zeroes/
P073 Set Matrix Zeroes
Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.
"""

class Solution_A:
    def setZeroes(self, matrix) -> None:
        """
        Memorize the coordinate that the value is 0 and iterate to change
        """
        m, n = len(matrix[0]), len(matrix)
        coor_list = []

        for nn in range(n):
            for mm in range(m):
                if matrix[nn][mm] == 0:
                    coor_list.append((nn, mm))

        for coor in coor_list:
            x, y = coor[0], coor[1]
            for i in range(m):
                matrix[x][i] = 0
            for nn in range(n):
                matrix[nn][y] = 0


class Solution_B:
    def setZeroes(self, matrix) -> None:
        """
        Iterate once, use two sets to record row and col to avoid repeat
        Then modify with according to the sets
        This will avoid repeatingly set the same row and col to zero
        """

        row, col = set(), set()

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                cur = matrix[m][n]
                if cur == 0:
                    row.add(m)
                    col.add(n)

        # Set all rows to zero
        for m in row:
            r = matrix[m]
            for n in range(len(matrix[m])):
                matrix[m][n] = 0

        # Set all cols to zero
        for m in range(len(matrix)):
            for n in col:
                matrix[m][n] = 0


if __name__ == "__main__":
    testCase = Solution_B()

    e1 = [[]]
    testCase.setZeroes(e1)
    assert e1 == [[]], "Edge 1"

    e2 = [[1]]
    testCase.setZeroes(e2)
    assert e2 == [[1]], "Edge 2"

    e3 = [[0]]
    testCase.setZeroes(e3)
    assert e3 == [[0]], "Edge 3"

    e4 = [[0], [1]]
    testCase.setZeroes(e4)
    assert e4 == [[0], [0]], "Edge 4"

    e5 = [[0, 1]]
    testCase.setZeroes(e5)
    assert e5 == [[0, 0]], "Edge 5"

    s1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    testCase.setZeroes(s1)
    assert s1 == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ], "Example 1"

    s2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    testCase.setZeroes(s2)
    assert s2 == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ], "Example 2"

    print("All passed")
