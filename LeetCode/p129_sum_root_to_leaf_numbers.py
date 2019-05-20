# P129 Sum Root to Leaf Numbers
# Medium


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.
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

def genTree(lst):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if not lst:
        return None

    LLL = log(len(lst)+1,2)
    if int(LLL) != LLL:
        print("List length is not complete, it must be 2^n - 1")
        raise ZeroDivisionError

    layers = []
    i, L = 0, 1

    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = []
        for i in layers[k]:
            if i is not None:
                cur.append(TreeNode(i))
            else:
                cur.append(None)

        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0 and cur[j] is not None:
                pre_root[rt_idx].left = cur[j]
            elif brc_side != 0 and cur[j] is not None:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return


class Solution:
    ### This is also using the showPaths method from Leetcode P112
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

    def translate(self, path):
        """
        translate a path into numbers by adding digit up
        example: path [1,2,3] returns number 123
        """
        N = len(path)
        result = 0
        for i in range(N):
            result += pow(10, N-1-i) * path[i]
        return result


    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        for path in self.allPath(root):
            result += self.translate(path)
        return result



if __name__ == '__main__':
    A = genTree([
        1,
        2,3
    ])
    assert Solution().sumNumbers(A) == 25, 'Example 1, 12 + 13 = 25'

    A = genTree([
        4,
        9, 0,
        5, 1, None, None
    ])
    assert Solution().sumNumbers(A) == 1026, 'Example 2, 495 + 491 + 40 = 1036'
    print('all passed')


