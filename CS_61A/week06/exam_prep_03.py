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

# Q1

def sum_range(t):
    """Returns the range of the sums of t, that is,
    the difference between the largest and the smallest sums of t."""
    def helper(t):
        if _________________________________________:
            return [_____________, _____________]
        else:
            a = min([___________________________])
            b = max([___________________________])
            x = __________________________________
            return [b + x, a + x]
    x, y = helper(t)
    return x - y
