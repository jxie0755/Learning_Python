# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.



class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """
    spots_taken = []

    def __init__(self, n):
        """
        An empty checkerboard -
        the structure should be a nested list of n lists where each list contain n spots, default to filled with 0
        """
        self.size = n
        self.board = []
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
        self.spots_taken.append(coor)

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
        """output a list of coor of column n from 1 at the left"""
        x = n
        col_coor_list = [(x, i) for i in range(1, self.size+1)]
        return col_coor_list

    def cross_coor_1(self, coor): # of \ cross
        """output a list of cross of coor in the direction of \\"""
        x, y = coor[0], coor[1]
        cross_coor_list = [coor]
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] < self.size:
            x, y = before[0], before[1]
            before = (x-1, y+1)
            cross_coor_list = [before] + cross_coor_list

        while after[0] < self.size and after[1] > 1:
            x, y = after[0], after[1]
            after = (x+1, y-1)
            cross_coor_list = cross_coor_list + [after]

        return cross_coor_list

    def cross_coor_2(self, coor): # # of / cross
        """output a list of cross of coor in the direction of //"""
        x, y = coor[0], coor[1]
        cross_coor_list = [coor]
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] > 1:
            x, y = before[0], before[1]
            before = (x-1, y-1)
            cross_coor_list = [before] + cross_coor_list

        while after[0] < self.size and after[1] < self.size:
            x, y = after[0], after[1]
            after = (x+1, y+1)
            cross_coor_list = cross_coor_list + [after]

        return cross_coor_list

    # analyze the chessboard, and generates a list of available coor that can still put queens
    def check_coor(self, coor):
        """return a list of coors that can not be put with queens"""
        row_coor_list = self.row_coor(coor[1])
        col_coor_list = self.col_coor(coor[0])
        cross_coor_list_1 = self.cross_coor_1(coor)
        cross_coor_list_2 = self.cross_coor_2(coor)
        all_non_available = set(row_coor_list + col_coor_list + cross_coor_list_1 + cross_coor_list_2)
        return all_non_available

    def analysis(self):
        """return a list of the available list after checking all the coor in self.spots_taken"""
        all_availble = [(x, y) for x in range(1, self.size+1) for y in range(1, self.size+1)]
        for coor in self.spots_taken:
            to_remove = self.check_coor(coor)
            for r_coor in to_remove:
                if r_coor in all_availble:
                    all_availble.remove(r_coor)
        return all_availble

    def queen_solve(self):
        N = 0
        while N != self.size:
            N += 1
            available_spots = self.analysis()
            for coor in self.row_coor(N):
                pass
    # TODO


if __name__ == '__main__':
    t = Chessboard(5)
    print(t)
    # show empty board n*n filled with 0

    t.insert((2,2))
    print(t)
    # show 1 at the location (1,1)

    print(t.get((2,2)))
    # >>> 1

    print(t.row_coor(2))
    # >>> [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]

    print(t.col_coor(2))
    # >>> [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]

    print(len(t.check_coor((2,2))))  # >>> 15, non_availble spots find
    print(len(t.analysis()))         # >>> 10, give 10 availble after removing 15 from 25


