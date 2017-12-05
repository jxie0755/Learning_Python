# You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value.
# The matrix consists of digits. You may move to neighbouring cells either horizontally or vertically provided the values of the origin and destination cells are equal.
# You should determine if a path exists between two given cells.
# A matrix is represented as a tuple of tuples with digits. Coordinates are represented as a tuple with two numbers: row and column.

# Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.
# Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.

def can_pass(matrix, first, second):
    # get value of first and second
    v1, v2 = matrix[first[0]][first[1]], matrix[second[0]][second[1]]

    # write a function to check neigher value
    def neigher(x, y):
        up = first[0]

    return None


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'

matrix = ((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),)
first = (3, 2)
second = (0, 5)
