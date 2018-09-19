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

# Write a function that takes a sorted linked list of integers and mutates it so that all duplicates are removed.

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
    else:
        return None
    remove_duplicates(lnk)

import doctest
doctest.testmod(verbose=True)


# Midterm Review
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # result = []
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         result.append(i*lst[i])
    # return result
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]


# The quicksort sorting algorithm is an efficient and commonly used algorithm to
# order the elements of a list.
# We choose one element of the list to be the pivot element and partition the remaining elements into two lists:
# one of elements less than the pivot and one of elements greater than the pivot.
# We recursively sort the two lists, which gives us a sorted list of all the elements less than the pivot and all the elements greater than the pivot, which we can then combine with the pivot for
# a completely sorted list.

# First, implement the quicksort list function. Choose the first element of the list
# as the pivot. You may assume that all elements are distinct.

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) == 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

