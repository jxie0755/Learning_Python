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

def is_leaf(tree):
    return not branches(tree)


# Test
if __name__ == '__main__':
    T = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    print(T) # >>>
    # [3, [1], [2, [1], [1]]]

    T = tree(1, [tree(5, [tree(7)]), tree(6)])
    print(T) # >>>
    # [1, [5, [7]], [6]]



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


# Test
if __name__ == '__main__':
    print(count_leaves(fib_tree(4)))
    # >>> 5

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


def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

if __name__ == '__main__':
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
    #  2
    #   3
    #    4
    #    4
    #   3
    #    4
    #    4
    #  2
    #   3
    #    4
    #    4
    #   3
    #    4
    #    4


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

if __name__ == '__main__':
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
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

if __name__ == '__main__':
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


def tree_max(t):
    """Return the max of a tree."""
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])
    # 要注意这里max不是对整个list求max,而是每一层都求max,一路递归到上到根部
