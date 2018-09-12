# This is to build a solver for any valid sudoku quiz
# This should be setup as a OOP method.

class Sudoku(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """
    def __init__(self):
        """generate an empty checkerboard
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0
        """
        line, board = [0] * 9, []
        for i in range(9):
            board.append(line[:])
        self.board = board
        print('Welcome to Sudoku Solver! a checkerboard is generated:')
        print(str(self) + '\n')


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
        self.board[9-x][y-1] = value



if __name__ == '__main__':
    a = Sudoku()
