"""
https://leetcode.com/problems/sudoku-solver/
P037 Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'

Note:
    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.
"""

from typing import *

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Version A
        """

        ans = Solution.PySudokuSolver_A(board).solve()
        for i in range(9):
            for j in range(9):
                board[i][j] = ans[i][j]

    class PySudokuSolver_A:
        """
        来自ZZZProject/SudokuSolver/sudoku_solver_v1
        改动:
        使用String作为board元素类型而不是Integer
        把空位从"0"改成"."以符合本体要求
        删去__str__, 对解本题没有帮助
        """

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
            all_subs = [self.row(n) for n in range(1, 10)] + [self.row(n) for n in range(1, 10)] + [self.grid(n) for n
                                                                                                    in
                                                                                                    range(1, 10)]
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
                    if self.get_value(coordinate) == ".":
                        all_subs = self.get_row_col_sub(coordinate)
                        cant_be = [i for i in sum(all_subs, []) if i != "."]
                        all_nums = ["1", "2", "3",
                                    "4", "5", "6",
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


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """Version B"""

        ans = Solution.PySudokuSolver_B(board)
        ans.solve()
        for coor, value in ans.hash_board.items():
            x, y = coor[0], coor[1]
            board[9 - y][x - 1] = value["cur"]

    class PySudokuSolver_B:
        """
        来自ZZZProject/SudokuSolver/sudoku_solver_v1
        改动:
        把空位从"0"改成"."以符合本体要求
        删去__str__, 对解本题没有帮助

        each instance should be a single plate that can be filled in with numbers
        there will be check method to ensure no conflict in going on.
        there will also be an final examination method to ensure when every empty slot is filled.
        the key is in the solve function, where the algorithm is in, to find the answer
        """

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
            只支持str的raw data, 空白处用"."来表示 (符合Leetcode p037)

            这里用哈希表实现算法, 基本原理:
            棋盘本身不变 self.board, 只有最终出解了才变化棋盘
            用哈希表来做推理 self.hastable

            创建一个哈希表 self.pool 记录当前牌池状况
            建造一个哈希表 self.history 来记录操作/推理的过程
            """

            self.blank = "."
            self.valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

            # 保留原puzzle, 用于print
            self.board = puzzle

            # 数据推理方式用哈希表实现
            # self.pool = {card:9 for card in self.valid}

            self.hash_board = {
                coor: {"cur": self.blank, "possible": []}
                for coor in [(x, y) for x in range(1, 10) for y in range(1, 10)]
            }

            self.load_quiz()  # 装载题目

            # 初始化一个历史记录, 备分操作过程, 使用list
            self.guess_history = []
            self.deduct_history = []

        # 读题
        def load_quiz(self):
            for coor, value in self.hash_board.items():
                x, y = coor[0], coor[1]
                given = self.board[9 - y][x - 1]
                if given in self.valid:
                    value["cur"] = given

        # define some verification method
        def cur_value(self, coor):
            """return the current value in hash_board"""
            return self.hash_board[coor]["cur"]

        # Define moves to add numbers to the board
        def insert(self, coor, value):
            """to insert a value into the checkerboard
            for convenience, indext start from 1, and act like coordinates
            """
            self.hash_board[coor]["cur"] = value

        # 基础设施, 判断行列
        def row(self, n):
            """返回一个行的值"""
            return [self.hash_board[coor]["cur"] for coor in self.hash_board if coor[1] == n]

        def col(self, n):
            """返回一个列的值"""
            return [self.hash_board[coor]["cur"] for coor in self.hash_board if coor[0] == n]

        def grid(self, n):
            """output a grid of 3*3 in the checkboard
            n: int 1-9

            The grid index on the checkerboad will be:
            1 2 3
            4 5 6
            7 8 9

            return: a list of numbers extracted from the grid
            """
            g1 = [self.hash_board[(x, y)]["cur"] for y in range(7, 10) for x in range(1, 4)]
            g2 = [self.hash_board[(x, y)]["cur"] for y in range(7, 10) for x in range(4, 7)]
            g3 = [self.hash_board[(x, y)]["cur"] for y in range(7, 10) for x in range(7, 10)]
            g4 = [self.hash_board[(x, y)]["cur"] for y in range(4, 7) for x in range(1, 4)]
            g5 = [self.hash_board[(x, y)]["cur"] for y in range(4, 7) for x in range(4, 7)]
            g6 = [self.hash_board[(x, y)]["cur"] for y in range(4, 7) for x in range(7, 10)]
            g7 = [self.hash_board[(x, y)]["cur"] for y in range(1, 4) for x in range(1, 4)]
            g8 = [self.hash_board[(x, y)]["cur"] for y in range(1, 4) for x in range(4, 7)]
            g9 = [self.hash_board[(x, y)]["cur"] for y in range(1, 4) for x in range(7, 10)]
            grids = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
            return grids[n - 1]

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
            return row_at, col_at, grid_at

        def no_conflict(self):
            """return if there is a conflict in the board, where 2 same number (!=self.blank) showed up:
            in the same row, column or grid

            return True if no conflicts were found
            return False if conflicts were found
            """
            all_subs = [self.row(n) for n in range(1, 10)] + \
                       [self.row(n) for n in range(1, 10)] + \
                       [self.grid(n) for n in range(1, 10)]

            for sub in all_subs:
                check_list = []
                for i in sub:
                    if i != self.blank:
                        if i not in check_list:
                            check_list.append(i)
                        else:
                            return False
            return True

        def all_filled(self):
            """To ensure all the place is filled with a number"""
            for coor, value in self.hash_board.items():
                if value["cur"] == self.blank:
                    return False
            return True

        def isSolved(self):
            """To check if the puzzle is solved"""
            return self.all_filled() and self.no_conflict()

        def analysis(self):
            """return a dict of every vacant coordinate linked to the possible value it can be put in
            the result dict should be in the form of :
            {(x,y): [v1, v2, v3], (x,y): [v1, v2, v3], (x,y): [v1, v2, v3]}
            """
            for coor, value in self.hash_board.items():
                if value["cur"] == self.blank:
                    cant_be = set(sum(self.get_row_col_sub(coor), []))
                    can_be = [i for i in self.valid if i not in cant_be]
                    value["possible"] = can_be

        def feasible(self):
            """return True if all vacant spot can still fill in a possible number"""
            self.analysis()
            for coor, value in self.hash_board.items():
                if value["cur"] == self.blank and value["possible"] == []:
                    return False
            return True

        def direct_deduce(self):
            """To analyze each vacant coordinate, and if there is only one possible value for it
            fill it in with the value on the checkerboard"""
            added = True
            all_deduced = []

            def deduce():
                nonlocal all_deduced, added
                self.analysis()
                coor_operated = []
                for coor, value in self.hash_board.items():
                    if len(value["possible"]) == 1 and value["cur"] == self.blank:
                        self.insert(coor, value["possible"][0])
                        coor_operated.append(coor)
                if not coor_operated:
                    added = False
                else:
                    all_deduced += coor_operated

            while added:
                deduce()
            self.deduct_history.append(all_deduced)

        def best_guess(self):
            """return a coor that has least possible numbers, if cannot deduct"""
            coor_to_move = min(
                self.hash_board,
                key=lambda x: len(self.hash_board[x]["possible"])
                if self.hash_board[x]["cur"] == self.blank else 10
            )
            self.guess_history.append(coor_to_move)
            return coor_to_move

        def hyper_move(self, coor):
            """try to move a hypothsized spot with a possible number
            according to coor, the self.hash_board insert this hyperthetical value
            """
            value = self.hash_board[coor]["possible"].pop()
            self.insert(coor, value)

        def undo(self):
            """according to self.history, undo all the moves in the last step
            this will undo all the direct deducted and the previous guess.
            """
            undo_deducted = self.deduct_history.pop()
            guess_deducted = self.guess_history[-1]
            for coor in undo_deducted:
                self.hash_board[coor]["cur"] = self.blank

            self.hash_board[guess_deducted]["cur"] = self.blank

        def last_guess_availble(self):
            """check if last guess still have possible values"""
            return len(self.hash_board[self.guess_history[-1]]["possible"]) > 0

        # Final solution
        def solve(self):
            """This will solve the problem and fill the self.board with correct answer
            it will then print(self) to show the answer
            """

            while not self.isSolved():
                self.direct_deduce()

                if self.isSolved():
                    break

                elif self.feasible() and not self.all_filled():
                    best_coor = self.best_guess()
                    self.hyper_move(best_coor)

                else:
                    while True:
                        self.undo()
                        if self.last_guess_availble():
                            break
                        else:
                            self.guess_history.pop()
                    self.hyper_move(self.guess_history[-1])



if __name__ == "__main__":
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
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ], "question 1"

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
    ], "question 2"

    print("all passed")
