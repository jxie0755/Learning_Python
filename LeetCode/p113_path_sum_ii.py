# P113 Path Sum II
# Medium


# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.

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
    def allPath(self, root):
        """show all the paths in a non-empty root"""
        result = []

        def helper(root, cur=[]):
            if not root:
                return None
            elif not root.left and not root.right:
                cur.append(root.val)
                result.append(cur)
            else:
                if root.left:
                    new_cur = cur[:]
                    new_cur.append(root.val)
                    helper(root.left, new_cur)
                if root.right:
                    new_cur = cur[:]
                    new_cur.append(root.val)
                    helper(root.right, new_cur)

        helper(root)
        return result


    def pathSum(self, root: TreeNode, target: int):
        result = []
        for i in self.allPath(root):
            if sum(i) == target:
                result.append(i)
        return result


if __name__ == '__main__':
    A = None
    assert Solution().pathSum(A, 0) == [], "Edge 0"

    A = genTree([1])
    assert Solution().pathSum(A, 1) == [
        [1]
    ], "Edge 1"

    A = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, 5, 1
    ])
    assert Solution().pathSum(A, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ], "Example 1"

    print('All passed')
