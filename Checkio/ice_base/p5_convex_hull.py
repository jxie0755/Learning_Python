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


# assert checkio(
#     [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
# ) == [4, 5, 6, 0, 1, 2, 3], "First example"
# assert checkio(
#     [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
# ) == [1, 0, 6, 3, 5, 2], "Second example"
# print('done')
# data = [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
# checkio(data)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"

# 未完待续
