"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
P82 Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

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
        new_head = cur = ListNode(check)

        while head:
            if head.next:
                if head.val == head.next.val:
                    check = head.val
                elif head.val != cur.next and head.val != check: # ensure not repeating before and after
                    cur.next = ListNode(head.val)
                    cur = cur.next
            elif head.val != check:
                cur.next = ListNode(head.val)
                cur = cur.next

            head = head.next

        return new_head.next


class Solution_A2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Similar to Version A1 but with clearer logic
        """
        new_head = dumb = ListNode("X")

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

        return dumb.next

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
            if head.val != tail.val:
                if not repeat:
                    cur.next = head
                    cur = cur.next
                else:
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


class Solution_C:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Singly recursive version, with clear logic
        Change in place, no extra space needed for storing new nodes
        """
        if not head or not head.next:  # no node or one node
            return head
        elif head and head.next and not head.next.next:  # only two nodes
            if head.val != head.next.val:
                return head
            else:
                return None
        else:  # three nodes
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

    assert repr(testCase.deleteDuplicates(None)) == "None", "Edge 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1]))) == "None", "Edge 2"
    assert repr(testCase.deleteDuplicates(genNode([1]))) == "1", "Edge 3"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 3, 3, 4, 4, 5]))) == "1->2->5", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 2, 3]))) == "2->3", "Example 2"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2]))) == "1", "Additional 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2, 3]))) == "1->3", "Additional 2"
    assert repr(testCase.deleteDuplicates(genNode([1, 2, 2, 2]))) == "1", "Additional 3"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 1]))) == "None", "Additional 4"

    print("all passed")


