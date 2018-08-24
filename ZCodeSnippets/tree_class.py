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

    def get_label(self):
        return self.label

    def get_branches(self):
        return self.branches

    def is_leaf(self):
        return not self.branches



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

    # Set getter functions
    print(T.get_label())     # >>> 1
    print(T.get_branches())  # >>> [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])]


