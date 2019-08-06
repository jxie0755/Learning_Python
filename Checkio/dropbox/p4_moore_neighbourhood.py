"""
You are given a state for a rectangular board game grid with chips in a binary matrix, where 1 is a cell with a chip and 0 is an empty cell.
You are also given the coordinates for a cell in the form of row and column numbers (starting from 0).
You should determine how many chips are close to this cell.

Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.
Output: How many neighbouring cells have chips as an integer.
"""

import itertools


def count_neighbours(grid, row, col):
    # add 1 layer over the matrix with 0
    grid_new = list(map(lambda x: list(x), grid))
    addrow1, addrow2 = itertools.tee(list(map(lambda x: 0, range(len(grid[0])))))
    grid_new.insert(0, list(addrow1))
    grid_new.append(list(addrow2))
    for i in grid_new:
        i.insert(0, 0)
        i.append(0)
        print(i)
    # new coordinates:
    row, col = row + 1, col + 1

    # Check neightbours
    result = 0 - grid_new[row][col]
    for i in range(-1, 2):
        x = row + i
        for j in range(-1, 2):
            y = col + j
            print(x, y)
            if grid_new[x][y] == 1:
                result += 1
    return result


if __name__ == "__main__":
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
