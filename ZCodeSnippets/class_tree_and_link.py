# These are some functions that use both Linked List class and Tree class

from class_tree import Tree
from class_link import Link

def linky_paths(t):
    """Takes in a tree, t, and modifies each label to be the path from that node
    to the root
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(<1>, [Tree(<2, 1>)])"""

    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for b in t.branches:
            helper(b, t.label)

    helper(t, Link.empty)


# All Paths Linked Implement all_paths_linked which takes in a Tree t and returns a list of all paths from root to leaf in a tree with one catch – each path is represented as a linked list.

def all_paths_linked(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> all_paths_linked(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths_linked(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1, Link(3, Link(5)))]
    """
    # paths = []
    # if t.is_leaf():
    #     paths.append(Link(t.label))
    # for b in t.branches:
    #     for path in all_paths_linked(b):
    #         paths.append(Link(t.label, path))
    # return paths

    # Version 2 from exam_prep_07
    if t.is_leaf():
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result = result + [Link(t.label, path) for path in all_paths_linked(branch)]
    return result









