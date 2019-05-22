# P114 Flatten Binary Tree to Linked List
# Medium

# Given a binary tree, flatten it to a linked list in-place.
from typing import *

# Definition for a binary tree node.
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def isLeaf(self):
        try:
            leftval = self.left.val
        except AttributeError:
            leftval = None
        try:
            rightval = self.right.val
        except AttributeError:
            rightval = None

        return leftval and rightval

def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


class Solution:
    def preorderTraversal(self, t):
        """return a flat list of the binary tree including None"""
        if not t:
            return [] # skip none
        return [t.val] + self.preorderTraversal(t.left) + self.preorderTraversal(t.right)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        travel = self.preorderTraversal(root)
        if len(travel) > 1:
            i = 1
            root.left = None
            while i != len(travel):
                new = TreeNode(travel[i])
                root.right = new
                root = new
                i += 1


if __name__ == '__main__':
    A = None
    Solution().flatten(A)
    assert not A, 'Edge 0'

    A = TreeNode(0)
    Solution().flatten(A)
    assert A == A, 'Edge 1'

    A = TreeNode(1)
    Solution().flatten(A)
    assert A == A, 'Edge 2'

    A = genTree([
        1,
        2,5,
        3,4,None,6
    ])
    Solution().flatten(A)
    assert A == genTree([
        1,
        None, 2,
        None, None, None, 3,
        None, None, None, None,
        None, None, None, 4,
        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ]), 'Example 1'

    print('all passed')
