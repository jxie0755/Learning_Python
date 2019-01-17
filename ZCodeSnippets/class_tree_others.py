from class_tree import Tree

# Other Tree related functions:
# Fibonacci tree setup by Tree class
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def fib_tree(n):
    """A Fibonacci tree.
    >>> print(fib_tree(4))  # 0 1 1 2 3
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


# Factor tree
def factor_tree(n):
    """
    Returns a factor tree.
    Recall that in a factor tree, multiplying the leaves together is the prime factorization of the root, n
    >>> print(factor_tree(20))
    20
      2
      10
        2
        5
    """
    for i in range(2, n):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)


# Containing search
def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf() and n == 1:
        return t.label == elem
    elif t.label == elem:
        return True in [contains(elem, n - 1, b) for b in t.branches]
    else:
        return True in [contains(elem, n, b) for b in t.branches]



# Siblings
def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.
    >>> a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
    >>> siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [b.label for b in t.branches if len(t.branches) > 1]
    for b in t.branches:
        result += siblings(b)
    return result


# Implement the Sib class that inherits from Tree.
# In addition to label and branches, a Sib instance t has an attribute siblings that stores the number of siblings t has in Sib trees containing t as a node.
# Assume that the branches of a Sib instance will never be mutated or re-assigned.

class Sib(Tree):
    """A tree that knows how many siblings it has.
    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        Tree.__init__(self, label, branches)
        self.siblings = 0
        for b in self.branches:
            b.siblings = len(self.branches) - 1


# Use tree to represent and search file directories:
def find_file_path(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]), Tree('ecc', [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path(t, 'file.py')
    '/data/ecc/file.py'
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str and t.is_leaf():
                                   # not necessary but to avoid folder and file as the same name
            return path_so_far + '/' + t.label
        elif t.is_leaf():
            return None
        for b in t.branches:
            result = helper(b, file_str, path_so_far + '/' + t.label)
            if result:
                return result
    return helper(t, file_str, '')
