"""
https://leetcode.com/problems/rotate-list/
P061 Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

from a0_ListNode import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        l = 0
        dumb = last_node = ListNode("X")
        last_node.next = head
        head_copy = head
        while head_copy:
            l += 1
            last_node = last_node.next
            head_copy = head_copy.next

        # here the last node is located, l = length of linked list is obtained
        last_node.next = head # this will make a cycling linked list

        move = l - k%l # avoid repeating when k >> l
        pre_new_head, new_head = dumb, dumb.next
        while move != 0:
            pre_new_head = pre_new_head.next
            new_head = pre_new_head.next
            move -=1

        pre_new_head.next = None # break the link before new_head, no longer cycling
        return new_head




if __name__ == "__main__":
    testCase = Solution()

    E0 = genNode([])
    assert repr(testCase.rotateRight(E0, 2)) == "None", "Edge 0"

    E1 = genNode([1])
    assert repr(testCase.rotateRight(E1, 2)) == "1", "Edge 1"

    E2 = genNode([1, 2])
    assert repr(testCase.rotateRight(E2, 1)) == "2->1", "Edge 2"

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S1, 2)) == "4->5->1->2->3", "Example 1"

    S2 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S2, 0)) == "1->2->3->4->5", "Example 2"

    S3 = genNode([0, 1, 2])
    assert repr(testCase.rotateRight(S3, 4)) == "2->0->1", "Example 3"

    print("all passed")




