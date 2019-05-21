# P111 Minimum Depth of Binary Tree
# Easy



# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
    ### The key is to find the first leaf
    def isLeaf(self, root):
        if root and not root.left and not root.right:
            return True
        return False

    def minDepth(self, root):
        if not root:
            return 0

        layer = [root]
        depth = 1
        while layer:
            new_layer = []
            for i in layer:
                if self.isLeaf(i):
                    return depth
                if i.left:
                    new_layer.append(i.left)
                if i.right:
                    new_layer.append(i.right)
            layer = new_layer
            depth += 1

        return depth


class Solution(object):
    # STD ans
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1



if __name__ == '__main__':
    A = None
    assert Solution().minDepth(A) == 0, 'Edge 0'

    A = TreeNode(1)
    assert Solution().minDepth(A) == 1, 'Edge 1'

    A = genTree([3,9,20,None, None, 15, 7])
    assert Solution().minDepth(A) == 2, 'Example 1'

    A = genTree([
        1,
        2, None
    ])
    assert Solution().minDepth(A) == 2, 'Additional 1'

    print('All passed')


