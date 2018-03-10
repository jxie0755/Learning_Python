# CS61A Lecture 04: Higher-Order Functions

# DRY principle (Don't repeat yourself)

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits.

    >>> same_length(50, 70)
    True
    >>> same_length(50, 100)
    False
    >>> same_length(1000, 100000)
    False
    """
    return digits(a) == digits(b)
    # a_digits = 0
    # while a > 0:
    #     last, a = a % 10, a // 10
    #     a_digits = a_digits + 1
    # b_digits = 0
    # while b > 0:
    #     last, b = b % 10, b // 10
    #     b_digits = b_digits + 1
    # return a_digits == b_digits

def digits(a):
    a_digits = 0
    while a > 0:
        a, last = a // 10, a % 10
        a_digits = a_digits + 1
    return a_digits

# instead of writing the same type of code blocks twice, better to create a function to specifically count the number of digits. Then apply it to both a and b and compare.

