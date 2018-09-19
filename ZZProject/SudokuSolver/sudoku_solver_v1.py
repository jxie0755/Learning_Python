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


    def __init__(self, puzzle=[]):
        """
        First:
        generate an empty checkerboard
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0

        Then:
        generate the problem by filling the known numbers at different location
        puzzle: a list of tuples, each tuple in the form of (x, y, value)
        mutate the checkerboard to become the board with the problem loaded
        """
        line, board = [0] * 9, []
        for i in range(9):
            board.append(line[:])
        self.board = board

        for data in puzzle:
            self.insert(data[0], data[1], data[2])
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

    def direct_deduce(self):
        """To analyze each vacant coordinate, and if there is only one possible value for it
        fill it in with the value on the checkerboard"""

        def deduce():
            to_be_filled = []
            for x in range(1,10):
                for y in range(1,10):
                    coordinate = (x, y)
                    if self.get_value(coordinate) == 0:
                        all_subs = self.get_row_col_sub(coordinate)
                        cant_be = [i for i in sum(all_subs, []) if i != 0]
                        all_nums = list(range(1,10))
                        can_be = [i for i in all_nums if i not in cant_be]
                        if len(can_be) == 1:
                            to_be_filled.append((coordinate, can_be[0]))
            return to_be_filled

        to_fill = deduce()
        while to_fill:
            for coor, value in to_fill:
                self.insert(coor[0], coor[1], value)
            to_fill = deduce()


if __name__ == '__main__':
    # list out 4 problems for test case

    # websudoku easy puzzle 10
    easy_data =[
        (2,1,9), (5,1,3), (8,1,8),
        (6,2,4), (7,2,7), (9,2,5),
        (3,3,4), (4,3,8), (6,3,5), (7,3,9), (8,3,2),
        (2,4,5), (3,4,3), (5,4,4), (7,4,2), (8,4,6),
        (1,5,8), (9,5,7),
        (2,6,7), (3,6,6), (5,6,8), (7,6,1), (8,6,5),
        (2,7,4), (3,7,8), (4,7,7), (6,7,9), (7,7,6),
        (1,8,9), (3,8,5), (4,8,1),
        (2,9,1), (5,9,6), (8,9,9),
    ]

    # websudoku medium puzzle 10
    medium_data = [
        (5,1,2), (6,1,8), (7,1,9), (9,1,6),
        (3,2,9), (5,2,1), (8,2,7), (9,2,4),
        (1,3,1), (4,3,7), (7,3,8), (8,3,5),
        (1,4,4), (4,4,3), (6,4,9),
        (3,5,1), (7,5,4),
        (4,6,2), (6,6,1), (9,6,8),
        (2,7,4), (3,7,6), (6,7,2), (9,7,1),
        (1,8,9), (2,8,1), (5,8,5), (7,8,2),
        (1,9,5), (3,9,2), (4,9,1), (5,9,8)
    ]

     # websudoku hard puzzle 10
    hard_data = [
        (1,1,5), (5,1,6), (6,1,4),
        (3,2,3), (4,2,1), (5,2,2), (9,2,7),
        (1,3,1), (2,3,6), (8,3,4),
        (8,4,5), (9,4,4),
        (4,5,7), (6,5,8),
        (1,6,9), (2,6,4),
        (2,7,5), (8,7,6), (9,7,2),
        (1,8,8), (5,8,5), (6,8,1), (7,8,3),
        (4,9,3), (5,9,7), (9,9,5),
    ]

     # websudoku evil puzzle 10
    evil_data = [
        (2,1,1), (5,1,9),
        (5,2,4), (6,2,3), (8,2,5),
        (7,3,2), (8,3,3), (9,3,6),
        (3,4,6), (9,4,4),
        (2,5,9), (4,5,7), (6,5,2), (8,5,8),
        (1,6,2), (7,6,5),
        (1,7,9), (2,7,3), (3,7,7),
        (2,8,5), (4,8,6), (5,8,8),
        (5,9,5), (8,9,9),
    ]


    easy = Sudoku(easy_data)
    # medium = Sudoku(medium_data)
    # hard = Sudoku(hard_data)
    # evil = Sudoku(evil_data)

    easy.direct_deduce()
    print(easy)

    print(easy.valid_solution())


