"""Colin's notes on recursion"""

def stairs(n):
    """Give the number of ways to take n steps, given that at each step, you can choose to take 1, 2
    >>> stairs(2)
    2
    >>> stairs(4)
    5
    >>> stairs(1)
    1
    >>> stairs(3)
    3
    """
    ### Your code here ###
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stairs(n-1) + stairs(n-2)

def kstairs(n, k):
    """Give the number of ways to take n steps, given that at each step, you can choose to take 1,2,3,k-2,k-1 or k steps,
    >>> kstairs(5, 2)
    8
    >>> kstairs(5, 5)
    16
    >>> kstairs(10, 5)
    464
    """
    if n == 0:
        return 0
    if n <= k:
        return 2**(n-1)
    return sum([kstairs(n - i, k) for i in range(1, k + 1)])

def permutations(lst):
    """List all permutations of the given list
    enumerate() function might be helpful
    >>> permutations(["angie", "cat"])
    [["angie", "cat"], ["cat", "angie"]]
    >>> permutations([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    ### Your code here ###
    if len(lst) <= 1:
        return [lst]
    total = []
    for i, k in enumerate(lst):
        total.extend([[k] + p for p in permutations(lst[:i] + lst[i+1:])])
    return total


class Tree(object):
    """ A tree with internal values. """
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ", {0}, {1}".format(repr(self.left), repr(self.right))
        return "Tree({0})".format(args)

    def print(self):
        def print_helper(tree, depth):
            if tree.right:
                print_helper(tree.right, depth + 1)
            print("{0}{1}".format("\t" * depth, tree.entry))
            if tree.left:
                print_helper(tree.left, depth + 1)
            print_helper(self, 0)


def tree_to_reversed_list(tree):
    """
    >>> t = Tree(5, Tree(1, None, Tree(4)), Tree(7, Tree(6), Tree(8)))
    >>> tree_to_reversed_list(t)
    [8, 7, 6, 5, 4, 1]
    """
    ### Your code here ###
    lst = []
    if tree is not None:
        if tree.right:
            lst.extend(tree_to_reversed_list(tree.right))
    lst.append(tree.entry)
    if tree.left:
        lst.extend(tree_to_reversed_list(tree.left))
    return lst
