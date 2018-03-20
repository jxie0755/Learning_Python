# PE015 Lattice paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#######
#  #  #
#######
#  #  #
#######

# How many such routes are there through a 20×20 grid?


def count_grid_path(n):
    """return number of paths from top left to bottom right

    only allow to move right and down
    n: size of the grid
    """

    count = 0
    current = [(0,0)]

    while len(current) != 0:
        temp = []
        for coor in current:
            temp += [(coor[0] + 1, coor[1]), (coor[0], coor[1] + 1)]
        current = temp

        open_path, end_path = [], []
        for coor in current:
            if coor[0] == n or coor[1] == n:
                end_path.append(coor)
            else:
                open_path.append(coor)

        current = open_path
        count += len(end_path)

    return count



print(count_grid_path(3))