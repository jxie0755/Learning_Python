# lass Sib(Tree):
#     """A tree that knows how many siblings it has.
#
#     """
#     def __init__(self, label, branches=[]):
#         self.sibilings = 0
#         self.branches = branches
#         for b in self.branches:
#             b.siblings = len(self.branches) - 1

class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])

# (b)
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
        self.siblings = 0
        self.label = label
        self.branches = branches
        for b in self.branches:
            b.siblings = len(self.branches) - 1
