# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.

from copy import deepcopy

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
        assert n > 1, 'n must be larger than 1'
        self.size = n
        self.board = []
        for i in range(n):
            self.board.append([0]*n)

        self.all_available = [[], ]
        for i in range(1, self.size + 1):
            self.all_available.append(self.row_coor(i))

        self.all_available_0 = deepcopy(self.all_available)

        self.spots_taken = []
        self.row1 = self.row_coor(1)

        self.snapshot = []
        self.result = []



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

    def un_insert(self, coor):
        x, y = coor[0], coor[1]
        self.board[self.size - y][x - 1] = 0

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
        # no need for row_coor as we won't check this row again
        col_coor_list = self.col_coor(coor[0])
        cross_coor_list_1 = self.cross_coor_1(coor)
        cross_coor_list_2 = self.cross_coor_2(coor)
        non_available = set(col_coor_list + cross_coor_list_1 + cross_coor_list_2)
        return non_available

    # def spots_taken(self):
    #     """
    #     To generate the list of coors available to put.
    #     Returns: a list of coor in the form of [(x1, y1), (x2, y2), ...]
    #     """
    #     result = []
    #     for coor in [(x, y) for x in range(1, self.size+1) for y in range(1, self.size+1)]:
    #         x, y = coor[0], coor[1]
    #         if self.board[self.size-y][x-1] == 1:
    #             result.append(coor)
    #     return result

    def analysis(self, coor):
        """
        Imperfect function:
        according to the new spot on the chessboard, analysis the available spots in the board
        Returns: None, just to update the self.all_available
        """

        all_to_remove = self.check_coor(coor)

        for coor_tr in all_to_remove:
            y = coor_tr[1]
            if coor_tr in self.all_available[y]:
                self.all_available[y].remove(coor_tr)

    def queen_solve(self, level=1):

        if level == 1:
            if self.row1:
                check_coor = self.row1.pop(0)
                self.insert(check_coor)
                self.snapshot.append(deepcopy(self.all_available))
                self.analysis(check_coor)
                self.queen_solve(2)
            else:
                print('Analysis finished')

        elif 1 < level < self.size:
            if self.all_available[level]:
                check_coor = self.all_available[level].pop(0)
                self.insert(check_coor)
                self.snapshot.append(deepcopy(self.all_available))
                self.analysis(check_coor)
                self.queen_solve(level+1)
            else:
                self.un_insert(self.spots_taken.pop())
                self.all_available = self.snapshot.pop()
                self.queen_solve(level-1)

        elif level == self.size:
            if self.all_available[level]:
                check_coor = self.all_available[level].pop(0)
                self.insert(check_coor)
                t = Chessboard(self.size)
                t.board = deepcopy(self.board)
                self.result.append(t)
                self.un_insert(self.spots_taken.pop())
            self.un_insert(self.spots_taken.pop())
            self.all_available = self.snapshot.pop()
            self.queen_solve(level-1)


if __name__ == '__main__':
    # Check 4 queens
    t = Chessboard(4)
    t.queen_solve()
    for i in t.result:
        print(i)
    print('Total solution number:', len(t.result))
    # >>> 2

    # Check 5 queens
    t = Chessboard(5)
    t.queen_solve()
    for i in t.result:
        print(i)
    print('Total solution number:', len(t.result))
    # >>> 10

    # Check 6 queens
    t = Chessboard(6)
    t.queen_solve()
    for i in t.result:
        print(i)
    print('Total solution number:', len(t.result))
    # >>> 4
