# P143 Reorder List
# Medium

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


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

class Solution(object):

    # STD ans
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head


        # Find the middle point by moving fast by 2 step and slow by 1 step.
        # when fast gets to the end, slow is at half point as the begining of second half
        # now second half begin with slow
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None

        # Revser the second half (now begin with prev)
        while current != None:
            current.next, prev, current = prev, current, current.next

        # Until now: head is the first half, prev is the reversed second half
        l1, l2 = head, prev
        dummy = ListNode(0)
        current = dummy

        # linked L1 head to L2 head
        # Move L1 head to next one and L2 head to next one
        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next
        return dummy.next

        # Breakdown:
        # 1-2-3-4-5
        # to
        # 1-2 and 3-4-5, then reverse 3-4-5 to 5-4-3:
        # got:
        # L1:  1-2
        # L2:  5-4-3
        # then link the head and move to next
        # 1-5-2-4-3 (4 naturally linked to 3)



if __name__ == '__main__':
    A = genNode(1,2,3,4)
    Solution().reorderList(A)
    assert A == genNode(1,4,2,3), 'Example 1'

    A = genNode(1,2,3,4,5)
    Solution().reorderList(A)
    assert A == genNode(1,5,2,4,3), 'Example 2'

    print('all passed')

