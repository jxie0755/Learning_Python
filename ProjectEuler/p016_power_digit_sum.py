# P016 Power digit sum


# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


def power_digit_sum(n):
    """return the sum of the digits of 2^n"""

    num = 2 ** n
    return sum([int(i) for i in str(num)])


if __name__ == "__main__":
    assert power_digit_sum(15) == 26, "regular"
    print(power_digit_sum(1000))
    # >>> 1366
    # passed
