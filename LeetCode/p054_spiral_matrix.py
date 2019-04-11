# P054 Spiral Matrix
# Medium


# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

from typing import *
class Solution:
    def spiralOrder(self, matrix):

        def next_coor(coor, direction):
            x, y = coor[0], coor[1]
            if direction == 'right':
                return [x, y+1]
            elif direction == 'down':
                return [x+1, y]
            elif direction == 'left':
                return [x, y-1]
            elif direction == 'up':
                return [x-1, y]

        def gen_direction():
            directions = ['right', 'down', 'left', 'up']
            D = 0
            while True:
                direction = directions[D % 4]
                D += 1
                yield direction

        def get_coor(coor):
            x, y = coor[0], coor[1]
            return matrix[x][y]

        def set_coor(coor, val):
            x, y = coor[0], coor[1]
            matrix[x][y] = val

        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        total_steps = m * n
        result = []

        # buffer
        matrix.insert(0, ['X' for _ in range(n)])
        matrix.append(['X' for _ in range(n)])
        for i in matrix:
            i.insert(0, 'X')
            i.append('X')

        D = gen_direction()
        go = next(D)
        coor = [1, 1]
        while total_steps:
            result.append(get_coor(coor))
            set_coor(coor, 'X')

            go_coor = next_coor(coor, go)
            if get_coor(go_coor) == 'X':
                go = next(D)
            coor = next_coor(coor, go)
            total_steps -= 1

        return result



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
