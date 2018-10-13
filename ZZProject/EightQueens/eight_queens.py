# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """
    empty_board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    all_spots = [(x, y) for x in range(1, 9) for y in range(1, 9)]
    available_spots = all_spots[:]
    spots_taken = [0,1,2,3,4,5,6,7]
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

    def un_insert(self, coor):
        x, y = coor[0], coor[1]
        self.board[8-y][x-1] = 0


    def get(self, coor):
        """obtain the value at a coor"""
        return self.board[8-coor[1]][coor[0]-1]


    # Generate coor list
    def row_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        row_coor_list = [(i, y) for i in range(1, 9)]
        return row_coor_list

    def col_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        col_coor_list = [(x, i) for i in range(1, 9)]
        return col_coor_list

    def cross_coor_1(self, coor): # of \ cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_coor_list = [coor]
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
        cross_coor_list = [coor]
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
        all_coors = self.all_spots[:]
        for coor in self.spots_taken:
            if type(coor) == tuple:
                coors_to_remove = set(self.row_coor(coor) + self.col_coor(coor)+ self.cross_coor_1(coor) + self.cross_coor_2(coor))
                for coor_r in coors_to_remove:
                    if coor_r in all_coors:
                        all_coors.remove(coor_r)
        return all_coors

    # def re_evaluate(self):
    #     self.available_spots = self.all_spots
    #     for coor in self.spots_taken:
    #         self.available_spots.remove(coor)
    #         coors_to_remove = set(self.row_coor(coor) + self.col_coor(coor)+ self.cross_coor_1(coor) + self.cross_coor_2(coor))
    #         for coor_r in coors_to_remove:
    #             if coor_r in self.available_spots:
    #                 self.available_spots.remove(coor_r)
    #     return self.available_spots

    def queen_solve(self, n):
        candidates = [self.all_spots[:]] + [[] for i in range(n - 1)]
        result = []

        # this while loop makes sure go over all first coor
        for coor_0 in candidates[0]:
            self.spots_taken[0] = coor_0
            for i in range(1,n):
                self.spots_taken[i] = i
            candidates[1] = self.queen_analysis()[:]

            # from here we start analysis
            for coor_1 in candidates[1]:
                for i in range(2,n):
                    self.spots_taken[i] = i
                self.spots_taken[1] = coor_1
                candidates[2] = self.queen_analysis()[:]

                for coor_2 in candidates[2]:
                    for i in range(3,n):
                        self.spots_taken[i] = i
                    self.spots_taken[2] = coor_2
                    candidates[3] = self.queen_analysis()[:]

                    for coor_3 in candidates[3]:
                        for i in range(4,n):
                            self.spots_taken[i] = i
                        self.spots_taken[3] = coor_3
                        candidates[4] = self.queen_analysis()[:]

                        for coor_4 in candidates[4]:
                            for i in range(5,n):
                                self.spots_taken[i] = i
                            self.spots_taken[4] = coor_4
                            candidates[5] = self.queen_analysis()[:]

                            for coor_5 in candidates[5]:
                                for i in range(6,n):
                                    self.spots_taken[i] = i
                                self.spots_taken[5] = coor_5
                                candidates[6] = self.queen_analysis()[:]

                                for coor_6 in candidates[6]:
                                    for i in range(7,n):
                                        self.spots_taken[i] = i
                                    self.spots_taken[6] = coor_6
                                    candidates[7] = self.queen_analysis()[:]

                                    for coor_7 in candidates[7]:
                                        self.spots_taken[7] = coor_7
                                        for coor in self.spots_taken:
                                            if type(coor) == tuple:
                                                self.insert(coor)
                                        result.append(Chessboard(self.board))
                                        self.spots_taken[7] = 7
                                        self.board = self.empty_board

        print('Total solution:', len(result))
        return result


# TODO 未完成最终算法

if __name__ == '__main__':
    t = Chessboard()
    answer = t.queen_solve(8)


