"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
P106 Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

from typing import *
from a0_TreeNode import *


class Solution_A:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert not testCase.buildTree([], []), "Edge 0"

    assert testCase.buildTree([1], [1]) == genTree([1]), "Edge 1"

    assert testCase.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    print("All passed")
