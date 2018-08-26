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
def sum_of_nodes(t):
    """return sum of all nodes including labels and leafs"""
    return label(t) + sum([sum_of_nodes(b) for b in branches(t)])

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
    return x, y


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


def add_trees(t1, t2):
    """
    Add two tree together
    t1, t2 are two trees

    If a node at any particular position is present in one tree but not the other, it should be present in the new tree as well.
    """
    lab = label(t1) + label(t2)
    b1, b2 = branches(t1), branches(t2)
    while len(b1) > len(b2):
        b2 = b2 + [tree(0)]
    while len(b2) > len(b1):
        b1 = b1 + [tree(0)]
    return tree(lab, [add_trees(b[0], b[1]) for b in zip(b1, b2)])

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain the same labels the same number of times.
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}
        else:
            counts = dict()
            for b in branches(t) + [tree(label(t))]:
                for lab, count in label_counts(b).items():
                    if lab not in counts:
                        counts[lab] = 0
                    counts[lab] += count
            return counts
    return label_counts(t1) == label_counts(t2)


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


    t1 = tree(5, [tree(1, [tree(2), tree(7, [tree(4, [tree(3)])])]), tree(2, [tree(0), tree(9)])])
    # the sums of the tree below are 20 (5+1+7+4+3), 8 (5+1+2), 7 (5+2+0), and 16 (5+2+9)
    # answer should be 20 - 7 = 13
    print(sum_range(t1)) # >>> 13

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

    print_tree(add_trees(tree(2, [tree(3)]), tree(3, [tree(4), tree(5)])))
    # >>>
    # 5
    #   7
    #   5

    x = tree(1, [tree(2), tree(2), tree(3)])
    y = tree(3, [tree(2), tree(1), tree(2)])
    print(about_equal(x, y))
    # >>> True
    z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    print(about_equal(x, z))
    # >>> False
