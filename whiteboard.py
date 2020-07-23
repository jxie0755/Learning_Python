"""
https://leetcode.com/problems/add-two-numbers/
P002 Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from a0_ListNode import *

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time:  O(n), Space: O(1)
        Non-recursion  method
        This will protect l1 and l2 from changing
        """
        ans = cur = ListNode(0)
        addup = 0
        while l1 or l2:
            va = l1.val if l1 else 0
            vb = l2.val if l2 else 0

            new_addup, val = divmod(va + vb + addup, 10)
            addup = new_addup

            cur.next = ListNode(val)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if addup:
            cur.next = ListNode(addup)

        return ans.next




if __name__ == "__main__":
    testCase = Solution()

    a1 = genNode([0])
    b1 = genNode([0, 1])

    c = testCase.addTwoNumbers(a1, b1)
    assert repr(c) == "0->1"

    a1 = genNode([9])
    b1 = genNode([9])

    c = testCase.addTwoNumbers(a1, b1)
    assert repr(c) == "8->1"

    # Example 1
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.

    a1 = genNode([2, 4, 3])
    b1 = genNode([5, 6, 4])
    c = testCase.addTwoNumbers(a1, b1)
    assert repr(c) == "7->0->8"

    # Example 2
    # Input: (2 -> 4 -> 3) + (8 -> 9)
    # Output: 0 -> 4 -> 4
    # Explanation: 342 + 98 = 440.

    a1 = genNode([2, 4, 3])
    b1 = genNode([8, 9])

    c = testCase.addTwoNumbers(a1, b1)
    assert repr(c) == "0->4->4"
    print("all passed")
