"""
This is to build a solver for any valid sudoku quiz
This should be setup as a OOP method.

question from https://www.websudoku.com/
It also allows to verify answer

We assume all raw data coming in the form of both str and int just like v2
In this version, the algorithm will be changed, hash table will be used.
"""

class Sudoku(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """

    def __init__(self, puzzle):
        """
        只支持str的raw data, 空白处用"."来表示 (符合Leetcode p037)

        这里用哈希表实现算法, 基本原理:
        棋盘本身不变 self.board, 只有最终出解了才变化棋盘
        用哈希表来做推理 self.hastable

        创建一个哈希表 self.pool 记录当前牌池状况
        建造一个哈希表 self.history 来记录操作/推理的过程
        """

        self.blank = "0"
        self.valid = ["1", "2", "3", "4", "5","6", "7", "8", "9"]

        # 保留原puzzle, 用于print
        self.board = puzzle

        # 数据推理方式用哈希表实现
        # self.pool = {card:9 for card in self.valid}

        self.hash_board = {
            coor: {"cur": [self.blank], "possible": [], "tried":[]}
            for coor in [(x, y) for x in range(1, 10) for y in range(1, 10)]
        }

        self.load_quiz()  # 装载题目


        # 初始化一个历史记录, 备分操作过程, 使用list
        self.guess_history = []
        self.deduct_history = []

        # 统计
        self.count = 0
        self.guess = 0
        self.guess_layer = []

        # 打印题目
        print("puzzle is generated:")
        print(self)
        print("")

    # 用于格式化的打印题目和题解
    def __str__(self):
        """to just print the current checker board
        also add a coordinate axis for easier read
        """

        def process_raw(row):
            x = "|"
            for i in row:
                if i not in self.valid:
                    x += "."
                else:
                    x += str(i)
                x += "  "

            return x[0:9] + "  " + x[9:18] + "  " + x[18:]

        to_print = ""
        y_num = 9
        separ = "    -----------------------------"
        x_num = "    1  2  3    4  5  6    7  8  9"

        for i in self.board:
            str_row = process_raw(i)
            to_print += str(y_num) + "  " + str_row + "\n"
            if y_num in [7, 4]:
                to_print += "\n"
            y_num -= 1

        to_print += separ + "\n" + x_num
        return to_print


    # 读题
    def load_quiz(self):
        for coor, value in self.hash_board.items():
            x, y = coor[0], coor[1]
            given = self.board[9-y][x-1]
            if given in self.valid:
                value["cur"][0] = given

    # define some verification method
    def cur_value(self, coor):
        """return the current value in hash_board"""
        return self.hash_board[coor]["cur"][0]

    # Define moves to add numbers to the board
    def insert(self, coor, value):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        self.hash_board[coor]["cur"][0] = value
        self.count += 1

    # 基础设施, 判断行列
    def row(self, n):
        """返回一个行的值"""
        return [self.hash_board[coor]["cur"][0] for coor in self.hash_board if coor[1] == n]

    def col(self, n):
        """返回一个列的值"""
        return [self.hash_board[coor]["cur"][0] for coor in self.hash_board if coor[0] == n]

    def grid(self, n):
        """output a grid of 3*3 in the checkboard
        n: int 1-9

        The grid index on the checkerboad will be:
        1 2 3
        4 5 6
        7 8 9

        return: a list of numbers extracted from the grid
        """
        grid_dict = {
            1: [7, 10, 1, 4],
            2: [7, 10, 4, 7],
            3: [7, 10, 7, 10],
            4: [4, 7, 1, 4],
            5: [4, 7, 4, 7],
            6: [4, 7, 7, 10],
            7: [1, 4, 1, 4],
            8: [1, 4, 4, 7],
            9: [1, 4, 7, 10],
        }

        a, b, c, d = grid_dict[n][0], grid_dict[n][1], grid_dict[n][2], grid_dict[n][3]
        grid = []
        for y in range(a, b):
            for x in range(c, d):
                grid.append(self.hash_board[(x, y)]["cur"][0])
        return grid

    def get_row_col_grid(self, coor):
        """return a list of 3 list, that contains the related row, column and sub grid of that coor
        """
        row_at = self.row(coor[1])
        col_at = self.col(coor[0])

        if coor[0] in [1,2,3]:
            if coor[1] in [1,2,3]:
                n = 7
            elif coor[1] in [4,5,6]:
                n = 4
            elif coor[1] in [7,8,9]:
                n = 1

        elif coor[0] in [4,5,6]:
            if coor[1] in [1,2,3]:
                n = 8
            elif coor[1] in [4,5,6]:
                n = 5
            elif coor[1] in [7,8,9]:
                n = 2

        elif coor[0] in [7,8,9]:
            if coor[1] in [1,2,3]:
                n = 9
            elif coor[1] in [4,5,6]:
                n = 6
            elif coor[1] in [7,8,9]:
                n = 3

        grid_at = self.grid(n)
        return list(set(sum([row_at, col_at, grid_at], [])))


    def no_conflict(self):
        """return if there is a conflict in the board, where 2 same number (!=self.blank) showed up:
        in the same row, column or grid

        return True if no conflicts were found
        return False if conflicts were found
        """
        all_subs = [self.row(n) for n in range(1,10)] + \
                   [self.row(n) for n in range(1,10)] + \
                   [self.grid(n) for n in range(1,10)]

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
            if value["cur"][0] == self.blank:
                return False
        return True

    def isSolved(self):
        """To check if the puzzle is solved"""
        return self.all_filled() and self.no_conflict()

    def analysis(self):
        """update the hashboard value on dict["possible"] for every coor"""
        for coor, value in self.hash_board.items():
            if value["cur"][0] == self.blank:
                cant_be = self.get_row_col_grid(coor)
                can_be = [i for i in self.valid if i not in cant_be]
                value["possible"] = can_be


    def feasible(self):
        """return True if all vacant spot can still fill in a possible number"""
        self.analysis()
        for coor, value in self.hash_board.items():
            if value["cur"][0] == self.blank and value["possible"] == []:
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
                if len(value["possible"]) == 1 and value["cur"][0] ==self.blank:
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
            if self.hash_board[x]["cur"][0] == self.blank else 10
        )
        self.guess_history.append(coor_to_move)
        return coor_to_move

    def hyper_move(self, coor):
        """try to move a hypothsized spot with a possible number
        according to coor, the self.hash_board insert this hyperthetical value
        """
        value = self.hash_board[coor]["possible"].pop()
        self.hash_board[coor]["tried"].append(value)
        self.insert(coor, value)
        self.guess += 1


    def undo(self):
        """according to self.history, undo all the moves in the last step
        this will undo all the direct deducted and the previous guess.
        """
        undo_deducted = self.deduct_history.pop()
        guess_deducted = self.guess_history[-1]
        for coor in undo_deducted:
            self.hash_board[coor]["cur"][0] = self.blank

        self.hash_board[guess_deducted]["cur"][0] = self.blank


    def last_guess_availble(self):
        """check if last guess still have possible values"""
        return len(self.hash_board[self.guess_history[-1]]["possible"]) > 0

    def print_translate(self):
        for coor, value in self.hash_board.items():
            x, y = coor[0], coor[1]
            self.board[9 - y][x - 1] = value["cur"][0]
        print(self)


    # Final solution
    def solve(self):
        """This will solve the problem and fill the self.board with correct answer
        it will then print(self) to show the answer
        """
        layer = 0

        while not self.isSolved():
            self.direct_deduce()

            if self.isSolved():
                break

            elif self.feasible() and not self.all_filled():
                best_coor = self.best_guess()
                self.hyper_move(best_coor)
                layer += 1

            else:
                while True:
                    self.undo()
                    if self.last_guess_availble():
                        break
                    else:
                        self.guess_history.pop()
                        self.guess_layer.append(layer)
                        layer -= 1
                self.hyper_move(self.guess_history[-1])

        print("problem solved!")


    def show_answer(self):
        print("The answer is: ")
        self.print_translate()
        print("\n")

    def show_statistics(self):
        print("total filled: ", self.count)
        print("total guess: ", self.guess)
        print("maximum layer", max(self.guess_layer))
        print()

    def single_step_solve(self):
        """This will solve the problem and fill the self.board with correct answer
        it will then print(self) to show the answer
        """
        # for i in q.guess_history:
        #     print(i, q.hash_board[i])

        self.direct_deduce()

        if not self.isSolved():

            if self.feasible() and not self.all_filled():
                best_coor = self.best_guess()
                self.hyper_move(best_coor)
                # print("New COOR")
            else:
                while True:
                    self.undo()
                    if self.last_guess_availble():
                        break
                    else:
                        self.guess_history.pop()
                self.hyper_move(self.guess_history[-1])

        print("problem solved!")


if __name__ == "__main__":
    # websudoku hard puzzle 10
    hard_data_10_str = [
        ["0", "0", "0", "3", "7", "0", "0", "0", "5"],
        ["8", "0", "0", "0", "5", "1", "3", "0", "0"],
        ["0", "5", "0", "0", "0", "0", "0", "6", "2"],
        ["9", "4", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "7", "0", "8", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "5", "4"],
        ["1", "6", "0", "0", "0", "0", "0", "4", "0"],
        ["0", "0", "3", "1", "2", "0", "0", "0", "7"],
        ["5", "0", "0", "0", "6", "4", "0", "0", "0"],
    ]

    q = Sudoku(hard_data_10_str)
    q.solve()
    q.show_answer()


    # problem solved!
    # 9  |6  9  1    3  7  2    4  8  5
    # 8  |8  2  4    6  5  1    3  7  9
    # 7  |3  5  7    4  8  9    1  6  2
    #
    # 6  |9  4  8    5  1  6    7  2  3
    # 5  |2  3  5    7  4  8    9  1  6
    # 4  |7  1  6    2  9  3    8  5  4
    #
    # 3  |1  6  2    9  3  7    5  4  8
    # 2  |4  8  3    1  2  5    6  9  7
    # 1  |5  7  9    8  6  4    2  3  1
    #     -----------------------------
    #     1  2  3    4  5  6    7  8  9
    # Total hypothesis:  17
    # max_layer_counted: 4

    import time
    ultimate_puzzle_str_3 = [
        ["8", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "3", "6", "0", "0", "0", "0", "0"],
        ["0", "7", "0", "0", "9", "0", "2", "0", "0"],
        ["0", "5", "0", "0", "0", "7", "0", "0", "0"],
        ["0", "0", "0", "0", "4", "5", "7", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "3", "0"],
        ["0", "0", "1", "0", "0", "0", "0", "6", "8"],
        ["0", "0", "8", "5", "0", "0", "0", "1", "0"],
        ["0", "9", "0", "0", "0", "0", "4", "0", "0"],
    ]

    ultimate_sudoku_3 = Sudoku(ultimate_puzzle_str_3)
    start_time = time.time()
    ultimate_sudoku_3.solve()
    ultimate_sudoku_3.show_statistics()
    print(f"--- {time.time() - start_time}s seconds ---\n")

    # for i in ultimate_sudoku_3.guess_history:
    #     print(i, "TRIED: ",  ultimate_sudoku_3.hash_board[i]["cur"][0])

    # 简化版, 把guess数字添加以后, 不需要任何推理就可以完成
    ultimate_puzzle_str_3b = [
        ["8", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "4", "3", "6", "0", "0", "0", "0", "0"],
        ["6", "7", "0", "0", "9", "0", "2", "0", "0"],
        ["0", "5", "0", "0", "0", "7", "0", "0", "0"],
        ["3", "0", "0", "0", "4", "5", "7", "0", "0"],
        ["2", "8", "0", "1", "0", "0", "0", "3", "0"],
        ["5", "2", "1", "0", "0", "0", "3", "6", "8"],
        ["0", "0", "8", "5", "0", "0", "9", "1", "0"],
        ["7", "9", "0", "0", "0", "0", "4", "0", "0"]]

    ultimate_sudoku_3b = Sudoku(ultimate_puzzle_str_3b)
    ultimate_sudoku_3b.direct_deduce()
    print(ultimate_sudoku_3b.isSolved())
