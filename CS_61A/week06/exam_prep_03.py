# CS61A Exam Prep 03: List, Trees, & Tree Recursion


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree): # every branch must be a tree as well
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# Q1 Tree Recursion with Trees

def sum_range(t):
    """Returns the range of the sums of t, that is,
    the difference between the largest and the smallest sums of t."""
    def helper(t):
        if is_leaf(t):
            return [label(t), label(t)]
        else:
            a = min([helper(b)[1] for b in branches(t)])
            b = max([helper(b)[0] for b in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y

if __name__ == "__main__":
    t1 = tree(5, [tree(1, [tree(2), tree(7, [tree(4, [tree(3)])])]), tree(2, [tree(0), tree(9)])])
    # the sums of the tree below are 20 (5+1+7+4+3), 8 (5+1+2), 7 (5+2+0), and 16 (5+2+9)
    # answer should be 20 - 7 = 13
    print(sum_range(t1)) # >>> 13


# Q2 This One Goes to Eleven

# Fill in the blanks of the implementation of no_eleven below,
# a function that returns a list of all distinct length-n lists of ones and sixes
# in which 1 and 1 do not appear0 consecutively.

def no_eleven(n):
    """Return a list of lists of 1"s and 6"s that do not
    contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven(n-1), no_eleven(n-2)
        return [[6] + s for s in a] + [[1, 6] + s for s in b]


# Q3 Expression Trees

# Your partner has created an interpreter for a language that can add or multiply positive integers.
# Expressions are represented as instances of the Tree class and must have one of the following three forms:
# • (Primitive) A positive integer entry and no branches, representing an integer
# • (Combination) The entry "+", representing the sum of the values of its branches
# • (Combination) The entry "*", representing the product of the values of its branches

# The sum of no values is 0. The product of no values is 1.

# Unfortunately, multiplication in Python is broken on your computer.
# Implement eval_with_add, which evaluates an expression without using multiplication.
# You may fill the blanks with names or call expressions
# but the only way you are allowed to combine two numbers is using addition.
# You may assume you have access to the tree, label, branches, and is_leaf functions, as defined below.


def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = Tree("+", [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree("*", [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree("*", [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree("*"))
    1
    """
    if label(t) == "+":
        return sum([eval_with_add(b) for b in branches(t)])

    elif label(t) == "*":
        total = 1
        for b in branches(t):
            total, term = 0, total
            for i in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return label(t)
