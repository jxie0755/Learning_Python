# P226 Invert Binary Tree
# Easy

# Invert a binary tree.
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    # Use showLayers (full layer)

    def showLayers(self, root): # Omit None
        """Show the tree layer by layer from top to bottom"""
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result



    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        pass



if __name__ == '__main__':
    assert Solution().invertTree(None) is None, 'Edge 0'

    A = genTree([1])
    assert Solution().invertTree(A) == A, 'Edge 1'

    A = genTree([
        4,
        2,7,
        1,3,6,9
    ])

    B = genTree([
        4,
        7,2,
        9,6,3,1
    ])
    assert Solution().invertTree(A) == B, 'Example 1'

    A = genTree([
        4,
        2, 7,
        None, 3, None, 9
    ])

    B = genTree([
        4,
        7, 2,
        9, None, 3, None
    ])
    assert Solution().invertTree(A) == B, 'Example 1b'

    print('all passed')
