"""
Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so: "(x1,y1),(x2,y2),(x3,y3)"

You should find the circle for three given points, such that the circle lies through these point and return the result as a string with the equation of the circle.

the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
"(x-x0)^2+(y-y0)^2=r^2"

Input: Coordinates as a string..
Output: The equation of the circle as a string.
"""

import math
def checkio(data):
    # prepare the x, y for iteration
    dataset = [int(x) for x in filter(lambda x: x.isdigit(), data)]

    # calculate the x,y coordinates
    def get_circle_center_and_radius(x):
        x1, y1, x2, y2, x3, y3 = dataset
        d = 2.0 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
        x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2)
             * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
        y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2)
             * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
        r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        return [str(round(x, 2)), str(round(y, 2)), str(round(r, 2))]

    # format the result
    result = get_circle_center_and_radius(dataset)
    print(result)
    for i in range(3):
        if len(result[i]) == 3 and ".0" in result[i]:
            result[i] = result[i][0]

    return f"(x-{result[0]})^2+(y-{result[1]})^2={result[2]}^2"

if __name__ == "__main__":
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    print("done")
