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
        """
        Recursive method to build a tree
        The key is:
        1. The current root node is always preorder[0]
        2. Determine the left side and right side of current root by indorer index
        """

        if not inorder:  # end case, no nodes
            return None
        else:
            root_val = preorder.pop(0) # pop the value and iterate to next recursion
            root_idx = inorder.index(root_val) # only when no duplicates (see question notes)

            T = TreeNode(root_val) # build the root node

            L_list = inorder[:root_idx] # recursively determine left side of the root
            if L_list:
                T.left = self.buildTree(preorder, L_list)

            R_list = inorder[root_idx+1:] # recursively determine right side of the root
            if R_list:
                T.right = self.buildTree(preorder, R_list)

            return T



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
