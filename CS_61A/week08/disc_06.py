# CS61A Discussion 06: Order of Growth and Linked list

from lecture_19_composition import Link

# Warm up
# What is the order of growth for the following functions?

# 1.1
def fib_iter(n):  # O(n)
    prev, curr, i = 0, 1, 0
    while i < n:
        prev, curr = curr, prev + curr
        i += 1
    return prev

# 1.2
def fib_recursive(n):  # O(2^n)
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# 1.3
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


# What is the order of growth for the following functions?

#2.1
def sum_of_factorial(n):  # O(n^2)
    if n == 0:
        return 1
    else:
        return factorial(n) + sum_of_factorial(n - 1)

# 2.2
def bonk(n):  # O(log(n))
    total = 0
    while n >= 2:
        total += n
        n = n / 2
    return total

# 2.3
def mod_7(n):  # O(1)
    if n % 7 == 0:
        return 0
    else:
        return 1 + mod_7(n - 1)

# 2.4
def bar(n):  # O(1)
    if n % 2 == 1:
        return n + 1
    return n

def foo(n):  # O(n)
    if n < 1:
        return 2
    if n % 2 == 0:
        return foo(n - 1) + foo(n - 2)
    else:
        return 1 + foo(n - 2)

# What is the order of growth of foo(bar(n))? # O(n^2)


# Linked list

# Write a function that takes in a Python list of linked lists and multiplies them element-wise.
# It should return a new linked list.

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    if all([lnk for lnk in lst_of_lnks]):
        value, sub_list = 1, []
        for lnk in lst_of_lnks:
                value *= lnk.first
                sub_list.append(lnk.rest)
        return Link(value, multiply_lnks(sub_list))
    return ()

