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

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

if __name__ == '__main__':
    T = tree(1, [
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
            tree(4)])])])

    print(tree_max(T))
    # >>> 4

    print(height(T))
    # >>> 3
