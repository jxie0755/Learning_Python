"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
P108 Convert Sorted Array to Binary Search Tree
Easy


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

from typing import *
from a0_TreeNode import *


class Solution_A:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = []
    assert testCase.sortedArrayToBST(T0) is None, "Edge 0"

    T1 = [1]
    assert testCase.sortedArrayToBST(T1) == genTree([1]), "Edge 1"

    T2 = [-10, -3, 0, 5, 9]
    assert testCase.sortedArrayToBST(T2) == genTree([0, -3, 9, -10, None, 5, None]), "Example 1"

    print("All passed")

