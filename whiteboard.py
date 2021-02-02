"""
https://leetcode.com/problems/validate-binary-search-tree/
P098 Validate Binary Search Tree
Medium


Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.
"""

from typing import *
from a0_TreeNode import *


class Solution_A:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Recursive verification
        """







if __name__ == "__main__":
    testCase = Solution_A()

    t1 = genTree([2, 1, 3])
    print(testCase.isValidBST(t1))
    assert testCase.isValidBST(t1), "Example 1"

    t2 = genTree([
        5,
        1, 4,
        None, None, 3, 6
    ])

    assert not testCase.isValidBST(t2), "Example 2"

    t3 = genTree([
        5,
        1, 6,
        None, None, 3, 7
    ])
    assert not testCase.isValidBST(t3), "Additional 1"

    t4 = genTree([0, None, -1])
    assert not testCase.isValidBST(t4), "Additional 2"

    print("All passed")
