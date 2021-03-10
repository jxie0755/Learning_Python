"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
LC082 Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

from typing import *
from a0_ListNode import *


class Solution_A1:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time O(N)
        Go over and skip the repeating elements
        This is not remove in-place, but create another new linked list
        """
        if not head or not head.next:
            return head

        check = "X"
        dummy = new_head = ListNode(check)

        while head:
            if head.next:
                if head.val == head.next.val:
                    check = head.val
                elif head.val != new_head.next and head.val != check: # ensure not repeating before and after
                    new_head.next = ListNode(head.val)
                    new_head = new_head.next
            elif head.val != check:
                new_head.next = ListNode(head.val)
                new_head = new_head.next

            head = head.next

        return dummy.next


class Solution_A2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Similar to Version A1 but with clearer logic
        """
        new_head = dummy = ListNode("X")

        repeat = False
        while head:
            if head.next:
                if head.val == head.next.val:
                    repeat = True
                else:
                    if not repeat:  # ensure not repeating before and after
                        new_head.next = ListNode(head.val)
                        new_head = new_head.next
                    else:  # if already repeating, then skip but reset the label
                        repeat = False
            else:
                if not repeat:  # check if this last node is different from before
                    new_head.next = ListNode(head.val)
            head = head.next

        return dummy.next

class Solution_B:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time O(N)
        Move in place
        Put a dummy before head and check move three nodes at the same time to find if a repeat happened at the 2nd and 3rd (by a boolean label).
        """
        if not head or not head.next:
            return head

        dummy = pre_head = ListNode("X")
        dummy.next = head
        next_head = head.next
        repeat = False

        while next_head:
            if head.val == next_head.val:
                pre_head.next = None  # 断开pre_head和head
                repeat = True
            else:
                if not repeat:
                    pre_head.next = head # head is unique, include
                    pre_head = pre_head.next  # 只有之前不重复,后面也不重复,才会move first
                else:
                    if next_head.next:
                        repeat = False
                    else: # prevent next_head is the last node
                        pre_head.next = next_head

            head = head.next # move second
            next_head = next_head.next # move third

        return dummy.next


class Solution_C:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Singly recursive version, with clear logic
        Change in place, no extra space needed for storing new nodes
        """
        if not head or not head.next:  # no node or one node
            return head
        elif not head.next.next:  # only two nodes
            if head.val == head.next.val:
                return None
            else:
                return head
        else:  # at least three nodes
            if head.val != head.next.val != head.next.next.val:  # first and second are unique, keep and check from third
                head.next.next = self.deleteDuplicates(head.next.next)
                return head
            elif head.val != head.next.val == head.next.next.val:  # first is unique, keep and check rest
                head.next = self.deleteDuplicates(head.next)
                return head
            elif head.val == head.next.val != head.next.next.val:  # fisrt and second not unique, skip and check from third
                return self.deleteDuplicates(head.next.next)
            elif head.val == head.next.val == head.next.next.val:  # none unique, skip only head and check from second
                # this is most tricky, continuity must be guranteed, can't skip all three
                return self.deleteDuplicates(head.next)


if __name__ == "__main__":
    testCase = Solution_C()

    assert repr(testCase.deleteDuplicates(None)) == "None", "Edge 0"
    assert repr(testCase.deleteDuplicates(genNode([1, 1]))) == "None", "Edge 1"
    assert repr(testCase.deleteDuplicates(genNode([1]))) == "1", "Edge 2"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 3, 3, 4, 4, 5]))) == "1->2->5", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 2, 3]))) == "2->3", "Example 2"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2]))) == "1", "Additional 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2, 3]))) == "1->3", "Additional 2"
    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2, 2]))) == "1", "Additional 3"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 1]))) == "None", "Additional 4"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 2, 2]))) == "None", "Additional 5"

    print("All passed")


