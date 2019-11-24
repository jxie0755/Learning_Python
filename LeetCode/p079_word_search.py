"""
https://leetcode.com/problems/word-search/
P079 Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import *

count = 0


class Solution:
    def neighbor(self, board: List[List[str]], coor: Tuple[int]) -> List[Tuple[int]]:
        """Find possible coors in the neighbor"""
        row, col = len(board), len(board[0])
        x, y = coor[0], coor[1]
        up = (x - 1, y)
        down = (x + 1, y)
        left = (x, y - 1)
        right = (x, y + 1)
        neighbor_list = list(
            filter( # make sure the neighbor is in the boundary of the board
                lambda c: 0 <= c[0] < row and 0 <= c[1] < col,
                [up, down, left, right]
            )
        )
        return neighbor_list


    def exist(self, board, word: str):
        # This recursive method passed most cased but exceeded max time when case is long.
        if not board:
            return False

        row, col = len(board), len(board[0])
        N = len(word)

        # Starting list
        start = [(r, c) for r in range(row) for c in range(col) if board[r][c] == word[0]]

        def helper(board, coor, word, result):
            result.append(coor)
            if len(result) == N:
                return True
            hmp = self.neighbor(board, coor)
            nextcoor = [c for c in hmp if hmp[c] == word[1] and c not in result]
            if nextcoor:
                return any([helper(board, c, word[1:], result[:]) for c in nextcoor])
            else:
                return False

        return any([helper(board, i, word, []) for i in start])


# TODO this algorithm is not fast enough to pass the time limit


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    # assert Solution().exist(board, "ABCCED"), "Example 1"
    # assert Solution().exist(board, "SEE"), "Example 2"
    # assert not Solution().exist(board, "ABCB"), "Example 3"
    #
    # board = [
    #     ["b", "a", "b", "a", "a", "a"],
    #     ["b", "b", "b", "a", "a", "a"],
    #     ["b", "a", "b", "a", "b", "a"]
    # ]
    #
    # assert Solution().exist(board, "ba"), "Additional 1"
    #
    # long = [
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "a"],
    #     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
    #      "a", "a", "a", "a", "a", "a", "a", "b"]
    # ]
    # target = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # # print(Solution().exist(long, target))
    #
    # print("all passed")
