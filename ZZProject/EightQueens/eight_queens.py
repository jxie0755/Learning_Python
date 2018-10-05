# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """

    all_spots = [(x, y) for x in range(1, 9) for y in range(1, 9)]

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
        the structure should be a nested list of 8 lists where each list contain 8 spots, default to filled with 0
        """
        self.board = empty

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

    # Basic get and set
    def insert(self, coor):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        x, y = coor[0], coor[1]
        self.board[8-y][x-1] = 1

    def get(self, coor):
        """obtain the value at a coor"""
        return self.board[8-coor[1]][coor[0]-1]


    # Generate coor list
    def row_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        cross_list = [(i, y) for i in range(1, 9)]
        return cross_list

    def col_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        cross_list = [(x, i) for i in range(1, 9)]
        return cross_list

    def cross_coor_1(self, coor): # of \ cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_list = [coor]
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] < 8:
            x, y = before[0], before[1]
            before = (x-1, y+1)
            cross_list = [before] + cross_list

        while after[0] < 8 and after[1] > 1:
            x, y = after[0], after[1]
            after = (x+1, y-1)
            cross_list = cross_list + [after]

        return cross_list

    def cross_coor_2(self, coor): # # of / cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_list = [coor]
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] > 1:
            x, y = before[0], before[1]
            before = (x-1, y-1)
            cross_list = [before] + cross_list

        while after[0] < 8 and after[1] < 8:
            x, y = after[0], after[1]
            after = (x+1, y+1)
            cross_list = cross_list + [after]

        return cross_list


    # Build up class attributes to for future to check up the rows, columns and grids.
    def row(self, coor):
        """"return: a list of numbers extracted from the row"""
        return [t.get(i) for i in t.row_coor(coor)]

    def col(self, coor):
        """return: a list of numbers extracted from the column"""
        return [t.get(i) for i in t.col_coor(coor)]

    def cross_1(self, coor):
        """return: a list of numbers extracted \ cross of coor"""
        return [t.get(i) for i in t.cross_coor_1(coor)]

    def cross_2(self, coor):
        """return: a list of numbers extracted from / cross of coor"""
        return [t.get(i) for i in t.cross_coor_2(coor)]



if __name__ == '__main__':
