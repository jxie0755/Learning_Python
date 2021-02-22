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


class Solution_A1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Basically the same idea the slow version in leetcode P105-A1
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


class Solution_A2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Similar idea of P105-A2
        Recursively Pop from the end, locate the head on which side of the tree
        """
        if not inorder:  # end case, no nodes
            return None

        root_val = postorder.pop()  # must use pop to carry the change into recursion
        # restricted by List structure, Array cannot pop

        in_idx = inorder.index(root_val)  # only when no duplicates (see question notes)
        T = TreeNode(root_val)  # build the root node

        L_inorder = inorder[:in_idx]  # recursively determine left side of the root
        R_inorder = inorder[in_idx + 1:]  # recursively determine right side of the root

        # confirm which side
        if postorder and postorder[-1] in R_inorder:
            T.right = self.buildTree(R_inorder, postorder)

        if postorder and postorder[-1] in L_inorder:
            T.left = self.buildTree(L_inorder, postorder)
            # preorder.pop in this step will carry over to next if condition

        return T



class Solution_STD:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        STD version, similar to P105-STD
        """
        return self.buildTreeRecu(postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, postorder, inorder, post_end_idx, in_start_idx, in_end_idx):
        if in_start_idx == in_end_idx:
            return None

        root_val = postorder[post_end_idx - 1]
        T = TreeNode(root_val)
        in_idx =inorder.index(root_val)


        T.left = self.buildTreeRecu(postorder, inorder,
                                    post_end_idx - 1 - (in_end_idx - in_idx - 1),
                                    in_start_idx, in_idx
                                    )

        T.right = self.buildTreeRecu(postorder, inorder,
                                     post_end_idx - 1,
                                     in_idx + 1, in_end_idx
                                     )

        return T


if __name__ == "__main__":
    testCase = Solution_STD()

    assert not testCase.buildTree([], []), "Edge 0"

    assert testCase.buildTree([1], [1]) == genTree([1]), "Edge 1"

    assert testCase.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    assert testCase.buildTree([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1]) == genTree([
        1,
        2, 3,
        4, 5, 6, 7
    ]), "Additional 1"

    print("All passed")
