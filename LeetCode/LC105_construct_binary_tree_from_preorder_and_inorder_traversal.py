"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
P105 Construct Binary Tree from Preorder and Inorder Traversal
Medium


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

from a0_TreeNode import *


class Solution_A1:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Recursive method
        Build a tree, and recursively determine the left side and right side by inorder index
        This will pass but exceed max time limit
        """

        if not preorder:
            return None
        root_val = preorder[0]
        T = TreeNode(root_val)
        root_idx = inorder.index(root_val)  # root在inorder中的位置

        left_found, right_found = False, False
        left_preorder, right_preorder = [], []
        left_inorder, right_inorder = [], []

        # 从preorder后面找到left和right的值
        for i in range(1, len(preorder)):
            check = preorder[i]
            if check in inorder:
                check_idx = inorder.index(check)
                if check_idx < root_idx and not left_found:  # 第一个出现的在root_idx左侧的preorder值
                    left_preorder = preorder[i:]
                    left_inorder = inorder[:root_idx]
                    left_found = True
                if check_idx > root_idx and not right_found:  # 第二个出现的在root_idx左侧的preorder值
                    right_preorder = preorder[i:]
                    right_inorder = inorder[root_idx:]
                    right_found = True
                if left_found and right_found:
                    break

        T.left = self.buildTree(left_preorder, left_inorder)
        T.right = self.buildTree(right_preorder, right_inorder)
        return T


class Solution_A2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Recursive method, similar to A1
        The key is:
        1. The current root node is always preorder[0]
        2. Determine the left side and right side of current root by indorer index
        This is much faster
        """

        if not inorder:  # end case, no nodes
            return None
        else:
            root_val = preorder.pop(0)  # must use pop to carry the change into recursion
                                        # restricted by List structure, Array cannot pop
            in_idx = inorder.index(root_val)  # only when no duplicates (see question notes)
            T = TreeNode(root_val)  # build the root node

            L_inorder = inorder[:in_idx]  # recursively determine left side of the root
            if L_inorder:
                T.left = self.buildTree(preorder, L_inorder)
                # preorder.pop in this step will carry over to next if condition

            R_inorder = inorder[in_idx + 1:]  # recursively determine right side of the root
            if R_inorder:
                T.right = self.buildTree(preorder, R_inorder)

            return T


class Solution_STD:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        STD version, recursive
        Save space by jumping the index stead of creating new inorder list
        """
        return self.buildTreeRecu(preorder, inorder,
                                  0,
                                  0, len(inorder))

    def buildTreeRecu(self, preorder, inorder, pre_start_idx: int, in_start_idx: int, in_end_idx: int) -> TreeNode:
        """
        A helper function, in addition to the preorder and inorder list
        pre_star defines start index of preorder to search, no need to define the end
        in_start and in_end defines range of inorder to search
        """
        if in_start_idx == in_end_idx:
            return None

        root_val = preorder[pre_start_idx]
        T = TreeNode(root_val)
        in_idx = inorder.index(root_val)

        T.left = self.buildTreeRecu(preorder, inorder,
                                    pre_start_idx + 1,  # left side preorder idx starts from the next
                                    in_start_idx, in_idx)  # left side inorder ends at root idx

        T.right = self.buildTreeRecu(preorder, inorder,
                                     pre_start_idx + 1 + in_idx - in_start_idx,  # most tricky part
                                     in_idx + 1, in_end_idx)  # right side inorder always ends at last one

        return T



if __name__ == "__main__":
    testCase = Solution_STD()

    assert not testCase.buildTree([], []), "Edge 0"

    assert testCase.buildTree([1], [1]) == genTree([1]), "Edge 1"

    assert testCase.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == genTree([
        3,
        9, 20,
        None, None, 15, 7
    ]), "Example 1"

    assert testCase.buildTree([3, 1, 2, 4], [1, 2, 3, 4]) == genTree([
        3,
        1, 4,
        None, 2, None, None
    ]), "Additional 1"

    assert testCase.buildTree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]) == genTree([
        1,
        2, 3,
        4, 5, 6, 7
    ]), "Additional 2"

    print("All passed")


