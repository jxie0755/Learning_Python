"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
p083 Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

from a0_ListNode import *


class Solution_A:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Version A
        Since it is a sorted list, so the repeat should stick together
        Remove in-place
        """
        if head:
            cur = head
            tail = head.next
            while tail:
                if cur.val != tail.val:
                    cur.next = tail
                    cur = cur.next
                else:
                    cur.next = None
                tail = tail.next
        return head


class Solution_B:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Create a new_head and link head to new head if value is different from the tail of new_head"""
        dumb = new_head = ListNode("X")
        while head:
            next_node = head.next  # record next head
            head.next = None  # break head's next, so that new_head only linked
            if head.val != new_head.val:
                new_head.next = head  # new_head -> head (single)
                new_head = new_head.next  # locate the tail of new_head
            head = next_node  # just move to next_node

        return dumb.next

if __name__ == "__main__":
    testCase = Solution_A()

    assert repr(testCase.deleteDuplicates(None)) == "None", "Edge 0"
    assert repr(testCase.deleteDuplicates(genNode([4]))) == "4", "Single Node"

    assert repr(testCase.deleteDuplicates(genNode([1, 1, 2, 3, 3]))) == "1->2->3", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 2]))) == "1->2", "Example 2"

    print("All passed")
