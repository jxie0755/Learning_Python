# From CS61a
# http://composingprograms.com/pages/23-sequences.html


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
    for branch in branches(tree): # every branch must be a tree as well
        if not is_tree(branch):
            return False
    return True


def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


# Leaves
def is_leaf(tree):
    return not branches(tree)


def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])


def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    # in the form as a list
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])  # sum of lists is still a list

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)



# Tree functions
def tree_max(t):
    """Return the max of a tree."""
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])
    # 要注意这里max不是对整个list求max,而是每一层都求max,一路递归到上到根部


def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])


def find_path(tree, x):
    """Find path to the value x if x in the tree, else None"""
    if label(tree) == x:
        return [label(tree)]

    for path in [find_path(branch, x) for branch in branches(tree)]:
        if path:
            return [label(tree)] + path



# New tree
def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t) **2, [square_tree(branch) for branch in branches(t)])


def prune(t, k):
    """Return a tree that takes in a tree only to the depth k"""
    if k == 0:
        return tree(label(t))
    else:
        return tree(label(t), [prune(branch, k-1) for branch in branches(t)])

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away."""

    if is_leaf(t) and label(t) in vals:
        return None
    else:
        return tree(label(t), [prune_leaves(b, vals) for b in branches(t) if prune_leaves(b, vals) != None])

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes."""
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def replace_leaf(t, old, new):
    if is_leaf(t) and label(t) == old:
        return tree(new)
    else:
        return tree(label(t), [replace_leaf(b, old, new) for b in branches(t)])

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree."""
    if is_leaf(t):
        return tree(label(t), [tree(i) for i in vals])
    else:
        return tree(label(t), [sprout_leaves(b, vals) for b in branches(t)])

def tree_finder(t, keywd):
    """Returns True if t contains a node with the value of keywd and
    False otherwise."""
    # result = []

    # # define a helper function to extract all the labels into a list
    # def search(t):
    #     nonlocal result
    #     result += [label(t)]
    #     for b in branches(t):
    #         search(b)
    # # this is an imperfect function which only use the side effect to change the list result.

    # search(t) # execute the helper function
    # return keywd in result

    return label(t) == keywd or True in [tree_finder(b, keywd) for b in branches(t)]

# Test
if __name__ == '__main__':
    T = tree(1, [
    tree(2, [
        tree(4, [
            tree(8),
            tree(9)]),
        tree(5, [
            tree(10),
            tree(11)])]),
    tree(3, [
        tree(6, [
            tree(12),
            tree(13)]),
        tree(7, [
            tree(14),
            tree(15, [
                tree(20),
                tree(21),
                tree(22)])])])])
    print_tree(T)
    # >>>
    # 1
    #   2
    #     4
    #       8
    #       9
    #     5
    #       10
    #       11
    #   3
    #     6
    #       12
    #       13
    #     7
    #       14
    #       15
    #         20
    #         21
    #         22

    # Leaves

    print('count leaves', count_leaves(T))
    # >>> 10

    # Tree functions

    print('tree max value', tree_max(T))
    # >>> 22
    print('tree height', height(T))
    # >>> 4


    print('path', find_path(T, 10))  # >>> [1, 2, 5, 10]
    print('path', find_path(T, 5))   # >>> [1, 2, 5]
    print('path', find_path(T, 50))  # >>> None

    # New tree

    print('incremented tree', increment(T))
    # >>>
    # [2, [3, [5, [9], [10]], [6, [11], [12]]], [4, [7, [13], [14]], [8, [15], [16, [21],

    print('squared tree', square_tree(T))
    # >>>
    # [1, [4, [16, [64], [81]], [25, [100], [121]]], [9, [36, [144], [169]], [49, [196], [225, [400], [441], [484]]]]]

    print('pruned tree', prune(T, 2))
    # >>>
    # [1, [2, [4], [5]], [3, [6], [7]]]

    numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    print('prune leaves')
    print_tree(numbers)
    # >>>
    # 1
    #   2
    #   3
    #     4
    #     5
    #   6
    #     7
    print_tree(prune_leaves(numbers, (3,4,6,7)))
    # >>>
    # 1
    #   2
    #   3
    #     5
    #   6

    print('sprout leaves', print_tree(sprout_leaves(numbers, [9, 10])))
    # >>>
    # 1
    #   2
    #     9
    #     10
    #   3
    #     4
    #       9
    #       10
    #     5
    #       9
    #       10
    #   6
    #     7
    #       9
    #       10


    print('replaced leaf', replace_leaf(T, 22, 99))
    # >>> a new tree, repalced the last leaf from 22 to 99

    sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('acorn')]), tree('branch2')])
    numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    print('search acorn', tree_finder(sproul, 'acorn'))
    print('search 10', tree_finder(numbers, 10))
    print('search 6', tree_finder(numbers, 6))



# Mobile balance from CS61a week05 HW05
# A similar structure as tree that use tree as a structure

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree('mobile', [left, right])

def is_mobile(m):
    return is_tree(m) and label(m) == 'mobile'

def sides(m):
    """Select the sides of a mobile."""
    assert is_mobile(m), "must call sides on a mobile"
    return branches(m)

def is_side(m):
    return not is_mobile(m) and not is_weight(m) and type(label(m)) == int

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return label(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return branches(s)[0]


# Q3 Weights
def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree('weight', [tree(size)])

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    assert is_weight(w)
    return label(branches(w)[0])

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return is_tree(w) and label(w) == 'weight'

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a weight"
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    if is_mobile(m):
        L, R = sides(m)[0], sides(m)[1]
        M_balance = length(L)* total_weight(end(L)) == length(R)* total_weight(end(R))  # 如果m是一个mobile,必须先要保证mobile两边是平衡的
        L_balance = balanced(end(L))  # 如果mobile的一边接的还是mobile, 必须保证它也是平衡的
        R_balance = balanced(end(R))  # 同上
        return M_balance and L_balance and R_balance

    else:
        return True  # 除非mobile的一边接得是weight,那就不必往下检查

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
