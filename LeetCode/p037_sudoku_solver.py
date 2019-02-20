# P037 Sudoku Solver
# Hard


# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'


# Note:
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.

import copy

class Solution:

    def __init__(self, puzzle=[
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]):
        """
        An empty checkerboard -
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0

        When initiated:
        The empty checkerboard is skipped by directly loading a pre-written board with numbers on.
        The pre-written board follows the same structure as a nested list like empty.
        """
        self.board = puzzle
        # Also create a permanent puzzle copy for future use
        self.puzzle = self.board_mem()


    # Build up class attributes to for future to check up the rows, columns and grids.
    def row(self, n):
        """output a row of numbers
        n: int 1-9
        return: a list of numbers extracted from the row
        """
        self.rows = self.board[:]  # make a copy
        return self.rows[9 - n]

    def col(self, n):
        """output a column of numbers
        n: int 1-9
        return: a list of numbers extracted from the column
        """
        self.columns = [[self.board[i][j] for i in range(9)] for j in range(9)]
        return self.columns[n - 1]

    def grid(self, n):
        """output a grid of 3*3 in the checkboard
        n: int 1-9

        The grid index on the checkerboad will be:
        1 2 3
        4 5 6
        7 8 9

        return: a list of numbers extracted from the grid
        """
        g1 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(0, 3)], [])
        g2 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(0, 3)], [])
        g3 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(0, 3)], [])
        g4 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(3, 6)], [])
        g5 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(3, 6)], [])
        g6 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(3, 6)], [])
        g7 = sum([[self.board[i][j] for j in range(0, 3)] for i in range(6, 9)], [])
        g8 = sum([[self.board[i][j] for j in range(3, 6)] for i in range(6, 9)], [])
        g9 = sum([[self.board[i][j] for j in range(6, 9)] for i in range(6, 9)], [])
        self.grids = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
        return self.grids[n - 1]

    # Define moves to add numbers to the board
    def insert(self, x, y, value):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        self.board[9 - y][x - 1] = value

    def board_mem(self):
        """a snpashot of current board
        for future roll back
        """
        return [self.board[i][:] for i in range(9)]

    # define some verification method
    def get_value(self, coor):
        """return the number at a coordinate in the checkerboard
        coor: a tuple with two value (x, y)
        return: the number on the checkerboard
        """
        return self.board[9 - coor[1]][coor[0] - 1]

    def get_row_col_sub(self, coor):
        """return a list of 3 list, that contains the related row, column and sub grid of that coor
        """
        row_at = self.row(coor[1])
        col_at = self.col(coor[0])

        if coor[0] in [1, 2, 3]:
            if coor[1] in [1, 2, 3]:
                n = 7
            elif coor[1] in [4, 5, 6]:
                n = 4
            elif coor[1] in [7, 8, 9]:
                n = 1

        elif coor[0] in [4, 5, 6]:
            if coor[1] in [1, 2, 3]:
                n = 8
            elif coor[1] in [4, 5, 6]:
                n = 5
            elif coor[1] in [7, 8, 9]:
                n = 2

        elif coor[0] in [7, 8, 9]:
            if coor[1] in [1, 2, 3]:
                n = 9
            elif coor[1] in [4, 5, 6]:
                n = 6
            elif coor[1] in [7, 8, 9]:
                n = 3

        grid_at = self.grid(n)
        return [row_at, col_at, grid_at]

    def no_conflict(self):
        """return if there is a conflict in the board, where 2 same number (!=0) showed up:
        in the same row, column or grid

        return True if no conflicts were found
        return False if conflicts were found
        """
        all_subs = [self.row(n) for n in range(1, 10)] + [self.row(n) for n in range(1, 10)] + [self.grid(n) for n in range(1, 10)]
        for sub in all_subs:
            check_list = []
            for i in sub:
                if i != "0":
                    if i not in check_list:
                        check_list.append(i)
                    else:
                        return False
        return True

    def all_filled(self):
        """To ensure all the place is filled with a number"""
        return all(all(j != "." for j in i) for i in self.board)

    def valid_solution(self):
        """To check if the puzzle is solved"""
        return self.all_filled() and self.no_conflict()

    def analysis(self):
        """return a dict of every vacant coordinate linked to the possible value it can be put in
        the result dict should be in the form of :
        {(x,y): [v1, v2, v3], (x,y): [v1, v2, v3], (x,y): [v1, v2, v3]}
        """
        result = {}
        for x in range(1, 10):
            for y in range(1, 10):
                coordinate = (x, y)
                if self.get_value(coordinate) == '.':
                    all_subs = self.get_row_col_sub(coordinate)
                    cant_be = [i for i in sum(all_subs, []) if i != "."]
                    all_nums = ["1", "2", "3",
                                "4", "5","6",
                                "7", "8", "9"]
                    can_be = [i for i in all_nums if i not in cant_be]
                    result[coordinate] = can_be
        return result

    def direct_deduce(self):
        """To analyze each vacant coordinate, and if there is only one possible value for it
        fill it in with the value on the checkerboard"""

        def deduce():
            to_be_filled = []
            all_possible = self.analysis()
            for key, value in all_possible.items():
                if len(value) == 1:
                    to_be_filled.append((key, value[0]))
            return to_be_filled

        to_be_filled = deduce()
        while to_be_filled:
            for coor, value in to_be_filled:
                self.insert(coor[0], coor[1], value)
            to_be_filled = deduce()

    def feasible(self):
        """return True if all vacant spot can still fill in a possible number"""
        all_possible = self.analysis()
        for key, value in all_possible.items():
            if len(value) == 0:
                return False
        if self.all_filled():
            return False
        return True

    def hypothesize(self):
        """analyze the board and picke the coordinate with least possible values
        then generate a list of sublist which contains coor and a possible value
        in the form of:
        [[(x,y), value],[(x,y), value],[(x,y), value]]
        """
        result = []
        all_possible = self.analysis()
        coor = min(all_possible, key=lambda x: len(all_possible.get(x)))
        value = all_possible[coor]
        for i in value:
            result.append([coor, i])
        return result

    def hyper_move(self, to_move):
        """try to move a hypothsized spot with a possible number
        to_move: a list as a pair of coordinates and possible values in the form of:
        [(x,y), value]
        according to to_move, the board insert this hyperthetical value
        """
        self.insert(to_move[0][0], to_move[0][1], to_move[1])

    # Final solution
    def solve(self):
        """This will solve the problem and fill the self.board with correct answer
        it will then print(self) to show the answer
        """
        snapshot_board = []
        snapshot_to_do = []
        count = 0
        hypo_layer = 0
        hypo_layer_all = []

        while not self.valid_solution():
            count += 1
            hypo_layer_all.append(hypo_layer)
            self.direct_deduce()

            if self.valid_solution():
                break

            if self.feasible():
                attemp_move = self.hypothesize()
                for i in range(len(attemp_move) - 1):
                    snapshot_board.append(self.board_mem())
                snapshot_to_do += attemp_move
                self.hyper_move(snapshot_to_do.pop())
                hypo_layer += 1

            else:
                hypo_layer -= 1
                self.board = snapshot_board.pop()
                self.hyper_move(snapshot_to_do.pop())

        return self.board[:]

    # For Leetcode P037
    def solveSudoku(self, board):
        ans = Solution(board).solve()
        for i in range(9):
            for j in range(9):
                board[i][j] = ans[i][j]


# class Solution:
#     def solveSudoku(self, board: 'List[List[str]]') -> 'None':
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         def sudoku_done(b):
#             for x in range(0,9):
#                 if "." in b[x]:
#                     return False
#             return True
#
#
#         tmp_board = []
#         all_sudoku_guess = []
#
#         while not sudoku_done(board):
#             # print(sudoku_done(board))
#             move_on = 0
#             list_possible_num = []
#             possible_num_min = ["1","2","3","4","5","6","7","8","9"]
#             all_possible_num = []
#             for coor_x in range(0,9):
#                 for coor_y in range(0,9):
#                     if board[coor_x][coor_y] == '.':
#                         possible_num = ["1","2","3","4","5","6","7","8","9"]
#                         for n in range(0,9):
#                             if board[coor_x][n] in possible_num:
#                                 possible_num.remove(board[coor_x][n])
#                             if board[n][coor_y] in possible_num:
#                                 possible_num.remove(board[n][coor_y])
#                         for n1 in range(0,9):
#                             for n2 in range(0,9):
#                                 if (n1//3 == coor_x//3 and
#                                     n2//3 == coor_y//3 and
#                                     board[n1][n2] in possible_num):
#                                     possible_num.remove(board[n1][n2])
#                         all_possible_num.append([coor_x,coor_y,possible_num])
#
#                         if len(possible_num) < len(possible_num_min):
#                             possible_num_min = possible_num
#                         #print("coor: ",coor_x,coor_y,", possible num: ",possible_num)
#                         if len(possible_num) == 1:
#                             board[coor_x][coor_y] = possible_num[0]
#                             move_on = 1
#                         if len(possible_num) == 0:
#                             move_on = -1
#                             break
#
#
#
#             if move_on == 0:
#                 for each_node in all_possible_num:
#                     if each_node[2] == possible_num_min:
#
#                         board_copy = copy.deepcopy(board)
#                         tmp_board.append(board_copy)
#
#
#                         board[each_node[0]][each_node[1]] = each_node[2][0]
#                         each_node[2].pop(0)
#                         all_sudoku_guess.append(each_node)
#                         break
#
#             while move_on == -1:
#                 board = tmp_board[-1]
#                 tmp_board.pop()
#                 each_node = all_sudoku_guess[-1]
#                 all_sudoku_guess.pop()
#
#                 if len(each_node[2]) == 0:
#                     move_on == -1
#                     continue
#                 board[each_node[0]][each_node[1]] = each_node[2][0]
#                 each_node[2].pop(0)
#
#                 all_sudoku_guess.append(each_node)
#                 tmp_board.append(board)
#                 move_on = 1
#
#         # print(sudoku_done(board))
#         # print(board)


if __name__ == '__main__':
    question = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    Solution().solveSudoku(question)
    assert question == [
        ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
        ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
        ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
        ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
        ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
        ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
        ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
        ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
        ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
    ]

    question_2 = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."]
    ]
    Solution().solveSudoku(question_2)

    assert question_2 == [
        ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
        ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
        ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
        ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
        ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
        ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
        ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
        ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
        ["6", "4", "1", "2", "7", "5", "9", "8", "3"]
    ]



    print("all passed")



