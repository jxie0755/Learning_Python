"""
https://leetcode.com/problems/valid-sudoku/
LC036 Valid Sudoku
Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    The given board contain only digits 1-9 and the character '.'.
    The given board size is always 9x9.

See reference in ZZProject/SudokuSolver
"""

from typing import *


class Solution_A:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Version A"""
        return self.all_rows(board) and self.all_cols(board) and self.all_blocks(board)

    def all_rows(self, board: List[List[str]]) -> bool:
        """Helper Aa"""

        for row in board:
            if not self.correct_line(row):
                return False
        return True

    def all_cols(self, board: List[List[str]]) -> bool:
        """Helper Ab"""

        for i in range(0, 9):
            col = [board[j][i] for j in range(0, 9)]
            if not self.correct_line(col):
                return False
        return True

    def all_blocks(self, board: List[List[str]]) -> bool:
        """Helper Ac"""

        for add_on_row in range(0, 9, 3):
            for add_on_col in range(0, 9, 3):
                block = sum([board[i + add_on_col][0 + add_on_row:3 + add_on_row] for i in range(3)], [])
                if not self.correct_line(block):
                    return False
        return True

    def correct_line(self, row: List[str]) -> bool:
        """Helper Aabc"""
        cur = "x"
        for i in row:
            if i == ".":
                pass
            elif cur == "x":
                cur = i
            elif i == cur:
                return False
        return True


if __name__ == "__main__":
    testCase = Solution_A()

    example_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert testCase.isValidSudoku(example_1) == True, "Example 1"

    example_2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert testCase.isValidSudoku(example_2) == False, "Example 2"

    example_3 = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    assert testCase.isValidSudoku(example_3) == False, "Example 3"
    print("All passed")
