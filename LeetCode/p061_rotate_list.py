"""
https://leetcode.com/problems/rotate-list/
P061 Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

from a0_ListNode import *

class Solution_A:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Loop the linked list and break from the rotate point
        """
        if not head:
            return None

        # Measure the length of the linked list, and locate the end node
        length = 1
        find_end = head
        while find_end.next:
            find_end = find_end.next
            length += 1

        # Special cases
        if k % length == 0:
            return head
        elif k > length:  # optimize by remove full cycles
            return self.rotateRight(head, k % length)

        # Common cases
        # locate the node before break point
        find_node_before_break = head

        for i in range(length - k - 1):
            find_node_before_break = find_node_before_break.next

        # link the end to head to be a loop
        find_end.next = head

        # locate the next node (as the new head), and break link of the two node
        new_head = find_node_before_break.next
        find_node_before_break.next = None
        return new_head


if __name__ == "__main__":
    testMethod = Solution_A().rotateRight

    E0 = genNode([])
    assert repr(testMethod(E0, 2)) == "None", "Edge 0"

    E1 = genNode([1])
    assert repr(testMethod(E1, 2)) == "1", "Edge 1"

    E2 = genNode([1,2])
    assert repr(testMethod(E2, 1)) == "2->1", "Edge 2"

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(testMethod(S1, 2)) == "4->5->1->2->3", "Example 1"

    S2 = genNode([1, 2, 3, 4, 5])
    assert repr(testMethod(S2, 0)) == "1->2->3->4->5", "Example 2"

    S3 = genNode([0, 1, 2])
    assert repr(testMethod(S3, 4)) == "2->0->1", "Example 3"

    print("all passed")
