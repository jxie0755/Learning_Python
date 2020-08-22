"""
https://leetcode.com/problems/swap-nodes-in-pairs/
P024 Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

from a0_ListNode import *

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode('X')
        dummy.next = head

        while head and head.next:
            first = head
            second = head.next
            third = head.next.next

            pre.next = second
            second.next = first
            first.next = third

            pre = first
            head = third

        return dummy.next
















if __name__ == "__main__":
    testCase = Solution()
    assert testCase.swapPairs(None) is None, "Empty"
    assert testCase.swapPairs(genNode([1])) == genNode([1]), "Single"

    assert repr(testCase.swapPairs(genNode([1, 2]))) == "2->1", "1 pair"
    assert repr(testCase.swapPairs(genNode([1, 2, 3, 4]))) == "2->1->4->3", "Even Pairs"
    assert repr(testCase.swapPairs(genNode([1, 2, 3, 4, 5]))) == "2->1->4->3->5", "with Odd"

    print("all passed")
