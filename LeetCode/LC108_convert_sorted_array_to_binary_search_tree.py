"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
LC108 Convert Sorted Array to Binary Search Tree
Easy


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


from typing import *
from a0_TreeNode import *


class Solution_A:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Make a balanced BST
        Find the mid point and recursive create the left and right part
        """
        if not nums:
            return None

        mid_idx = len(nums) // 2
        mid_val = nums[mid_idx]
        T = TreeNode(mid_val)

        T.left = self.sortedArrayToBST(nums[:mid_idx])
        T.right = self.sortedArrayToBST(nums[mid_idx+1:])

        return T


class Solution_STD:
    def sortedArrayToBST(self, nums):
        """
        STD version
        Time:  O(n)
        Space: O(logn)
        """
        return self.sortedArrayToBSTRecu(nums, 0, len(nums))

    def sortedArrayToBSTRecu(self, nums, start_idx, end_idx):
        if start_idx == end_idx:
            return None

        # find mid idx according to start value and the range
        mid_idx = start_idx + (end_idx - start_idx)//2
        node = TreeNode(nums[mid_idx])

        node.left = self.sortedArrayToBSTRecu(nums, start_idx, mid_idx)
        node.right = self.sortedArrayToBSTRecu(nums, mid_idx + 1, end_idx)
        return node


if __name__ == "__main__":
    testCase = Solution_STD()

    A0 = []
    assert testCase.sortedArrayToBST(A0) is None, "Edge 0"

    A1 = [1]
    assert testCase.sortedArrayToBST(A1) == genTree([1]), "Edge 1"

    A2 = [-10, -3, 0, 5, 9]
    assert testCase.sortedArrayToBST(A2) == genTree([0, -3, 9, -10, None, 5, None]), "Example 1"

    print("All passed")
