# CSM01 Tree Recursion and Data Abstraction

# Q1
# Write a function is_sorted that takes in an integer n and returns true if the digits of that number are increasing from right to left.

def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    # result = []
    # while n > 0:
    #     result.append(n % 10)
    #     n = n // 10

    # check, is_sort = result[0], True
    # for i in result:
    #     if i >= check:
    #         check = i
    #     else:
    #         is_sort = False
    # return is_sort

    # recursion way
    right_digit, rest = n % 10, n // 10
    if rest == 0:
        return True
    elif right_digit > rest % 10:
        return False
    else:
        return is_sorted(rest)

import doctest
doctest.testmod(verbose=True)

# # Q2
# def mario_number(level):
#     """
#     Return the number of ways that Mario can traverse the
#     level, where Mario can either hop by one digit or two
#     digits each turn. A level is defined as being an integer
#     with digits where a 1 is something Mario can step on and 0
#     is
#     something Mario cannot step on.
#     >>> mario_number(10101)
#     1
#     >>> mario_number(11101)
#     2
#     >>> mario_number(100101)
#     0
#     """
