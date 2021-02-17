"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
P105 Construct Binary Tree from Preorder and Inorder Traversal
Medium


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

from a0_TreeNode import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return genTree(preorder)



if __name__ == "__main__":
    testCase = Solution()

    assert not testCase.buildTree([], []), "Edge 0"

    assert testCase.buildTree([1], [1]) == genTree(
        [1]
    ), "Edge 1"

    assert testCase.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    print("All passed")
