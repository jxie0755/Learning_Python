# This is to build a solver for any valid sudoku quiz
# This should be setup as a OOP method.

# question from https://www.websudoku.com/
# It also allows to verify answer


class Sudoku(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """


    def __init__(self, puzzle=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]):
        """
        An empty checkerboard -
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0

        When initiated:
        The empty checkerboard is skipped by directly loading a pre-written board with numbers on.
        The pre-written board follows the same structure as a nested list like empty.
        """
        self.board = puzzle

        print('puzzle is generated:')
        print(self)
        print('\n')

        # Also create a permanent puzzle copy for future use
        self.puzzle = self.board_mem()

    def __str__(self):
        """to just print the current checker board
        also add a coordinate axis for easier read
        """

        to_print = ''
        y_num = 9
        x_num = '   1, 2, 3, 4, 5, 6, 7, 8, 9'

        for i in self.board:
            to_print += str(y_num) + ' ' + str(i) + '\n'
            y_num -= 1

        to_print += x_num
        return to_print


    # Build up class attributes to for future to check up the rows, columns and grids.
    def row(self, n):
        """output a row of numbers
        n: int 1-9
        return: a list of numbers extracted from the row
        """
        self.rows = self.board[:] # make a copy
        return self.rows[9-n]

    def col(self, n):
        """output a column of numbers
        n: int 1-9
        return: a list of numbers extracted from the column
        """
        self.columns = [[self.board[i][j] for i in range(9)] for j in range(9)]
        return self.columns[n-1]

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
        return self.grids[n-1]

    # Define moves to add numbers to the board
    def insert(self, x, y, value):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        assert 1 <= value <= 9 and type(value) == int
        self.board[9-y][x-1] = value

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
        return self.board[9-coor[1]][coor[0]-1]

    def get_row_col_sub(self, coor):
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
        return [row_at, col_at, grid_at]

    def no_conflict(self):
        """return if there is a conflict in the board, where 2 same number (!=0) showed up:
        in the same row, column or grid

        return True if no conflicts were found
        return False if conflicts were found
        """
        all_subs = [self.row(n) for n in range(1,10)] + [self.row(n) for n in range(1,10)] + [self.grid(n) for n in range(1,10)]
        for sub in all_subs:
            check_list = []
            for i in sub:
                if i != 0:
                    if i not in check_list:
                        check_list.append(i)
                    else:
                        return False
        return True

    def all_filled(self):
        """To ensure all the place is filled with a number"""
        return all(all(j != 0 for j in i) for i in self.board)


    def valid_solution(self):
        """To check if the puzzle is solved"""
        print('The answer is:')
        return self.all_filled() and self.no_conflict()


    def analysis(self):
        """return a dict of every vacant coordinate linked to the possible value it can be put in"""
        result = {}
        for x in range(1,10):
            for y in range(1,10):
                coordinate = (x, y)
                if self.get_value(coordinate) == 0:
                    all_subs = self.get_row_col_sub(coordinate)
                    cant_be = [i for i in sum(all_subs, []) if i != 0]
                    all_nums = list(range(1,10))
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
        return True




    # def solve(self):

    #     snapshot_board = []
    #     snapshot_to_do = []

    #     while not self.valid_solution():

    #         self.direct_deduce()
    #         situation = self.analysis()

    #         if self.feasible(situation):
    #             attemp_move = self.hypothesize(situation)
    #             for i in range(len(attemp_move)-1):
    #                 snapshot_board.append(self.board_mem())
    #             snapshot_to_do.append(attemp_move)
    #             self.hyper_move(snapshot_to_do)

    #         else:
    #             self.board = snapshot_board.pop()
    #             self.hyper_move(snapshot_to_do)













if __name__ == '__main__':
    # list out 4 problems for test case

    # websudoku easy puzzle 10
    easy_data =[
        [0,1,0,0,6,0,0,9,0],
        [9,0,5,1,0,0,0,0,0],
        [0,4,8,7,0,9,6,0,0],
        [0,7,6,0,8,0,1,5,0],
        [8,0,0,0,0,0,0,0,7],
        [0,5,3,0,4,0,2,6,0],
        [0,0,4,8,0,5,9,2,0],
        [0,0,0,0,0,4,7,0,5],
        [0,9,0,0,3,0,0,8,0],
    ]

    # websudoku medium puzzle 10
    medium_data = [
        [5,0,2,1,8,0,0,0,0],
        [9,1,0,0,5,0,2,0,0],
        [0,4,6,0,0,2,0,0,1],
        [0,0,0,2,0,1,0,0,8],
        [0,0,1,0,0,0,4,0,0],
        [4,0,0,3,0,9,0,0,0],
        [1,0,0,7,0,0,8,5,0],
        [0,0,9,0,1,0,0,7,4],
        [0,0,0,0,2,8,9,0,6],
    ]

     # websudoku hard puzzle 10
    hard_data = [
        [0,0,0,3,7,0,0,0,5],
        [8,0,0,0,5,1,3,0,0],
        [0,5,0,0,0,0,0,6,2],
        [9,4,0,0,0,0,0,0,0],
        [0,0,0,7,0,8,0,0,0],
        [0,0,0,0,0,0,0,5,4],
        [1,6,0,0,0,0,0,4,0],
        [0,0,3,1,2,0,0,0,7],
        [5,0,0,0,6,4,0,0,0],
    ]

     # websudoku evil puzzle 10
    evil_data = [
        [0,0,0,0,5,0,0,9,0],
        [0,5,0,6,8,0,0,0,0],
        [9,3,7,0,0,0,0,0,0],
        [2,0,0,0,0,0,5,0,0],
        [0,9,0,7,0,2,0,8,0],
        [0,0,6,0,0,0,0,0,4],
        [0,0,0,0,0,0,2,3,6],
        [0,0,0,0,4,3,0,5,0],
        [0,1,0,0,9,0,0,0,0],
    ]


    easy = Sudoku(easy_data)
    # medium = Sudoku(medium_data)
    # hard = Sudoku(hard_data)
    # evil = Sudoku(evil_data)

    a = easy.analysis()
    for key, value in a.items():
        if len(value) == 1:
            print(key, value)


    # easy.direct_deduce()
    # print(easy)
    # print(easy.valid_solution())
