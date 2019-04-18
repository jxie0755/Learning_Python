# P82 Remove Duplicates from Sorted List II
# Medium


# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)


def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None


class Solution:
    ### O(N)
    ### Go over and skip the repeating elements
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:  # this can be removed but this will go faster
            return head

        check = 'X'
        new_head = ListNode('X')
        cur = new_head

        while head:
            if head.next:
                if head.val == head.next.val:
                    check = head.val
                elif head.val != cur.next and head.val != check:
                    cur.next = ListNode(head.val)
                    cur = cur.next
            elif head.val != check:
                cur.next = ListNode(head.val)
                cur = cur.next

            head = head.next

        return new_head.next


if __name__ == '__main__':
    L = None
    assert not Solution().deleteDuplicates(L), 'Edge 1'

    L = genNode(1,1)
    assert not Solution().deleteDuplicates(L), 'Edge 2'

    L = genNode(1)
    assert repr(Solution().deleteDuplicates(L)) == '1', 'Edge 3'

    L = genNode(1, 2, 3, 3, 4, 4, 5)
    assert repr(Solution().deleteDuplicates(L)) == '1->2->5', 'Example 1'

    L = genNode(1, 1, 1, 2, 3)
    assert repr(Solution().deleteDuplicates(L)) == '2->3', 'Example 1'

    print('all passed')
