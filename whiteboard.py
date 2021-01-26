"""
https://leetcode.com/problems/reverse-linked-list-ii/
P092 Reverse Linked List II
Medium


Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
"""

from a0_ListNode import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pass


if __name__ == "__main__":
    testCase = Solution()

    s1 = genNode([1])
    assert repr(testCase.reverseBetween(s1, 1, 1)) == "1", "Edge 1"

    s1 = genNode([1, 2])
    assert repr(testCase.reverseBetween(s1, 1, 2)) == "2->1", "Edge 2"

    s1 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.reverseBetween(s1, 2, 4)) == "1->4->3->2->5", "Example 1"

    print("All passed")
