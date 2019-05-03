# You are given a list of points on a coordinate plane. We need you find the convex hull formed by these points.
# The convex hull may be visualized as the shape formed by a rubber band stretched around X. If a point lies on edge, it's included.

# Input: A list of coordinates. Each coordinate is a list of two integers.
# Output: The list of indexes of coordinates from the given list.
# The sequence starts from the bottom leftmost point.
# points lie on the convex hull in clockwise order (see the picture)


import math
def checkio(data):
    """
    Using convex hull algorithm learned from Princeton Algorithm Part 1 lecture 04

    Method:
    1. find the lowest right point p (minimum y point with largest x if multiple exist
    2. sort the rest point x in sequence according to the angle px - p - x (y is the vertical line of p[x])
    3. iterate through the sorted list and exclude the point x once the new p - x - xnext angle is bigger than 180 degrees
    """
    # Find the lowest right p point:
    p = [0,float('inf')]
    for i in data:
        if i[1] < p[1]:
            p = i
        elif i[1] == p[1] and i[0] > p[0]:
            p = i

    def distance(a, b):
        """return the distance of two points"""
        A = abs(a[0] - b[0])
        B = abs(a[1] - b[1])
        return math.sqrt(A*A + B*B)

    def sin_p(a):
        """calculate the sin value of point a and p
                   a
                  /
                 /
                p------x
        """
        if a == p:
            return -1
        elif a[0] >= p[0]:
            return abs(a[1] - p[1]) / distance(a, p)
        else:
            return 1 + (p[0] - a[0]) / distance(a, p)

    # Sort the data list according to the sin_p angle
    sorted_coors = sorted(data, key=lambda x:sin_p(x))

    pass











# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(
#         [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
#     ) == [4, 5, 6, 0, 1, 2, 3], "First example"
#     assert checkio(
#         [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
#     ) == [1, 0, 6, 3, 5, 2], "Second example"
#     print('done')

print(checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]))
# TODO 继续完成debug
