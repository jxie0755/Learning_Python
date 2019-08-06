"""
You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

Input: The lengths of the sides of a triangle as integers.
Output: Angles of a triangle in degrees as sorted list of integers.
"""

from math import degrees, acos

def checkio(a, b, c):

    # check if triangle could be made:
    checklist = sorted([a, b, c])
    if checklist[0] + checklist[1] <= checklist[2]:
        return [0, 0, 0]
    # if triangle can be formed, then continue:
    else:
        def cal_angle(x, y, z):
            return round(degrees(acos((x**2 + y**2 - z**2)/(2 * x * y))))
    return sorted([cal_angle(a, b, c), cal_angle(a, c, b), cal_angle(c, b, a)])

if __name__ == "__main__":
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
