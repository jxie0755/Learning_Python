# P095 Unique Binary Search Trees II
# Medium

# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
# TODO after learning BST

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
    def generateTrees(self, n: int) -> List[TreeNode]:
        data = list(range(1, n))


if __name__ == '__main__':
    assert Solution().generateTrees(3) == [
        genTree([1, None, 3, None, None, 2, None]),
        genTree([3, 2, None, 1, None, None, None]),
        genTree([3, 1, None, None, 2, None, None]),
        genTree([2, 1, 3]),
        genTree([1, None, 2, None, None, None, 3]),
    ], 'Example 1'

    print('all passed')
