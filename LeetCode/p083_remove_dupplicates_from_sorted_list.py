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


if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.deleteDuplicates(None) is None, "Empty"
    assert testCase.deleteDuplicates(genNode([4])) == genNode([4]), "Single Node"

    assert testCase.deleteDuplicates(genNode([1, 1, 2, 3, 3])) == genNode([1, 2, 3]), "Example 1"
    assert testCase.deleteDuplicates(genNode([1, 1, 2])) == genNode([1, 2]), "Example 2"

    print("all passed")
