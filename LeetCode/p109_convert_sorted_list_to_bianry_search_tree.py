# P109 Convert Sorted List to Binary Search Tree
# Medium


# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    # Convert linked list to an arrayList then solve the problem like Leetcode P108



    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None

        nums = []
        while head:
            nums.append(head.val)
            head = head.next


        mid_idx = len(nums) // 2
        mid = nums[mid_idx]
        ans = TreeNode(mid)

        def helper(root, left_list, right_list):
            if left_list:
                left_mid_idx = len(left_list) // 2
                left_val = left_list[left_mid_idx]
                root.left = TreeNode(left_val)
                LL, LR = left_list[:left_mid_idx], left_list[left_mid_idx+1:]
                helper(root.left, LL, LR)

            if right_list:
                right_mid_idx = len(right_list) // 2
                right_val = right_list[right_mid_idx]
                root.right = TreeNode(right_val)
                RL, RR = right_list[:right_mid_idx], right_list[right_mid_idx + 1:]
                helper(root.right, RL, RR)

        helper(ans, nums[:mid_idx], nums[mid_idx+1:])
        return ans


if __name__ == "__main__":
    if __name__ == "__main__":
        A = None
        assert Solution().sortedListToBST(A) is None, "Edge 0"

        A = genNode([1])
        assert Solution().sortedListToBST(A) == genTree([1]), "Edge 1"

        A = genNode([-10, -3, 0, 5, 9])
        assert Solution().sortedListToBST(A) == genTree([0, -3, 9, -10, None, 5, None]), "Example 1"

        print("all passed")
