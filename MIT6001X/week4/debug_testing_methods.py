def sqrt(x, eps):
    """
    :param x: floats, x >= 0
    :param eps: floats, eps > 0
    :return: Returns res such that x-eps <= res*res <= x + eps
    """

def abs(x):
    """
    :param x: an integer
    :return: x if x>= 0, and -x other wise
    """

    if x < -1:
        return -x
    else:
        return x

print(abs(-1))

# black box testing
# designed without looking at the code, can be done by anyone, other than the programmer
# testing can be reused if implementation changes
# paths through specification
    # build test cases in different natural space partitions
    # also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)

# test boundary:
# boundary: x = 0
# Perfect square: x = 25
# Less than 1: x = 0.05
# Irrational square root(imperfect): x = 2
# extremes: large epslon
# extremes: small eplon
# large number


# glass box testing
# use code directly to guide design of test cases
# called path-complete if every potential path through code is tested as leaset once
# what are the drawbacks of this type of testing?
    # can go through loops arbitrarily many times
    # missing pathts
# guildelines
    # branches - exercise all parts of a conditional
    # for loops - loop not entered, body of loop executed exactly once, or more than once
    # while loops - same as for loops, cases that catch all ways to exit loop
