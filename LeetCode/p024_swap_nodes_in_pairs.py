# P024 Swap Nodes in Pairs
# Medium


# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pass



if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    # Given 1->2->3->4, you should return the list as 2->1->4->3.
    e = Solution().swapPairs(a)
    assert e.val == 2
    assert e.next.val == 1
    assert e.next.next.val == 4
    assert e.next.next.next.val == 3

