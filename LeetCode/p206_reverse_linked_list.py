# P206 Reverse Linked List
# Easy

# Reverse a singly linked list
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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

    f = Solution().reverse_nodes(a)
    assert f.val == 5
    assert f.next.val == 4
    assert f.next.next.val == 3
    assert f.next.next.next.val == 2
    assert f.next.next.next.next.val == 1
    assert not f.next.next.next.next.next
    print('all passed!')
