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
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])


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
