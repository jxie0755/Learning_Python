# P107 Binary Tree Level Order Traversal II
# Easy


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    # Use the showLayers operation but the maximum time limit is exceeded
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

    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        elif not root.left and not root.right:
            return [[root.val]]

        result = []
        for i in self.showLayers(root)[::-1]:
            filtered = list(filter(lambda x: x is not None, i))  # Be careful with the t.val == 0
            result.append(filtered)
        return result[1:]


class Solution:
    def levelOrderBottom(self, root):
        # STD ans
        # Almost the same way as I tried, but it does not add None to next layer
        # Use i.left and i.right to screen each node in current layer and only add the branch to next layer if the branch exist
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                if node:
                    vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result[::-1]


class Solution:
    def levelOrderBottom(self, root):
        # A more structed stack method accoding to last method
        # First build up the stack all the way to the bottom to get nodes at each layer
        # Then extract the values of each node in every layer
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        stack = [[root]]
        current = [root]
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack.append(next_level)
            current = next_level

        result = []
        for i in stack[-2::-1]:
            vals = []
            for node in i:
                if node:
                    vals.append(node.val)
            result.append(vals)

        return result


if __name__ == "__main__":
    A = None
    assert Solution().levelOrderBottom(A) == [], "Edge 0"

    A = genTree([1])
    assert Solution().levelOrderBottom(A) == [[1]], "Edge 1"

    A = genTree([3, 9, 20, None, None, 15, 7])
    assert Solution().levelOrderBottom(A) == [
        [15, 7],
        [9, 20],
        [3]
    ], "Example"

    A = genTree([
        0,
        2, 4,
        1, None, 3, -1,
        5, 1, None, None, 6, None, 8, None])
    assert Solution().levelOrderBottom(A) == [
        [5, 1, 6, 8],
        [1, 3, -1],
        [2, 4],
        [0]
    ]

    print("All passed")
