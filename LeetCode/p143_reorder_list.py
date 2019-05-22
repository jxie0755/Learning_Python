# P143 Reorder List
# Medium

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

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

    def __eq__(self, other):
        if not self and not other:
            return True
        elif not self or not other:
            return False
        else:
            return self.val == other.val and self.next == other.next


def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None



class Solution(object):

    ### Put nodes in a list
    ### Keep poping the list from head and tail in turn and link them
    ### This will pass but runs slow
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        lst = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next

        dummy = ListNode('X')
        for i in range(len(lst)):
            if i % 2 == 0:
                dummy.next = lst.pop(0)
            else:
                dummy.next = lst.pop()
            dummy = dummy.next

        dummy.next = None  # avoid cycling




if __name__ == '__main__':
    A = genNode(1,2,3,4)
    Solution().reorderList(A)
    assert A == genNode(1,4,2,3), 'Example 1'

    A = genNode(1,2,3,4,5)
    Solution().reorderList(A)
    assert A == genNode(1,5,2,4,3), 'Example 2'

    print('all passed')

