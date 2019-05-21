# P104 Maximum Depth of Binary Tree
# Easy


# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

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


def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if not lst:
        return None

    N = len(lst)
    if i > N:
        return None

    val = lst[i-1]
    node = TreeNode(val)
    if val is not None:
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    A = None
    assert Solution().maxDepth(A) == 0, 'Edge 0'

    A = TreeNode([1])
    assert Solution().maxDepth(A) == 1, 'Edge 1'

    A = genTree([3,9,20,None, None, 15, 7])
    assert Solution().maxDepth(A) == 3, 'Example'

    print('All passed')
