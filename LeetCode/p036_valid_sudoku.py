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
        for row in board:
            if not self.correct_line(row):
                return False
        return True

    def all_cols(self, board):
        for i in range(0, 9):
            col = [board[i][j] for j in range(0, 9)]
            print(col)
            if not self.correct_line(col):
                return False
        return True

    def all_blocks(self, board):
        for add_on_row in range(0,9,3):
            for add_on_col in range(0,9,3):
                block = sum([board[i+add_on_col][0+add_on_row:3+add_on_row] for i in range(3)], [])
                if not self.correct_line(block):
                    return False
        return True

    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        return self.all_rows(board) and self.all_cols(board) and self.all_blocks(board)





if __name__ == '__main__':
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

    assert Solution().isValidSudoku(example_2) == False

    example_3 = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]

    print(Solution().all_cols(example_3))

    assert Solution().isValidSudoku(example_3) == False

    print('all passed')

