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

    # Build up class attributes to for future to check up the rows, columns and grids.
    def row(self, n):
        """output a row of numbers
        n: int 1-9
        return: a list of numbers extracted from the row
        """
        self.rows = self.board[:] # make a copy
        return self.rows[n-1]

    def col(self, n):
        """output a column of numbers
        n: int 1-9
        return: a list of numbers extracted from the row
        """
        self.columns = [[self.board[i][j] for i in range(9)] for j in range(9)]
        return self.columns[n-1]

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

    def insert(self, x, y, value):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        assert 1 <= value <= 9 and type(value) == int
        self.board[9-y][x-1] = value

if __name__ == '__main__':
    # list out 4 problems for test case

    # websudoku easy puzzle 10
    easy_data = [
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
                   (1,9,5), (3,9,2), (4,9,1), (5,9,8),
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
    medium = Sudoku(medium_data)
    hard = Sudoku(hard_data)
    evil = Sudoku(evil_data)

    print(evil.col(8))
    evil.insert(8,1,3)
    print(evil.col(8))

