"""
https://leetcode.com/problems/merge-two-sorted-lists/
p021 Merge two sorted list
Easy

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

from a0_ListNode import *

class Solution_A:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Quick Iteration"""
        head = ListNode(0)
        current = head

        while l1 and l2:

            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return head.next


if __name__ == "__main__":
    testCase = Solution_A()
    l1 = genNode([1, 2, 4])
    l2 = genNode([1, 3, 4])
    check = testCase.mergeTwoLists(l1, l2)
    assert repr(check) == "1->1->2->3->4->4", "Example 1"

    print("all passed")
