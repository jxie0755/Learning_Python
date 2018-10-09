# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """

    all_spots = [(x, y) for x in range(1, 9) for y in range(1, 9)]
    available_spots = all_spots[:]
    spots_taken = []
    snapshots = [available_spots[:]]

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
        self.spots_taken.append(coor)
        self.available_spots.remove(coor)

    def un_insert(self, coor):
        x, y = coor[0], coor[1]
        self.board[8-y][x-1] = 0
        self.spots_taken.remove(coor)
        self.available_spots.append(coor)

    def get(self, coor):
        """obtain the value at a coor"""
        return self.board[8-coor[1]][coor[0]-1]


    # Generate coor list
    def row_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        row_coor_list = [(i, y) for i in range(1, 9)]
        row_coor_list.remove(coor)
        return row_coor_list

    def col_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        col_coor_list = [(x, i) for i in range(1, 9)]
        col_coor_list.remove(coor)
        return col_coor_list

    def cross_coor_1(self, coor): # of \ cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_coor_list = []
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] < 8:
            x, y = before[0], before[1]
            before = (x-1, y+1)
            cross_coor_list = [before] + cross_coor_list

        while after[0] < 8 and after[1] > 1:
            x, y = after[0], after[1]
            after = (x+1, y-1)
            cross_coor_list = cross_coor_list + [after]

        return cross_coor_list

    def cross_coor_2(self, coor): # # of / cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_coor_list = []
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] > 1:
            x, y = before[0], before[1]
            before = (x-1, y-1)
            cross_coor_list = [before] + cross_coor_list

        while after[0] < 8 and after[1] < 8:
            x, y = after[0], after[1]
            after = (x+1, y+1)
            cross_coor_list = cross_coor_list + [after]

        return cross_coor_list


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

    def exam(self, coor):
        return [
            self.row(coor),
            self.col(coor),
            self.cross_1(coor),
            self.cross_2(coor),
        ]

    # Analysis function to update the available spot list
    def queen_analysis(self):
        """analysis the checkerboard and return a new list of available spots left"""
        new_available = self.available_spots[:]
        for coor in self.spots_taken:
            coors_to_remove = set(self.row_coor(coor) + self.col_coor(coor)+ self.cross_coor_1(coor) + self.cross_coor_2(coor))
            for coor_r in coors_to_remove:
                if coor_r in new_available:
                    self.available_spots.remove(coor_r)
        self.snapshots.append(new_available)
        return new_available

    def eight_queen_solve(self):
        result = []
        for coor1 in self.all_spots:
            self.insert(coor1)
            if self.queen_analysis():
                for coor2 in self.queen_analysis():
                    self.insert(coor2)
                    if self.queen_analysis():
                        for coor3 in self.queen_analysis():
                            self.insert(coor3)
                            if self.queen_analysis():
                                for coor4 in self.queen_analysis():
                                    self.insert(coor4)
                                    if self.queen_analysis():
                                        for coor5 in self.queen_analysis():
                                            self.insert(coor5)
                                            if self.queen_analysis():
                                                for coor6 in self.queen_analysis():
                                                    self.insert(coor6)
                                                    if self.queen_analysis():
                                                        for coor7 in self.queen_analysis():
                                                            self.insert(coor7)
                                                            if self.queen_analysis():
                                                                for coor8 in self.queen_analysis():
                                                                    self.insert(coor8)
                                                                    result.append(Chessboard(self.board[:]))
                                                                else:
                                                                    self.un_insert(coor8)
                                                    else:
                                                        self.un_insert(coor6)
                                            else:
                                                self.un_insert(coor5)
                                    else:
                                        self.un_insert(coor4)
                            else:
                                self.un_insert(coor3)
                    else:
                        self.un_insert(coor2)
            else:
                self.un_insert(coor1)
        print('done!')



if __name__ == '__main__':
    t = Chessboard()
    t.eight_queen_solve()
