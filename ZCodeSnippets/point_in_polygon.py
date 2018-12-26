# http: // okomestudio.net / biboroku /?p = 986

def inside_polygon(point, polygon):
    """
    Return True if a coordinate (x, y) is inside or on the edge of a polygon defined by
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


polygon = [[3, 8], [1, 6], [6, 2], [8, 4], [6, 8]]
point3 = [7, 6]
point4 = [5, 5]
pointx = [8, 6]

print(inside_polygon(point3, polygon))  # >>> True (on the edge)
print(inside_polygon(point4, polygon))  # >>> True (inside)
print(inside_polygon(pointx, polygon))  # >>> False (outside)


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


polygon = [[3, 8], [1, 6], [6, 2], [8, 4], [6, 8]]
point1 = [7, 6]
point2 = [5, 5]
pointx = [8, 6]

print(pointOnBorder(point1, polygon))  # >>> True (on the edge)
print(pointOnBorder(point2, polygon))  # >>> False (inside)
print(pointOnBorder(pointx, polygon))  # >>> False (outside)

# TODO this is proved to be wrong
# 新想法: 每个点和其他点连成的封闭图形相比,如果再外则被排除, 直到无法排除任何一个点
