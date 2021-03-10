"""
https://leetcode.com/problems/rotate-list/
LC061 Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

from typing import *
from A01_ListNode import *

class Solution_A:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Loop the linked list twice
        First loop find out the length of the linked list
        Second loop find out the break point (k from the end)

        Cannot use 1 loop by the distanted k nodes (slow and fast)
        because k can be much bigger than the length of linked list
        """
        if not head:
            return None

        # Measure the length of the linked list, and locate the end node
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1

        # link the end to head to be a loop
        last_node.next = head

        # locate the node before break point
        node_before_break = head
        for i in range(length - k % length - 1):
            node_before_break = node_before_break.next

        # locate the next node (as the new head), and break link of the two node
        new_head = node_before_break.next
        node_before_break.next = None
        return new_head


if __name__ == "__main__":
    testCase = Solution_A()

    E0 = genNode([])
    assert repr(testCase.rotateRight(E0, 2)) == "None", "Edge 0"

    E1 = genNode([1])
    assert repr(testCase.rotateRight(E1, 2)) == "1", "Edge 1"

    E2 = genNode([1,2])
    assert repr(testCase.rotateRight(E2, 1)) == "2->1", "Edge 2"

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S1, 2)) == "4->5->1->2->3", "Example 1"

    S2 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S2, 0)) == "1->2->3->4->5", "Example 2"

    S3 = genNode([0, 1, 2])
    assert repr(testCase.rotateRight(S3, 4)) == "2->0->1", "Example 3"

    print("All passed")
