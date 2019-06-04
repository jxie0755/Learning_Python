# P111 Minimum Depth of Binary Tree
# Easy



# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    # The key is to find the first leaf
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


