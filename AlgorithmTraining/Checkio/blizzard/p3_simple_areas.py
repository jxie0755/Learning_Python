"""
You should write a function to calculate the area of simple figures: circles, rectangles and triangles.
You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures.
One argument -- The diameter of a circle and you need calculate the area of the circle.
Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.

Input: One, two or three arguments as floats or as integers.
Output: The area of the circle, the rectangle or the triangle as a float.
"""


import math
def simple_areas(*args):
    if len(args) == 1:
        return round((args[0]/2)**2*(math.pi), 2)
    if len(args) == 2:
        return round(args[0] * args[1], 2)
    if len(args) == 3:
        a, b, c, p = args[0], args[1], args[2], (args[0] + args[1] + args[2])/2
        return round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)

if __name__ == "__main__":
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
