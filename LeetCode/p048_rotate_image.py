# P048 Roate Image
# Medium


# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).


# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass







if __name__ == '__main__':
    edge_1 = [[1]]
    Solution().rotate(edge_1)
    assert edge_1 == [[1]]

    edge_2 = [[]]
    Solution().rotate(edge_2)
    assert edge_2 == [[]]

    sample_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    sample_2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    Solution().rotate(sample_1)
    Solution().rotate(sample_2)

    assert sample_1 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    assert sample_2 == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]

    print('all passed')
