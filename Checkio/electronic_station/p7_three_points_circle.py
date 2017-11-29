# Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so: "(x1,y1),(x2,y2),(x3,y3)"

# You should find the circle for three given points, such that the circle lies through these point and return the result as a string with the equation of the circle.

# the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
# "(x-x0)^2+(y-y0)^2=r^2"

# Input: Coordinates as a string..
# Output: The equation of the circle as a string.



import math
def checkio(data):
    def distance(x, y, x0, y0):
        """both x and y are a set of coordinates in the form of (x, y)"""
        return round(math.sqrt(abs(x - x0)**2 + abs(y - y0) ** 2), 2)

    dataset = [int(x) for x in filter(lambda x: x.isdigit(), data)]
    x, xlst, y, ylst = 0, [], 0, []
    while x <= 10:
        x += 0.01
        xlst.append(round(x, 2))
    while y <= 10:
        y += 0.01
        ylst.append(round(y, 2))
    for i in xlst:
        for j in ylst:
            if distance(dataset[0], dataset[1], i, j) == distance(dataset[2], dataset[3], i, j) == distance(dataset[4], dataset[5], i, j):
                result = [i, j]
                break
    print(result)


    return ""

# if __name__ == '__main__':
#     assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
#     assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

data = "(2,2),(6,2),(2,6)"
print(checkio(data))
