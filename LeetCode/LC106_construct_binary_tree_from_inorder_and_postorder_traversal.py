# P106 Construct Binary Tree from Inorder and Postorder Traversal
# Medium


# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.


from typing import *

from typing import *
from a0_TreeNode import *


class Solution:
    # Basically the same idea of my own slow version in leetcode P105
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        hmp = dict()
        for idx, val in enumerate(inorder):
            hmp[val] = idx

        def helper(postorder_lst):
            if not postorder_lst:
                return None
            root_val = postorder_lst[-1]
            root = TreeNode(root_val)
            root_idx = hmp[root_val]

            left_postorder, right_postorder = [], []
            for i in postorder_lst[::-1]:
                check_idx = hmp[i]
                if check_idx > root_idx:
                    right_postorder.insert(0, i)
                elif check_idx < root_idx:
                    left_postorder.insert(0, i)

            root.left = helper(left_postorder)
            root.right = helper(right_postorder)
            return root

        return helper(postorder)


class Solution(object):
    # STD ans
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node


if __name__ == "__main__":
    assert not Solution().buildTree([], []), "Edge 0"
    assert Solution().buildTree([1], [1]) == genTree([1]), "Edge 1"
    assert Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    print("All passed")
