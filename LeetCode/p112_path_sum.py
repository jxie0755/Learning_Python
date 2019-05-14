# P112 Path Sum
# Easy

# Given a binary tree and a sum,
# determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

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
    generate a binary tree according to a non-empty list of values
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
    def allPath(self, root):
        """show all the paths in a non-empty root"""
        result = []

        def helper(root, cur=[]):
            if not root.left and not root.right:
                cur.append(root.val)
                result.append(cur)
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


    def hasPathSum(self, root: TreeNode, target: int) -> bool:

        ### Borrow the idea of allPath
        def helper(root, cur=[]):
            if not root:
                return False

            elif not root.left and not root.right:
                cur.append(root.val)
                return sum(cur) == target

            else:
                left_cur, right_cur = cur[:], cur[:]
                left_cur.append(root.val)
                right_cur.append(root.val)
                return helper(root.left, left_cur) or helper(root.right, right_cur)

        return helper(root)




if __name__ == '__main__':
    A = None
    assert not Solution().hasPathSum(A, 0), "Edge 0"

    A = genTree([1])
    assert Solution().hasPathSum(A, 1), "Edge 1"

    A = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, None, 1
    ])
    assert Solution().hasPathSum(A, 22), "Example 1"

    print('All passed')
