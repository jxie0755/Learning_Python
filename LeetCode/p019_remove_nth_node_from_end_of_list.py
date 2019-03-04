# P019 Remove Nth Node From End of List
# Medium


# Given a linked list, remove the n-th node from the end of list and return its head.
# Note:
# Given n will always be valid.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ### 笨办法先判断链表长度, 再正向解决
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        p_length = length-n
        curr = head
        if p_length == 0:
            return head.next
        while p_length > 1:
            curr = curr.next
            p_length -= 1

        curr.next = curr.next.next
        return head





if __name__ == '__main__':
    # Given linked list: 1->2->3->4->5, and n = 2
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # becomes 1->2->3->5
    f = Solution().removeNthFromEnd(a, 2)
    assert f.val == 1
    assert f.next.val == 2
    assert f.next.next.val == 3
    assert f.next.next.next.val == 5
    assert not f.next.next.next.next

    a = ListNode(1)
    f = Solution().removeNthFromEnd(a, 1)
    assert not f

    print('all passed')

