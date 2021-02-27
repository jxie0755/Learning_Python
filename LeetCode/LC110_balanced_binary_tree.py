"""
https://leetcode.com/problems/balanced-binary-tree/
P110 Balanced Binary Tree
Easy


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

from a0_TreeNode import *


class Solution_A1:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Check if two side maxDepth differece <= 1 and recursively verify their two sides
        """
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution_A2:
    MAX_DEPTH_HMP = {}

    def isBalanced(self, root: TreeNode) -> bool:
        """
        Same idea of A1 but use memoization to track maxDepth of each TreeNode
        """
        if not root:
            return True

        ans = abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)

        self.MAX_DEPTH_HMP.clear()

        return ans

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root in self.MAX_DEPTH_HMP:
            return self.MAX_DEPTH_HMP[root]
        else:
            max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            self.MAX_DEPTH_HMP[root] = max_depth
            return max_depth


class Solution_STD:    # @param root, a tree node
    def isBalanced(self, root: TreeNode) -> bool:

        def getHeight(root: TreeNode) -> int:
            """
            Helper function
            """
            if root is None:
                return 0

            left_height= getHeight(root.left)
            right_height = getHeight(root.right)

            if left_height < 0 or right_height < 0 or \
                    abs(left_height - right_height) > 1: # save time by skip if one unbalanced tree is found
                return -1 # not balanced

            return max(left_height, right_height) + 1

        return getHeight(root) != -1



if __name__ == "__main__":
    testCase = Solution_STD()

    T0 = None
    assert testCase.isBalanced(T0), "Edge 0"

    T1 = genTree([1])
    assert testCase.isBalanced(T1), "Edge 1"

    T2 = genTree([
        3,
        9, 20,
        None, None, 15, 7])
    assert testCase.isBalanced(T2), "Example 1"

    T3 = genTree([
        1,
        2, 2,
        3, 3, None, None,
        4, 4, None, None, None, None, None, None
    ])
    assert not testCase.isBalanced(T3), "Example 2"

    T4 = genTree([
        1,
        2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, None, None,
        5, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    ])
    assert testCase.isBalanced(T4), "Additional 1"

    T5 = genTree([
        1,
        None, 2,
        None, None, None, 3
    ])
    assert not testCase.isBalanced(T5), "Additional 2"

    T6 = genTree([
        1,
        2, 2,
        3, 3, None, 3,
        4, 4, None, None, None, None, None, 4,
        5, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, 5,
    ])
    assert not testCase.isBalanced(T6), "Additional 3"
    print("All passed")
