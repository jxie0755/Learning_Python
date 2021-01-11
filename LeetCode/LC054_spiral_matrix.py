"""
https://leetcode.com/problems/spiral-matrix/
P054 Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

from typing import *


class Solution_A:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Use multiple helper functions to solve
        Needs buffer area around the matrix
        """

        def next_coor(coor, direction):
            """Helper A1"""
            x, y = coor[0], coor[1]
            if direction == "right":
                return [x, y + 1]
            elif direction == "down":
                return [x + 1, y]
            elif direction == "left":
                return [x, y - 1]
            elif direction == "up":
                return [x - 1, y]

        def gen_direction():
            """Helper A2"""
            directions = ["right", "down", "left", "up"]
            D = 0
            while True:
                direction = directions[D % 4]
                D += 1
                yield direction

        def get_coor(coor):
            """Helper A3"""
            x, y = coor[0], coor[1]
            return matrix[x][y]

        def set_coor(coor, val):
            """Helper A4"""
            x, y = coor[0], coor[1]
            matrix[x][y] = val

        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        total_steps = m * n
        result = []

        # create a buffer around the matrix to determine the boundary
        matrix.insert(0, ["X" for _ in range(n)])
        matrix.append(["X" for _ in range(n)])
        for i in matrix:
            i.insert(0, "X")
            i.append("X")

        D = gen_direction()
        go = next(D)
        coor = [1, 1]  # after adding buffer area, original starting point become [1,1] instead of [0,0]

        for each_step in range(total_steps):
            result.append(get_coor(coor))
            set_coor(coor, "X")  # when iterated, change value to "X" so that buffer area updateds
            go_coor = next_coor(coor, go)

            # use buffer area detection to tell if a turn is needed
            if get_coor(go_coor) == "X":
                go = next(D)

            coor = next_coor(coor, go)

        return result


class Solution_B:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Direct output, no buffer needed
        """
        result = []

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return result

        m, n = len(matrix), len(matrix[0])
        step = 0
        top_idx, bot_idx, left_idx, right_idx = 0, m - 1, 0, n - 1

        while step < m * n:
            # always check step for each for loop

            if step < m*n:
                for a in range(left_idx, right_idx + 1):  # left -> right
                    result.append(matrix[top_idx][a])
                    step += 1
                top_idx += 1

            if step < m * n:
                for b in range(top_idx, bot_idx + 1):  # top -> bot
                    result.append(matrix[b][right_idx])
                    step += 1
                right_idx -= 1

            if step < m * n:
                for c in range(right_idx, left_idx - 1, -1):  # right -> left
                    result.append(matrix[bot_idx][c])
                    step += 1
                bot_idx -= 1

            if step < m * n:
                for d in range(bot_idx, top_idx - 1, -1):  # bot -> top
                    result.append(matrix[d][left_idx])
                    step += 1
                left_idx += 1

        return result


if __name__ == "__main__":
    testCase = Solution_B()

    edge_0 = []
    assert testCase.spiralOrder(edge_0) == [], "Edge 0"

    edge_1 = [[]]
    assert testCase.spiralOrder(edge_1) == [], "Edge 1"

    edge_2 = [[1]]
    assert testCase.spiralOrder(edge_2) == [1], "Edge 2"

    edge_3 = [[1], [2]]
    assert testCase.spiralOrder(edge_3) == [1, 2], "Edge 3"

    edge_4 = [[1, 2]]
    assert testCase.spiralOrder(edge_4) == [1, 2], "Edge 4"

    sample_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert testCase.spiralOrder(sample_1) == [1, 2, 3, 6, 9, 8, 7, 4, 5], "Example 1"

    sample_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert testCase.spiralOrder(sample_2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "Example 2"

    sample_3 = [
        [1, 2],
        [3, 4]
    ]
    assert testCase.spiralOrder(sample_3) == [1, 2, 4, 3], "Example 3"

    sample_4 = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
    assert testCase.spiralOrder(sample_4) == [1, 2, 4, 6, 8, 7, 5, 3], "Extra"

    print("All passed")
