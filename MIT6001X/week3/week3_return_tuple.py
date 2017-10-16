def quotient_and_remainder(x, y):
    """
    this is to calculate the quotient and remainder when x / y

    :param x: x for x / y
    :param y: y for x / y
    :return:
    """
    q = x // y
    r = x % y
    return (q, r)

(quot, rem) = quotient_and_remainder(7, 3)
print(quot, rem)
