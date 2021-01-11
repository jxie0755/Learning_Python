"""
This is from ProjectEuler P026 (ProjectEuler.p026_reciprocal_cycles.py)
Optimized algorithm by using divide calculation, to obtain the repeating pattern.
"""

def find_reciprocal(numerator, denominator):
    """find out the pattern of the reciprocal part when numerator / denominator
    numerator: integer
    denominator: integer
    num
    return: a string of the pattern numbers
    """

    assert numerator < denominator, "numerator must be smaller than denominator"

    decimal_part, remainder_list = "", [numerator % denominator]
    numerator *= 10  # start with numerator * 10 to avoid the first decimal point

    for i in range(denominator):
        quotient, numerator = divmod(numerator, denominator)
        if numerator == 0:
            return "the result is not reciprocal"
        else:
            decimal_part += str(quotient)
            if numerator not in remainder_list:
                remainder_list.append(numerator)
                numerator *= 10
            else:
                start = remainder_list.index(numerator)
                pattern = decimal_part[start:]
                return pattern

if __name__ == "__main__":
    print("Test algorithm:")
    assert find_reciprocal(1, 7) == "142857"   # = 0.(142857)
    assert find_reciprocal(1, 70) == "142857"  # = 0.0(142857)
    assert find_reciprocal(2, 3) == "6"        # = 0.(6)
    assert find_reciprocal(1, 12) == "3"       # = 0.08(3)

    a = find_reciprocal(1, 983)
    print("Pattern length for 1/983 is", len(a))

    print("All passed")
