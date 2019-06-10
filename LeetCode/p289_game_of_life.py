# P289 Game of Life
# Medium


# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.


# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

from typing import *

class Solution:

    # Version A
    # Write a function to check neighor counts
    # Create a list of all coors with the neighbor count
    # Change the value all in-once
    # This takes O(N^2) time and O(N) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def checkNeighbors(coor):
            """check a coor's neighbor and decide it's next value"""
            live_neigbors = 0
            r, c = coor[0], coor[1]
            for rr in range(r-1, r+2):
                for cc in range(c-1, c+2):
                    if row > rr >= 0 and col > cc >= 0 and (rr, cc) != (r, c):
                        live_neigbors += board[rr][cc]
            if live_neigbors < 2:
                return 0
            elif live_neigbors ==2:
                return board[r][c]
            elif live_neigbors == 3:
                return 1
            else:
                return 0

        # Generate a temporarily check list for final update
        check_list = []
        for r in range(0, row):
            for c in range(0, col):
                check_list.append(checkNeighbors((r, c)))

        # Load all new values into board
        for r in range(0, row):
            for c in range(0, col):
                board[r][c] = check_list.pop(0)



    # Version B, change value in-place
    # Same idea as Version 1, but use -1 represent new value, and -2 for new 0
    # This takes O(N^2) time and O(1) space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def updateTempVal(coor):
            """check a coor's neighbor and decide it's next value"""
            # -1 : currently 0, will be 1
            # -2 : currently 1, will be 0

            live_neigbors = 0
            r, c = coor[0], coor[1]
            cur_val = board[r][c]
            for rr in range(r - 1, r + 2):
                for cc in range(c - 1, c + 2):
                    if row > rr >= 0 and col > cc >= 0 and (rr, cc) != (r, c):
                        # add more conditioanl check to calculate the value
                        neighbor_val = board[rr][cc]
                        if neighbor_val == 0 or neighbor_val == -1:
                            live_neigbors += 0
                        elif neighbor_val == 1 or neighbor_val == -2:
                            live_neigbors += 1

            if live_neigbors < 2:
                board[r][c] = -2 if cur_val == 1 else 0
            elif live_neigbors == 3:
                board[r][c] = -1 if cur_val == 0 else 1
            elif live_neigbors > 3:
                board[r][c] = -2 if cur_val == 1 else 0

        # Generate a temporarily val in-place with temp val
        for r in range(0, row):
            for c in range(0, col):
                updateTempVal((r, c))

        # update the new values in-place in board
        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == 1 or board[r][c] == -1:
                    board[r][c] = 1
                else:
                    board[r][c] = 0




if __name__ == '__main__':
    A = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    Solution().gameOfLife(A)
    assert A == [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ], 'Example 1'

    print('all passed')
