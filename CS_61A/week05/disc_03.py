# CS61a Discussion 03 Trees & Sequences


# Q1 Index
# What would python display?

a = [1, 5, 4, [2, 3], 3]
print((a[0], a[-1])) # >>> 1 3
print(len(a)) # >>> 5
print(2 in a) # >>> False
print(4 in a) # >>> True
print(a[3][0]) # >>> 2

# Q2 Slicing
# What would python display?

a = [3, 1, 4, 2, 5, 3]
print(a[1::2]) # >>> [1, 2, 3]
print(a[:]) # >>> same as a
print(a[4:2]) # >>> []
print(a[1:-2]) # [1, 4, 2]
print(a[::-1]) # >>> reversied(a)


# List comprehensions
# What would python display?

print([i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0])
# >>> [3, 5]

print([i * i - i for i in [5, -1, 3, -1, 3] if i > 2])
# >>> [20, 6, 6]

print([[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]])
# >>> [[2, 4], [4, 6], [6, 8], [8, 10]]


# Trees
# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):  # every branch must be a tree as well
        if not is_tree(branch):
            return False
    return True

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

# Q1
def tree_max(t):
    """Return the max of a tree."""
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])
    # 要注意这里max不是对整个list求max,而是每一层都求max,一路递归到上到根部

# Q2
def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

# Q3
def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t) **2, [square_tree(branch) for branch in branches(t)])

# Q4
def find_path(tree, x):
    """Find path to the value x if x in the tree, else None"""
    if label(tree) == x:
        return [label(tree)]

    for path in [find_path(branch, x) for branch in branches(tree)]:
        if path:
            return [label(tree)] + path

# Q5
def prune(t, k):
    """a function that takes in a tree and a depth k and returns a new tree."""
    if k == 0:
        return tree(label(t))
    else:
        return tree(label(t), [prune(branch, k-1) for branch in branches(t)])



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
            tree(15, [tree(20), tree(21), tree(22)])])])])


    print(tree_max(T))
    # >>> 22

    print(height(T))
    # >>> 4

    print(T)
    print(square_tree(T))
    # >>> [1, [2, [4, [8], [9]], [5, [10], [11]]], [3, [6, [12], [13]], [7, [14], [15, [20], [21], [22]]]]]
    # >>> [1, [4, [16, [64], [81]], [25, [100], [121]]], [9, [36, [144], [169]], [49, [196], [225, [400], [441], [484]]]]]

    print(find_path(T, 10))  # >>> [1, 2, 5, 10]
    print(find_path(T, 5))   # >>> [1, 2, 5]
    print(find_path(T, 50))  # >>> None

    print(prune(T, 2))
    # >>> [1, [2, [4], [5]], [3, [6], [7]]]
