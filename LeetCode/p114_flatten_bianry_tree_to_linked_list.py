# P114 Flatten Binary Tree to Linked List
# Medium

# Given a binary tree, flatten it to a linked list in-place.
from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    def preorderTraversal(self, t):
        """return a flat list of the binary tree including None"""
        if not t:
            return [] # skip none
        return [t.val] + self.preorderTraversal(t.left) + self.preorderTraversal(t.right)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        travel = self.preorderTraversal(root)
        if len(travel) > 1:
            i = 1
            root.left = None
            while i != len(travel):
                new = TreeNode(travel[i])
                root.right = new
                root = new
                i += 1


if __name__ == "__main__":
    A = None
    Solution().flatten(A)
    assert not A, "Edge 0"

    A = TreeNode(0)
    Solution().flatten(A)
    assert A == A, "Edge 1"

    A = TreeNode(1)
    Solution().flatten(A)
    assert A == A, "Edge 2"

    A = genTree([
        1,
        2,5,
        3,4,None,6
    ])
    Solution().flatten(A)
    assert A == genTree([
        1,
        None, 2,
        None, None, None, 3,
        None, None, None, None,
        None, None, None, 4,
        None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ]), "Example 1"

    print("all passed")
