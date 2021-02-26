"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
P109 Convert Sorted List to Binary Search Tree
Medium


Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution_A:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Convert linked list to an arrayList then solve the problem like Leetcode P108
        """

        if not head:
            return None

        numsList = []
        while head:
            numsList.append(head.val)
            head = head.next

        return self.sortedArrayToBST(numsList)

    def sortedArrayToBST(self, nums: List[int]):
        """
        Helpfer functionfrom LC108
        """
        if not nums:
            return None

        mid_idx = len(nums) // 2
        mid_val = nums[mid_idx]
        T = TreeNode(mid_val)

        T.left = self.sortedArrayToBST(nums[:mid_idx])
        T.right = self.sortedArrayToBST(nums[mid_idx + 1:])

        return T

if __name__ == "__main__":
    testCase = Solution_A()

    A = None
    assert testCase.sortedListToBST(A) is None, "Edge 0"

    A = genNode([1])
    assert testCase.sortedListToBST(A) == genTree([1]), "Edge 1"

    A = genNode([-10, -3, 0, 5, 9])
    assert testCase.sortedListToBST(A) == genTree([
        0,
        -3, 9,
        -10, None, 5, None
    ]), "Example 1"

    print("All passed")
