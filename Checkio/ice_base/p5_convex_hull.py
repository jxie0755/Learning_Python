# You are given a list of points on a coordinate plane. We need you find the convex hull formed by these points.
# The convex hull may be visualized as the shape formed by a rubber band stretched around X. If a point lies on edge, it's included.

# Input: A list of coordinates. Each coordinate is a list of two integers.
# Output: The list of indexes of coordinates from the given list.
# The sequence starts from the bottom leftmost point.
# points lie on the convex hull in clockwise order (see the picture)

def checkio(data):
    # find the points at most up/down/left/right in a list called edge, edge is safe
    xlst, ylst = [i[0] for i in data], [i[1] for i in data]
    edge = list(
        filter(lambda i: i[0] == min(xlst) or i[0] == max(xlst) or i[1] == min(ylst) or i[1] == max(ylst), data))

    # the rest of the coor is suspecious
    suspecious = [i for i in data if i not in edge]

    print(edge)
    print(suspecious)

    def inside_polygon(point, polygon):
        """
        Return True if a coordinate (x, y) is inside a polygon defined by
        a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].
        """
        x, y = point[0], point[1]
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(1, n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def pointOnBorder(point, polygon):
        """
        Return True if a coordinate (x, y) is on the edge of a polygon defined by
        a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].
        """
        x, y = point[0], point[1]
        n = len(polygon)
        for i in range(n):
            p1x, p1y = polygon[i]
            p2x, p2y = polygon[(i + 1) % n]
            v1x = p2x - p1x
            v1y = p2y - p1y  # vector for the edge between p1 and p2
            v2x = x - p1x
            v2y = y - p1y  # vector from p1 to the point in question
            if (v1x * v2y - v1y * v2x == 0):  # if vectors are parallel
                if (v2x / v1x > 0):  # if vectors are pointing in the same direction
                    if (v1x * v1x + v1y * v1y >= v2x * v2x + v2y * v2y):  # if v2 is shorter than v1
                        return True
        return False

    candidates = edge[:]
    for i in suspecious:
        if inside_polygon(i, candidates) and not pointOnBorder(i, candidates):
           pass
        else:
            candidates.append(i)
    print(candidates)

    # after edge is finished report the index
    left, right, up, down, result = [], [], [], [], []
    for i in sorted(candidates):
        if i[0] == min(xlst):  # left
            left.append(i)
        if i[1] == max(ylst):  # up
            up.append(i)
        if i[0] == max(xlst):  # right
            right.append(i)
        if i[1] == min(ylst):  # down
            down.append(i)
    restcandidates = []
    for i in candidates:
        if i not in up and i not in down and i not in left and i not in right:
            restcandidates.append(i)

    # organize the result with the sequence of coordinates
    for i in left:
        result.append(i)
    for i in restcandidates:
        if i[1] >= left[-1][1] and i[0] <= up[0][0]:  # left to up
            result.append(i)
    for i in up:
        result.append(i)
    for i in restcandidates:
        if i[0] >= up[-1][0] and i[1] >= right[-1][1]:
            result.append(i)
    for i in right[::-1]:
        result.append(i)
    for i in restcandidates:
        if i[0] >= down[-1][0] and i[1] <= right[0][1]:
            result.append(i)
    for i in down[::-1]:
        result.append(i)
    for i in restcandidates:
        if i[0] <= down[0][0] and i[1] <= left[0][1]:
            result.append(i)
    print(result)
    indexlst = []
    for i in result:
        if data.index(i) not in indexlst:
            indexlst.append(data.index(i))
    return indexlst

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
        """calculate the sin value of point a and b
                   a
                  /
                 /
                p------x
        """
        if a[0] > p[0]:
            return abs(a[1] - p[1]) / distance(a, p)

    print(sin_p([8,4]))











# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(
#         [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
#     ) == [4, 5, 6, 0, 1, 2, 3], "First example"
#     assert checkio(
#         [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
#     ) == [1, 0, 6, 3, 5, 2], "Second example"
#     print('done')

print(checkio([[3, 8], [1, 6], [3,2], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]))
# TODO 继续完成debug
