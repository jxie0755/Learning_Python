# P073 Set Matrix Zeroes
# Medium



# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        coor_list = []

        for nn in range(n):
            for mm in range(m):
                if matrix[nn][mm] == 0:
                    coor_list.append((nn, mm))

        for coor in coor_list:
            x, y = coor[0], coor[1]
            matrix[x] = [0 for _ in range(m)]
            for nn in range(n):
                matrix[nn][y] = 0




if __name__ == "__main__":
    e1 = [[]]
    Solution().setZeroes(e1)
    assert e1 == [[]], "Edge 1"

    e2 = [[1]]
    Solution().setZeroes(e2)
    assert e2 == [[1]], "Edge 2"

    e3 = [[0]]
    Solution().setZeroes(e3)
    assert e3 == [[0]], "Edge 3"

    e4 = [[0], [1]]
    Solution().setZeroes(e4)
    assert e4 == [[0], [0]], "Edge 4"

    e5 = [[0, 1]]
    Solution().setZeroes(e5)
    assert e5 == [[0, 0]], "Edge 5"

    s1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(s1)
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
    Solution().setZeroes(s2)
    assert s2 == [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ], "Example 2"

    print("all passed")
