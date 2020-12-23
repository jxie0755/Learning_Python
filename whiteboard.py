"""
https://leetcode.com/problems/set-matrix-zeroes/
P073 Set Matrix Zeroes
Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        pass



if __name__ == "__main__":
    testCase = Solution()

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

    print("all passed")
