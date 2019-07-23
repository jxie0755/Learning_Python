# P085 Maximal Rectangle
# Hard


# Given a 2D binary matrix filled with 0"s and 1"s, find the largest rectangle containing only 1's and return its area.


class Solution:
    def maximalRectangle(self, matrix):
        hmp = dict()
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(col):
                coor = (r, c)
    # TODO


if __name__ == "__main__":
    sample = [
        ["1"]
    ]
    assert Solution().maximalRectangle(sample) == 1, "Edge 1"

    sample = [
        ["1", "1"]
    ]
    assert Solution().maximalRectangle(sample) == 2, "Edge 2"

    sample = [
        ["1"],
        ["1"]
    ]
    assert Solution().maximalRectangle(sample) == 2, "Edge 3"

    sample = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    assert Solution().maximalRectangle(sample) == 6, "Example 1"

    print("all passed")
