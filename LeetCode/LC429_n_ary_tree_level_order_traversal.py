# LC429 N-ary Tree Level Order Traversal
# Easy


# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Note:
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.

from A01_ListNode import *


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:

    # Version A, use showLayer idea
    def levelOrder(self, root: "Node") -> List[List[int]]:
        """Show the tree layer by layer from top to bottom"""
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                for child in node.children:
                    next_level.append(child)
            current = next_level
            result.append(vals)

        return result


if __name__ == "__main__":
    C1, C2 = Node(5, []), Node(6, [])
    B1, B2, B3 = Node(3, [C1, C2]), Node(2, []), Node(4, [])
    A = Node(1, [B1, B2, B3])

    assert Solution().levelOrder(A) == [
        [1],
        [3, 2, 4],
        [5, 6]
    ], "Example"

    print("All passed")
