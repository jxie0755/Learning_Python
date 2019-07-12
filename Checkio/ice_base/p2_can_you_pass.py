# You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value.
# The matrix consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the origin and destination cells are equal.
# You should determine if a path exists between two given cells.
# A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers: row and column.

# Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.
# Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.

import itertools


def can_pass(matrix, first, second):
    # add 1 layer over the matrix with "x"
    matrix_new = list(map(lambda x: list(x), matrix))
    addrow1, addrow2 = itertools.tee(list(map(lambda x: "x", range(len(matrix[0])))))
    matrix_new.insert(0, list(addrow1))
    matrix_new.append(list(addrow2))

    for i in matrix_new:
        i.insert(0, "x")
        i.append("x")

    # get new coordinates for first and second
    first, second = tuple(map(lambda x: x + 1, first)), tuple(map(lambda x: x + 1, second))

    # write a function to get the value of a coordinate
    def coorvalue(coor):
        """"coor is a tuple indicating a coordinate (x, y)"""
        return matrix_new[coor[0]][coor[1]]

    # write a function to check neighbor value
    temp, result = [], []

    def neighbor(coor):
        """"coor is a tuple indicating a coordinate (x, y)"""
        if coor not in temp:  # only examine each coor once
            temp.append(coor)  # by using a temp list
            x, y = coor[0], coor[1]
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]  # up, down, left, right

            # examine and filter the one that has the same value as first and include in a list
            connected = list(filter(lambda x: coorvalue(x) == coorvalue(coor), neighbors))
            for i in connected:
                result.append(i)  # if same value, then add to result list
                neighbor(i)  # and also check the neighbor of it (recursion)

    neighbor(first)  # start the recursion

    return second in result


if __name__ == "__main__":
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, "First example"
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, "First example"
    print("done")
