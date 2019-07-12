# P199 Binary Tree Right Side View
# Medium


# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Use the showLayers method and add each Layer's last item to a list
    def showLayers(self, root):  # Omit None
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

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        for i in self.showLayers(root):
            result.append(i[-1])
        return result


if __name__ == "__main__":
    assert Solution().rightSideView(None) == [], "Edge 0"

    A = genTree([
        1,
        2,3,
        None, 5, None, 4
    ])

    assert Solution().rightSideView(A) == [1,3,4], "Example 1"

    A = genTree([
        1,
        2, None,
        None, 5, None, None
    ])

    assert Solution().rightSideView(A) == [1, 2, 5], "Additional 1"

    A = genTree([
        1,
        2, 3,
        None, 5, None, None
    ])

    assert Solution().rightSideView(A) == [1, 3, 5], "Additional 1"

    print("all passed")

