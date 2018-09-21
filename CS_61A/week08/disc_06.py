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
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [i for i in lst if i < pivot]
    greater = [i for i in lst if i > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

# Write a function that takes in a list and returns the maximum product that can be
# formed using nonconsecutive elements of the list.
# The input list will contain only numbers greater than or equal to 1.

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if lst == []:
        return 1
    elif len(lst) == 1: # Base case optional
        return lst[0]
    else:
        return max(max_product(lst[1:]), lst[0]*max_product(lst[2:]))

# 4.4
# An expression tree is a tree that contains a function for each non-leaf node,
# which can be either ’+’ or ’*’. All leaves are numbers. Implement eval_tree,
# which evaluates an expression tree to its value. You may want to use the functions
# sum and prod, which take a list of numbers and compute the sum and product
# respectively.

def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if label(tree) == '+':
        return sum([eval_tree(b) for b in branches(tree)])

    elif label(tree) == '*':
        temp = 1
        for b in branches(tree):
            temp *= eval_tree(b)
        return temp

    else:
        return label(tree)

# Complete redundant map, which takes a tree t and a function f, and applies f to
# the node (2d) times, where d is the depth of the node. The root has a depth of 0
def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(branch, new_f) for branch in t.branches]
    return t
    