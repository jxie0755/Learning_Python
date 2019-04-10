# P054 Spiral Matrix
# Medium


# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

from typing import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == '__main__':
    edge_1 = [[]]
    assert Solution().spiralOrder(edge_1) == [], 'Edge 1'

    edge_2 = [[1]]
    assert Solution().spiralOrder(edge_2) == [1], 'Edge 2'

    edge_3 = [[1],[2]]
    assert Solution().spiralOrder(edge_3) == [1, 2], 'Edge 3'

    edge_4 = [[1, 2]]
    assert Solution().spiralOrder(edge_4) == [1, 2], 'Edge 4'

    sample_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert Solution().spiralOrder(sample_1) == [1,2,3,6,9,8,7,4,5], "Example 1"

    sample_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert Solution().spiralOrder(sample_2) == [1,2,3,4,8,12,11,10,9,5,6,7],  "Example 2"

    print('all passed')
