"""
https://leetcode.com/problems/validate-binary-search-tree/
LC098 Validate Binary Search Tree
Medium


Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.
"""

from typing import *
from A02_TreeNode import *


class Solution_A:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Use inorderTraversal to get the list from Leetcode LC094
        Then check if the flateen list is sorted
        """
        if not root:
            # Must write this way to avoid val=0
            # Do not write "not root.val"
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        flat = self.inorderTraversal(root)

        # tell if flat list is sorted
        for i in range(1, len(flat)):
            if flat[i] <= flat[i - 1]:
                return False
        return True


class Solution_STD_A:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Recursive verification
        Use a helper to carry low and high boundary
        """
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root: TreeNode, low: int, high: int) -> bool:
        """
        Recursive helper to carry the low and high boundary
        """
        if root is None:
            return True

        return low < root.val < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)



class Solution_STD_B:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Incorporate Morris Travael and check in-place
        """
        check = None # starting check with minimum value
        cur = root
        while cur:
            if cur.left is None: # ignore adding the first element
                if check is not None and cur.val < check: # always compare cur.val with check, replace if >
                    return False
                else:
                    check = cur.val
                    cur = cur.right
            else:
                node = cur.left

                while node.right and node.right is not cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    if check is not None and cur.val < check:  # always compare cur.val with check, replace if >
                        return False
                    else:
                        check = cur.val
                        node.right = None
                        cur = cur.right
        return True


if __name__ == "__main__":
    testCase = Solution_STD_A()

    t1 = genTree([2, 1, 3])
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

