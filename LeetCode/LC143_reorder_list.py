"""
https://leetcode.com/problems/reorder-list/
LC143 Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

from typing import *
from A01_ListNode import *


class Solution_A:

    def reorderList(self, head: ListNode) -> None:
        """
        Put nodes in a list
        Keep poping the list from head and tail in turn and link them
        This will pass but runs slow
        """
        if not head:
            return None

        lst = []
        while head:
            lst.append(head)
            head = head.next

        dummy = ListNode(0)
        for i in range(len(lst)): # pop head and tail in turn
            if i % 2 == 0:
                dummy.next = lst.pop(0)
            else:
                dummy.next = lst.pop(-1)
            dummy = dummy.next

        dummy.next = None  # disconnect the last node to avoid cycling


class Solution_STD:

    def reorderList(self, head: ListNode) -> None:
        """
        Change in place
        Find half-way point and break.
        Then reverse second half
        Merge two halves node by node
        """

        # find out half way linked list
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next  # locate
        slow.next = None  # disconnect

        # reverse second half (classic method)
        dummy = ListNode(0)
        end = None
        while second_half:
            temp = second_half.next
            dummy.next = second_half
            second_half.next = end
            second_half = temp
            end = dummy.next

        # merge first half (head) and reversed second half
        reversed_second_half = dummy.next
        ans = head
        while head and reversed_second_half:
            head_next = head.next
            second_next = reversed_second_half.next

            head.next = reversed_second_half
            reversed_second_half.next = head_next

            head = head_next
            reversed_second_half = second_next

        # Breakdown:
        # 1-2-3-4-5
        # to
        # 1-2 and 3-4-5, then reverse 3-4-5 to 5-4-3:
        # got:
        # L1:  1-2
        # L2:  5-4-3
        # then link the head and move to next
        # 1-5-2-4-3 (4 naturally linked to 3)


if __name__ == "__main__":
    testCase = Solution_A()

    L1 = genNode([1])
    testCase.reorderList(L1)
    assert L1 == genNode([1]), "Edge 1"

    L2 = genNode([1, 2, 3, 4])
    testCase.reorderList(L2)
    assert L2 == genNode([1, 4, 2, 3]), "Example 1"

    L3 = genNode([1, 2, 3, 4, 5])
    testCase.reorderList(L3)
    assert L3 == genNode([1, 5, 2, 4, 3]), "Example 2"

    print("All passed")
