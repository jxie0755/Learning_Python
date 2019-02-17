# P036 Valid Sudoku
# Medium


# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.


class Solution:
    Stable = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def correct_line(self, row):
        written = []
        for i in row:
            if i == ".":
                pass
            elif i not in written:
                written.append(i)
            else:
                return False
        return True

    def all_rows(self, board):
        return all([self.correct_line(row) for row in board])

    def all_cols(self, board):
        result = []
        for i in range(0, 9):
            col = [board[i][j] for j in range(0, 9)]
            result.append(self.correct_line(col))
        return all(result)



    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        pass







example_1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

assert Solution().isValidSudoku(example_1) == True;

example_2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

assert Solution().isValidSudoku(example_2) == False;




