"""
https://leetcode.com/problems/rotate-list/
P061 Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

from typing import *
from a0_TreeNode import *
from a0_ListNode import *

class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Version A
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
        else:
            # locate two adjacent node and move together until at the two side of the break point
            find_node_before_break = head
            find_node_after_break = head.next

            for i in range(length - k - 1):
                find_node_before_break = find_node_before_break.next
                find_node_after_break = find_node_after_break.next

            # link the end to head to be a loop
            find_end.next = head

            # break link of the two node, and use the later node as the new head
            find_node_before_break.next = None

            # new head is the node after break point
            return find_node_after_break


if __name__ == "__main__":
    E0 = genNode([])
    assert repr(Solution().rotateRight(E0, 2)) == "None", "Edge 0"

    E1 = genNode([1])
    assert repr(Solution().rotateRight(E1, 2)) == "1", "Edge 1"

    E2 = genNode([1,2])
    assert repr(Solution().rotateRight(E2, 1)) == "2->1", "Edge 2"

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(Solution().rotateRight(S1, 2)) == "4->5->1->2->3", "Example 1"

    S2 = genNode([1, 2, 3, 4, 5])
    assert repr(Solution().rotateRight(S2, 0)) == "1->2->3->4->5", "Example 2"

    S3 = genNode([0, 1, 2])
    assert repr(Solution().rotateRight(S3, 4)) == "2->0->1", "Example 3"

    print("all passed")
