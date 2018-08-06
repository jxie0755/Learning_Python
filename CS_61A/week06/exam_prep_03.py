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

# Q1

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

if __name__ == '__main__':
    t1 = tree(5, [tree(1, [tree(2), tree(7, [tree(4, [tree(3)])])]), tree(2, [tree(0), tree(9)])])
    # the sums of the tree below are 20 (5+1+7+4+3), 8 (5+1+2), 7 (5+2+0), and 16 (5+2+9)
    # answer should be 20 - 7 = 13
    print(sum_range(t1)) # >>> 13