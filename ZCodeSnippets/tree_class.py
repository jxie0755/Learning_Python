# This is an extension of learning from CS61A, tree recursion

# tree_recursion_tree.py summarized all the tree functions.

# This is to convert tree_recursion_tree.py into a full Tree class which contains all the methods within.


class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):  # this is to recursively print a Tree.
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
        # This is the original print_tree fucntion is a series of print() at different lines.
        # But __str__ requires to return a str object.

    # Set getter functions
    def get_label(self):
        return self.label

    def get_branches(self):
        return self.branches

    # Set bool function to tell whether it is a leaf
    # There is no need to tell whether it is a tree, because the object is created under the tree class.
    # Leaf has no branches, if it is not a leaf, then it must be a tree with branches.
    def is_leaf(self):
        """To tell whether the tree instance is a leaf or a tree with branches"""
        return not self.branches


    def count_nodes(self):
        # return len(self.extract_nodes())
        return sum([1] + [b.count_nodes() for b in self.branches])

    def count_leaves(self):
        """Count the leaves of a tree"""
        if self.is_leaf():
            return 1
        else:
            return sum([b.count_leaves() for b in self.branches])


    def extract_nodes(self):
        """return a flat list contains all the nodes"""
        return [self.label] + sum([b.extract_nodes() for b in self.branches], [])


    def extract_leaves(self):
        """Return a list containing all the leaf labels of tree"""
        if self.is_leaf():
            return [self.label]
        else:
            return sum([b.extract_leaves() for b in self.branches], [])


    def increment_trees(self, n):
        """Return a tree like self but with every tree labels incremented of n"""
        return Tree(self.label + n, [b.increment_trees(n) for b in self.branches])

    def increment_leaves(self, n):
        """Return a tree like self but with only leaf labels incremented of n """
        if self.is_leaf():
            return Tree(self.label + n)
        else:
            return Tree(self.label, [b.increment_leaves(n) for b in self.branches])


    def max_tree_v(self):
        """return the max labels in this tree"""
        return max([self.label] + [b.max_tree_v() for b in self.branches])
        # return max(self.extract_nodes())

    def max_leaf_v(self):
        """return the max leaf label in this tree"""
        return max(self.extract_leaves())


    def max_height(self):
        """Return the max height of a tree"""
        if self.is_leaf():
            return 1
        else:
            return 1 + max([b.max_height() for b in self.branches])

    def find_path(self, x):
        """Find path to the value x if x in the tree, else None"""
        if self.label == x:
            return [self.label]

        for path in [b.find_path(x) for b in self.branches]:
            if path:
                return [self.label] + path

    def finder(self, keywd):
        """Returns True if t contains a node with the value of keywd and False otherwise."""
        return self.label == keywd or True in [b.finder(keywd) for b in self.branches]
        # return keywd in self.extract_nodes()

    def sum_range(self):
        """Returns the range of the sums of t, that is:
        the difference between the largest and the smallest sums of t.
        return as a pair of value [min, max]
        """
        if self.is_leaf():
            return [self.label, self.label]
        else:
            min_v = min([b.sum_range()[0] for b in self.branches])
            max_v = max([b.sum_range()[1] for b in self.branches])
            x = self.label
            return [min_v + x, max_v + x]


if __name__ == '__main__':
    T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
    print(T)
    # >>>
    # 1
    #   2
    #     4
    #     5
    #   3
    #     6
    #     7

    print(repr(T))
    # >>>
    # Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])

    print(T.get_label())     # >>> 1
    print(T.get_branches())  # >>> [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])]

    print(T.count_nodes())   # >>> 7
    print(T.count_leaves())  # >>> 4

    print(T.extract_nodes()) # >>> [1, 2, 4, 5, 3, 6, 7]
    print(T.extract_leaves())    # >>> [4, 5, 6, 7]

    print(T.increment_trees(2))
    # >>>
    # 3
    #   4
    #     6
    #     7
    #   5
    #     8
    #     9
    print(T.increment_leaves(2))

    # >>>
    # 1
    #   2
    #     6
    #     7
    #   3
    #     8
    #     9

    print(T.max_tree_v())  # >>> 7
    print(T.max_leaf_v())  # >>> 7

    print(T.max_height())  # >>> 3

    print(T.find_path(7))  # >>> [1, 3, 7]  # does not have to end at leaf

    print(T.finder(4)) # >>> True
    print(T.finder(10)) # >>> False

    print(T.sum_range()) # >>> [11, 7]












