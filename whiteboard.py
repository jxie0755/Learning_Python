"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
P114 Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

Notes:
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
from a0_TreeNode import *


class Solution_A:
    def flatten(self, root: TreeNode) -> None:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    testCase.flatten(T0)
    assert not T0, "Edge 0"

    T1 = TreeNode(0)
    testCase.flatten(T1)
    assert T1 == T1, "Edge 1"

    T2 = TreeNode(1)
    testCase.flatten(T2)
    assert T2 == T2, "Edge 11"

    T3 = genTree([
        1,
        2, 5,
        3, 4, None, 6
    ])
    testCase.flatten(T3)
    assert T3 == genTree([
        1,
        None, 2,
        None, None, None, 3,
        None, None, None, None, None, None, None, 4,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 5,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 6
    ]), "Example 1"

    print("All passed")
