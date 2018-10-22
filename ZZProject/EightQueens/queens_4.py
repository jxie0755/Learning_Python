# This is a size down from eight queens just to check the algorithym with lower calculation amount

# This is to solve the Eight Queens problem in Chess
# TO security set 8 queens in a chess checkerboard where no queen can directly attack the other queens.


class Chessboard(object):
    """each instance should be a single plate that can be filled in with numbers
    there will be check method to ensure no conflict in going on.
    there will also be an final examination method to ensure when every empty slot is filled.
    the key is in the solve function, where the algorithm is in, to find the answer
    """
    empty_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    all_spots = [(x, y) for x in range(1, 5) for y in range(1, 5)]
    available_spots = all_spots[:]
    spots_taken = [0,1,2,3]
    snapshots = [available_spots[:]]

    def __init__(self, empty=[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
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
        y_num = 4
        separ = '    ----------'
        x_num = '    1, 2, 3, 4'


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
        self.board[4-y][x-1] = 1

    def un_insert(self, coor):
        x, y = coor[0], coor[1]
        self.board[4-y][x-1] = 0


    def get(self, coor):
        """obtain the value at a coor"""
        return self.board[4-coor[1]][coor[0]-1]


    # Generate coor list
    def row_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        row_coor_list = [(i, y) for i in range(1, 5)]
        return row_coor_list

    def col_coor(self, coor):
        """output a list of cross of coor in the direction of row"""
        x, y = coor[0], coor[1]
        col_coor_list = [(x, i) for i in range(1, 5)]
        return col_coor_list

    def cross_coor_1(self, coor): # of \ cross
        """output a list of cross of coor in the direction of /"""
        x, y = coor[0], coor[1]
        cross_coor_list = [coor]
        before, after = coor[:], coor[:]
        while before[0] > 1 and before[1] < 4:
            x, y = before[0], before[1]
            before = (x-1, y+1)
            cross_coor_list = [before] + cross_coor_list

        while after[0] < 4 and after[1] > 1:
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

        while after[0] < 4 and after[1] < 4:
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

    def queen_solve(self, n):
        candidates = [self.all_spots[:]] + [[] for i in range(n - 1)]
        result = []
        screen_list = []

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
                        self.spots_taken[3] = coor_3
                        if set(self.spots_taken) not in screen_list:
                            for coor in self.spots_taken:
                                if type(coor) == tuple:
                                    self.insert(coor)
                            result.append(Chessboard(self.board[:]))
                            screen_list.append(set(self.spots_taken[:]))
                            self.board = [
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                                [0, 0, 0, 0],
                            ]

        print('Total solution:', len(result))
        return result


if __name__ == '__main__':
    import time
    t = Chessboard()
    start_time = time.time()
    answer = t.queen_solve(4)
    for t in answer:
        print(t)
    print(f"--- {time.time() - start_time}s seconds ---\n")

    # --- 0.003989219665527344s seconds ---
    