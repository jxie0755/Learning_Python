# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is:
# 0.25*n*s^2
# -----------
# tan(π/n)

# The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

import math

def polysum(n, s):
    """
    Calculation of the area of a regular polygon

    :param n: number of sides of the polygon
    :param s: length of each sides
    :return: (area + perimeter^2) of the polygon
    """
    area = 0.25 * n * s ** 2 / math.tan((math.pi / n))
    perimeter = n * s

    result = area + perimeter**2

    # round result to 4 decimal spaces
    result = round(result, 4)
    return result

