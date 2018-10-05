# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """

    all_spots = []

    def __init__(self, empty=[
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]):
        """
        An empty checkerboard -
        the structure should be a nested list of 10 lists where each list contain 10 spot, default to filled with 0

        When initiated:
        The empty checkerboard is skipped by directly loading a pre-written board with numbers on.
        The pre-written board follows the same structure as a nested list like empty.
        """
        self.board = empty

        print('A chess is generated:')
        print(self)
        print('\n')

    def __str__(self):
        """to just print the current checker board
        also add a coordinate axis for easier read
        """

        to_print = ''
        y_num = 8
        separ = '    ----------------------'
        x_num = '    1, 2, 3, 4, 5, 6, 7, 8'


        for i in self.board:
            row = str(i)
            to_print += str(y_num) + '  ' + row + '\n'
            y_num -= 1

        to_print += separ + '\n' + x_num
        return to_print


    def put(self, coor):




if __name__ == '__main__':
    t = Chessboard()

