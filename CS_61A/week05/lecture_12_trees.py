"""CS61A Lecture 12 Trees"""

# Slicing
odds = [3, 5, 7, 9, 11]
print(list(range(1, 3)))
print([odds[i] for i in range(1, 3)])
print(odds[1:3])
print(odds[1:])
print(odds[:3])
print(odds[:])

# Aggregation

print(sum(odds))
print(sum({3:9, 5:25}))
print(max(range(10)))
print(max(range(10), key=lambda x: 7 - (x-2)*(x-4)))
print(all([x < 5 for x in range(5)]))
perfect_square = lambda x: x == round(x ** 0.5) ** 2
print(any([perfect_square(x) for x in range(50, 60)])) # Try ,65


# Trees
# A tree contains a root label and a list of branches, each branch is a tree
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
    for branch in branches(tree):  # every branch must be a tree as well
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


T = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(T) # >>>
# [3, [1], [2, [1], [1]]]

T = tree(1, [tree(5, [tree(7)]), tree(6)])
print(T) # >>>
# [1, [5, [7]], [6]]

# fibonacci tree
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

print(fib_tree(4))
# >>>
# [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]

def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

print(count_leaves(fib_tree(4)))
# >>> 5

def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

print(leaves(fib_tree(4)))
# >>>
# [0, 1, 1, 0, 1]

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t):
    print(label(t))
    for b in branches(t):
        print_tree(b)

print_tree(fib_tree(4))
# >>>
# 3
# 1
# 0
# 1
# 2
# 1
# 1
# 0
# 1

# new version
def print_tree(t, indent=0):
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

print_tree(fib_tree(4))
# >>>
# 3
#   1
#     0
#     1
#   2
#     1
#     1
#       0
#       1
print_tree(fib_tree(5))
# >>>
# 5
#   2
#     1
#     1
#       0
#       1
#   3
#     1
#       0
#       1
#     2
#       1
#       1
#         0
#         1


print("f1", fib_tree(1))
print("f2", fib_tree(2))
print("f3", fib_tree(3))
print("f4", fib_tree(4))

print_tree(
tree(1, [
    tree(2, [
        tree(3, [
            tree(4),
            tree(4)]),
        tree(3, [
            tree(4),
            tree(4)])]),
    tree(2, [
        tree(3, [
            tree(4),
            tree(4)]),
        tree(3, [
            tree(4),
            tree(4)])])]))
# >>>
# 1
#   2
#     3
#       4
#       4
#     3
#       4
#       4
#   2
#     3
#       4
#       4
#     3
#       4
#       4


# Lecture 12 Extra
# From textbook <Composing Programs>
# http://composingprograms.com/pages/23-sequences.html

# Partition Trees
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m"""
    if n == 0:
        return (tree(True))
    elif n < 0 or m == 0:
        return (tree(False))
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return (tree(m, [left, right]))

print_tree(partition_tree(2,2))
# >>>
# 2
#  True
#  1
#   1
#    True
#    False
#   False

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

print_parts(partition_tree(6, 4))
# >>>
# 4 + 2
# 4 + 1 + 1
# 3 + 3
# 3 + 2 + 1
# 3 + 1 + 1 + 1
# 2 + 2 + 2
# 2 + 2 + 1 + 1
# 2 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1 + 1


# Right binarized tree
def right_binarize(tree):
    """Construct a right-branching binary tree."""
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

# print(right_binarize([1, 2, 3, 4, 5, 6, 7])) some how does not work
# >>>
# [1, [2, [3, [4, [5, [6, 7]]]]]]


# Linked list

# Common representation of a sequence constructed fro nested aris is called a linked list
four = [1, [2, [3, [4, "empty"]]]]
# a pair containing the first element of the sequence (in this case 1) and the rest of the sequence

empty = "empty"
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest"""
    assert is_link(rest), "rest must be a linked list"
    return [first, rest]

def first(s):
    """return the first element of a linked list s."""
    assert is_link(s), "only apllies to linked list"
    assert s != empty, "empty linked list has no first element"
    return s[0]

def rest(s):
    """Return the rest of the elemetns of a linked list s"""
    assert is_link(s), "rest only applies to linked lists"
    assert s != empty, "empty linked list has no rest"
    return s[1]

four = [1, [2, [3, [4, "empty"]]]]
four = link(1, link(2, link(3, link(4, empty))))
print(four)
# >>>
# [1, [2, [3, [4, "empty"]]]]


def len_link(s):
    """Return the length of linked list"""
    assert is_link(s), "must apply on linked list"
    if len(s) == 2:
        return 1 + len_link(rest(s))
    else:
        return 0

print(len_link(four))
# >>> 4

def getitem_link(s, i):
    """Return the element at index i of linked list s"""
    assert is_link(s)
    if i == 0:
        return first(s)
    else:
        return getitem_link(rest(s), i-1)

print(getitem_link(four, 1))
# >>> 2



def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree("*", [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree("+", [expr, tree(4), tree(5)]))
    15
    """
    if label(tree) == "+":
        return sum([eval_tree(b) for b in branches(tree)])

    elif label(tree) == "*":
        temp = 1
        for b in branches(tree):
            temp *= eval_tree(b)
        return temp

    else:
        return label(tree)

print(eval_tree(tree(1)))
# >>> 1
expr = tree("*", [tree(2), tree(3)])
print(eval_tree(expr))
# >>> 6
print(eval_tree(tree("+", [expr, tree(4), tree(5)])))
# >>> 15
