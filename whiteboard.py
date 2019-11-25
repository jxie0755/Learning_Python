return any([self.finder(board, word, idx+1, new_coor, new_prev) for new_coor in [up, down, left, right]])

