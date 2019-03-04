# P025 Reverse Nodes in k-group
# Hard


# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # Given 1->2->3->4, you should return the list as 2->1->4->3.
    f = Solution().reverseKGroup(a, 2)
    assert f.val == 2
    assert f.next.val == 1
    assert f.next.next.val == 4
    assert f.next.next.next.val == 3
    assert f.next.next.next.next.val == 5

    g = Solution().reverseKGroup(a, 3)
    assert f.val == 3
    assert f.next.val == 2
    assert f.next.next.val == 1
    assert f.next.next.next.val == 4
    assert f.next.next.next.next.val == 5

    print('all passed')
