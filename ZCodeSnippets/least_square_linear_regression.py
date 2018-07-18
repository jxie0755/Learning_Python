# This is to generate a linear regression function for a bunch of coordinates

def mean(sequence):
    return sum(sequence) / len(sequence)


def find_linear_reg(coordinates):
    """Return a least square linear regression function
    in the form of: b * x + a

    coordinates: a list of coordinates in the form of [x, y]
    return: a function, which takes x and returns b * x + a
    """


    xs = [coor[0] for coor in coordinates]
    ys = [coor[1] for coor in coordinates]

    # BEGIN Question 7
    s_xx = sum([(x - mean(xs)) ** 2 for x in xs])
    s_yy = sum([(y - mean(ys)) ** 2 for y in ys])
    s_xy = sum([(x - mean(xs)) * (y - mean(ys)) for x, y in coordinates])

    b = s_xy / s_xx
    a = mean(ys) - b * mean(xs)
    r_squared = s_xy ** 2 / (s_xx * s_yy)

    # END Question 7

    print('b =', b, 'a =', a, 'r_squared =', r_squared )
    def predictor(x):
        return b * x + a

    return predictor

if __name__ == '__main__':
    coors = [[1, 3], [2, 1], [3, 4], [4, 2], [5, 5], [6, 3]]
    print(find_linear_reg(coors))
    # >>>
    # b = 0.2857142857142857 a = 2.0 r_squared = 0.14285714285714285
    # <function find_linear_reg.<locals>.predictor at 0x000001E60C3D6268>
    # confirmed by Excel plotting.
