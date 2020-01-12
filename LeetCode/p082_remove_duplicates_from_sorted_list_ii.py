"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
P82 Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

from a0_ListNode import *


class Solution_A:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time O(N)
        Go over and skip the repeating elements
        This is not remove in-place, but create another new linked list
        """
        if not head or not head.next:
            return head

        check = "X"
        new_head = cur = ListNode(check)

        while head:
            if head.next:
                if head.val == head.next.val:
                    check = head.val
                elif head.val != cur.next and head.val != check:
                    cur.next = ListNode(head.val)
                    cur = cur.next
            elif head.val != check:
                cur.next = ListNode(head.val)
                cur = cur.next

            head = head.next

        return new_head.next


class Solution_B:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time O(N)
        Move in place
        Put a dummy before head and check move three nodes at the same time to find if a repeat happened at the 2nd and 3rd (by a boolean label).
        """
        if not head or not head.next:
            return head

        dummy = cur = ListNode("X")
        dummy.next = head
        tail = head.next
        repeat = False

        while tail:
            if head.val != tail.val and not repeat:
                cur.next = head
                cur = cur.next

            elif head.val != tail.val and repeat:
                if tail.next:
                    repeat = False
                else:
                    cur.next = tail
            else:
                cur.next = None
                repeat = True

            head = head.next
            tail = tail.next

        return dummy.next


if __name__ == "__main__":
    testCase = Solution_B()

    assert testCase.deleteDuplicates(None) is None, "Edge 1"
    assert testCase.deleteDuplicates(genNode([1, 1])) is None, "Edge 2"
    assert repr(testCase.deleteDuplicates(genNode([1]))) == "1", "Edge 3"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 3, 3, 4, 4, 5]))) == "1->2->5", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 2, 3]))) == "2->3", "Example 2"

    print("all passed")

