# CS61A Discussion 06: Order of Growth and Linked list

from lecture_19_composition import Link

# Warm up
# What is the order of growth for the following functions?

def fib_iter(n):  # O(n)
    prev, curr, i = 0, 1, 0
    while i < n:
        prev, curr = curr, prev + curr
        i += 1
    return prev


def fib_recursive(n):  # O(2^n)
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# Write a function that takes in a a linked list and returns the sum of all its elements.
# You may assume all elements in lnk are integers
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest:
        return lnk.first + sum_nums(lnk.rest)
    else:
        return lnk.first

