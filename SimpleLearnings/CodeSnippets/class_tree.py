"""
This is an extension of learning from CS61A, tree recursion
tree_recursion_tree.py summarized all the tree functions.
This is to convert functional setup in tree_recursion_tree.py into a full Tree class which contains all the methods within.

Use by:
from ZCodeSnippets.tree_class import Tree
"""

from class_link import Link

class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        """
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> repr(T)
        "Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])"
        """
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(self.label, branch_str)

    def __str__(self):
        """
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T)
        1
          2
            4
            5
          3
            6
            7
        """
        return "\n".join(self.indented())

    def indented(self):  # this is to recursively print a Tree.
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append("  " + line)
        return [str(self.label)] + lines
        # This is the original print_tree fucntion is a series of print() at different lines.
        # But __str__ requires to return a str object.

    def eq_fake(self, other):
        """
        >>> T1 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3)])
        >>> T2 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3)])
        >>> T1.eq_fake(T2)
        True
        >>> T3 = Tree(1, [Tree(2), Tree(3)])
        >>> T4 = Tree(1, [Tree(3), Tree(2)])
        >>> T3.eq_fake(T4)
        False
        """
        return self.extract_nodes() == other.extract_nodes()
    # This method needs improvement
    # It will not show True if two tree is mirrored.

    def __eq__(self, other):
        """
        >>> T1 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T2 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T1 == T2
        True
        """
        return repr(self) == repr(other)

    # Set getter functions
    def get_label(self):
        """
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.get_label()
        1
        """
        return self.label

    def get_branches(self):
        """
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.get_branches()
        [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])]
        """
        return self.branches

    # Set bool function to tell whether it is a leaf
    # There is no need to tell whether it is a tree, because the object is created under the tree class.
    # Leaf has no branches, if it is not a leaf, then it must be a tree with branches.
    def is_leaf(self):
        """To tell whether the tree instance is a leaf or a tree with branches"""
        return not self.branches


    def count_nodes(self):
        """Return total number of nodes in this tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.count_nodes()
        7
        """
        # return len(self.extract_nodes())
        return sum([1] + [b.count_nodes() for b in self.branches])

    def count_leaves(self):
        """Count the leaves of a tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.count_leaves()
        4
        """
        if self.is_leaf():
            return 1
        else:
            return sum([b.count_leaves() for b in self.branches])


    def extract_nodes(self):
        """return a flat list contains all the nodes
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.extract_nodes()
        [1, 2, 4, 5, 3, 6, 7]
        """
        return [self.label] + sum([b.extract_nodes() for b in self.branches], [])


    def extract_leaves(self):
        """Return a list containing all the leaf labels of tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.extract_leaves()
        [4, 5, 6, 7]
        """
        if self.is_leaf():
            return [self.label]
        else:
            return sum([b.extract_leaves() for b in self.branches], [])


    def increment_trees(self, n):
        """Return a tree like self but with every tree labels incremented of n
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.increment_trees(2))
        3
          4
            6
            7
          5
            8
            9
        """
        return Tree(self.label + n, [b.increment_trees(n) for b in self.branches])


    def square_tree(self):
        """Return a tree with the square of every element in t
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.square_tree())
        1
          4
            16
            25
          9
            36
            49
        """
        return Tree(self.label **2, [b.square_tree() for b in self.branches])


    def increment_leaves(self, n):
        """Return a tree like self but with only leaf labels incremented of n
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.increment_leaves(2))
        1
          2
            6
            7
          3
            8
            9
        """
        if self.is_leaf():
            return Tree(self.label + n)
        else:
            return Tree(self.label, [b.increment_leaves(n) for b in self.branches])


    def max_tree_v(self):
        """return the max labels in this tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.max_tree_v()
        7
        """
        return max([self.label] + [b.max_tree_v() for b in self.branches])
        # return max(self.extract_nodes())

    def max_leaf_v(self):
        """return the max leaf label in this tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.max_leaf_v()
        7
        """
        return max(self.extract_leaves())


    def max_height(self):
        """Return the max height of a tree
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.max_height()
        3
        """
        if self.is_leaf():
            return 1
        else:
            return 1 + max([b.max_height() for b in self.branches])

    def find_path(self, x):
        """Find path to the value x if x in the tree, else None
        >>> T = Tree(1, [Tree(3, [Tree(4), Tree(3)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.find_path(7)
        [1, 3, 7]
        >>> T.find_path(3)  # iteration sequence, stop at first seen
        [1, 3]
        """
        if self.label == x:
            return [self.label]

        for path in [b.find_path(x) for b in self.branches]:
            if path:
                return [self.label] + path

    def finder(self, keywd):
        """Returns True if t contains a node with the value of keywd and False otherwise.
        >>> T = Tree(1, [Tree(3, [Tree(4), Tree(3)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.finder(4)
        True
        >>> T.finder(10)
        False
        """
        return self.label == keywd or True in [b.finder(keywd) for b in self.branches]
        # return keywd in self.extract_nodes()

    def sum_range(self):
        """Returns the range of the sums of t, that is:
        the difference between the largest and the smallest sums of t.
        return as a pair of value [min, max]
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T.sum_range()  # 1-2-4 and 1-3-7
        [7, 11]
        """
        if self.is_leaf():
            return [self.label, self.label]
        else:
            min_v = min([b.sum_range()[0] for b in self.branches])
            max_v = max([b.sum_range()[1] for b in self.branches])
            x = self.label
            return [min_v + x, max_v + x]

    def prune(self, k):
        """Return a tree that takes in a tree only to the depth k
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.prune(1))
        1
          2
          3
        """
        if k == 0:
            return Tree(self.label)
        else:
            return Tree(self.label, [b.prune(k-1) for b in self.branches])

    def copy_tree(self):
        """Returns a copy of t. Only for testing purposes.
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T_copy = T.copy_tree()
        >>> T_copy == T
        True
        """
        return Tree(self.label, [b.copy_tree() for b in self.branches])


    def replace_label(self, old, new):
        """replace a tree label to a new value is the value == old
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.replace_label(2, 10))
        1
          10
            4
            5
          3
            6
            7
        """
        if self.label == old:
            return Tree(new, [b.replace_label(old, new) for b in self.branches])
        else:
            return Tree(self.label, [b.replace_label(old, new) for b in self.branches])

    def replace_leaf(self, old, new):
        """replace a leaf label to a new value is the value == old
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.replace_leaf(4, 10))
        1
          2
            10
            5
          3
            6
            7
        >>> print(T.replace_leaf(2, 10))  # only apply to leaves
        1
          2
            4
            5
          3
            6
            7
        """
        if self.is_leaf() and self.label == old:
            return Tree(new)
        else:
            return Tree(self.label, [b.replace_leaf(old, new) for b in self.branches])


    def sprout_leaves(self, vals):
        """Sprout new leaves containing the data in vals at each leaf in
        the original tree t and return the resulting tree.
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.sprout_leaves([10, 20]))
        1
          2
            4
              10
              20
            5
              10
              20
          3
            6
              10
              20
            7
              10
              20
        """
        if self.is_leaf():
            return Tree(self.label, [Tree(i) for i in vals])
        else:
            return Tree(self.label, [b.sprout_leaves(vals) for b in self.branches])


    def prune_repeats(self, seen=[]):
        """remove the tree in the branches that has shown before
        >>> from class_tree import fib_tree
        >>> T = fib_tree(6)
        >>> print(T) # a binary tree to 6th fib, starting from 0th (0,1,1,2,3,5,8)
        8
          3
            1
              0
              1
            2
              1
              1
                0
                1
          5
            2
              1
              1
                0
                1
            3
              1
                0
                1
              2
                1
                1
                  0
                  1
        >>> T.prune_repeats()
        >>> print(T)
        8
          3
            1
              0
              1
            2
          5
            2
            3
              2
        """
        self.branches = [b for b in self.branches if b not in seen]
        seen.append(self)
        for b in self.branches:
            b.prune_repeats(seen)

    # Set basic calculation and comparison
    def __add__(self, other):
        """
        Add two tree together
        If a node at any particular position is present in one tree but not the other, it should be present in the new tree as well.
        >>> T1 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3)])
        >>> T2 = Tree(1, [Tree(2, [Tree(10), Tree(10)]), Tree(100, [Tree(1000), Tree(2000)])])
        >>> print(T1+T2)
        2
          4
            14
            15
          103
            1000
            2000
        """
        lab = self.label + other.label
        b1, b2 = self.branches, other.branches
        while len(b1) > len(b2):
            b2 = b2 + [Tree(0)]
        while len(b2) > len(b1):
            b1 = b1 + [Tree(0)]
        return Tree(lab, [b[0] + b[1] for b in zip(b1, b2)])


    def all_paths(self):
        """to get all path of a tree in list form in a big list
        >>> X = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9)])])])
        >>> path_list = X.all_paths()
        >>> for i in path_list:
        ...     print(i)
        [1, 2, 4]
        [1, 2, 5]
        [1, 3, 6]
        [1, 3, 7, 8]
        [1, 3, 7, 9]
        """

        def helper(tree):
            """return a list of Linked list that are all the paths in the tree
            need to use the Link class as well
            >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
            >>> print(helper(T))
            [[1, [2, 4], [2, 5]], [1, [3, 6], [3, 7]]]
            """
            paths = []
            if tree.is_leaf():
                paths.append(tree.label)
            for b in tree.branches:
                for path in helper(b):
                    paths.append([tree.label, path])
            return paths  # can't not print all paths right away as it is a recursive function

        def flatten(lnk_lst):
            """To flatten a linked list like list in the form of:
            [a, [b, [c, d]]]
            return a flattened list in the form of:
            [a, b, c, d]
            """
            if isinstance(lnk_lst[1], list):
                return [lnk_lst[0]] + flatten(lnk_lst[1])
            else:
                return lnk_lst

        all_paths = helper(self)
        return [flatten(path) for path in all_paths]

    # All Paths Linked Implement all_paths_linked which takes in a Tree t and returns a list of all paths from root to leaf in a tree with one catch â€" each path is represented as a linked list.
    def all_paths_linked(self):
        """return a list of Linked list that are all the paths in the tree
        need to use the Link class as well
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T.all_paths_linked())
        [Link(1, Link(2, Link(4))), Link(1, Link(2, Link(5))), Link(1, Link(3, Link(6))), Link(1, Link(3, Link(7)))]
        """
        # From exam_prep_07
        if self.is_leaf():
            return [Link(self.label)]
        result = []
        for b in self.branches:
            result = result + [Link(self.label, path) for path in b.all_paths_linked()]
        return result


    def convert_to_list(self):
        """This converts the tree strcture to a nested list type
        >>> T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> T0 = Tree(1)
        >>> print(T0.convert_to_list())
        [1]
        >>> T1 = Tree(1, [Tree(2), Tree(3)])
        >>> print(T1.convert_to_list())
        [[1, 2], [1, 3]]
        >>> T2 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
        >>> print(T2.convert_to_list())
        [[1, [2, 4], [2, 5]], [1, [3, 6], [3, 7]]]
        >>> T3 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9),Tree(10)])])])
        >>> print(T3.convert_to_list())
        [[1, [2, 4], [2, 5]], [1, [3, 6], [3, [7, 8], [7, 9], [7, 10]]]]
        """
        if self.is_leaf():
            return [self.label]
        else:
            tail = [b.convert_to_list() for b in self.branches]
            return [[self.label] + i for i in tail]


# Addtiona functions
def linky_paths(t):
    """Takes in a tree, t, and modifies each label to be the path from that node
    to the root
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(<1>, [Tree(<2, 1>)])
    """

    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for b in t.branches:
            helper(b, t.label)

    helper(t, Link.empty)


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
    >>> t = Tree("data", [Tree("comm", [Tree("dummy.py")]), Tree("ecc", [Tree("hello.py"), Tree("file.py")]), Tree("file2.py")])
    >>> find_file_path(t, "file2.py")
    "/data/file2.py"
    >>> find_file_path(t, "dummy.py")
    "/data/comm/dummy.py"
    >>> find_file_path(t, "hello.py")
    "/data/ecc/hello.py"
    >>> find_file_path(t, "file.py")
    "/data/ecc/file.py"
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str and t.is_leaf():
                                   # not necessary but to avoid folder and file as the same name
            return path_so_far + "/" + t.label
        elif t.is_leaf():
            return None
        for b in t.branches:
            result = helper(b, file_str, path_so_far + "/" + t.label)
            if result:
                return result
    return helper(t, file_str, "")
