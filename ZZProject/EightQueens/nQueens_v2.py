# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """

    def __init__(self, n):
        """
        An empty checkerboard -
        the structure should be a nested list of n lists where each list contain n spots, default to filled with 0
        """
        self.board = []
        self.size = n
        for i in range(n):
            self.board.append([0]*n)


    def __str__(self):
        """to just print the current checker board
        also add a coordinate axis for easier read
        """

        to_print = ''
        y_num = self.size  # 根据棋盘大小输出
        nums = str(list(range(1,self.size+1)))[1:-1]
        x_num = '    ' + nums
        separ = '    ' + len(nums) * '-'

        for i in self.board:
            row = str(i)
            to_print += str(y_num) + '  ' + row + '\n'
            y_num -= 1

        to_print += separ + '\n' + x_num
        return to_print

    # Basic set and get
    def insert(self, coor):
        """to insert a value into the checkerboard
        for convenience, indext start from 1, and act like coordinates
        """
        x, y = coor[0], coor[1]
        self.board[self.size-y][x-1] = 1

    def get(self, coor):
        """obtain the value at a coor"""
        return self.board[self.size-coor[1]][coor[0]-1]

    # define obtaining the coor list of each row or column
    def row_coor(self, n):
        """output a list of coor of row n starting from 1 at the bottom"""
        y = n
        row_coor_list = [(i, y) for i in range(1, self.size+1)]
        return row_coor_list

    def col_coor(self, n):
        """output a list of cross of coor in the direction of row"""
        x = n
        col_coor_list = [(x, i) for i in range(1, self.size+1)]
        return col_coor_list



if __name__ == '__main__':
    t = Chessboard(5)
    print(t)
    # show empty board n*n filled with 0

    t.insert((1,1))
    print(t)
    # show 1 at the location (1,1)

    print(t.get((1,1)))
    # >>> 1

    print(t.row_coor(1))
    # >>> [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]

    print(t.col_coor(1))
    # >>> [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

