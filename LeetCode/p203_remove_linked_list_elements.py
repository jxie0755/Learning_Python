# 203 Remove Linked List Elements
# Easy

# Remove all elements from a linked list of integers that have value val.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # create a dummy head and remove tail one by one through tracking prev nodes and cur nodes
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode('X')
        dummy.next = head

        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next



if __name__ == '__main__':
    assert Solution().removeElements(None, 1) is None, 'Edge 0'

    A = genNode(1,2,3,4,5)
    assert Solution().removeElements(A, 6) == A, 'Edge 1'

    A = genNode(1, 2, 3, 4, 5)
    assert Solution().removeElements(A, 1) == genNode(2,3,4,5), 'Edge 2'

    A = genNode(1, 1, 1, 1, 1)
    assert Solution().removeElements(A, 1) is None, 'Edge 3'

    A = genNode(1,2,3,2,3,2,3,2)
    assert Solution().removeElements(A, 2) == genNode(1,3,3,3), 'Edge 4'

    A = genNode(1,2,6,3,4,5,6)
    assert Solution().removeElements(A, 6) == genNode(1,2,3,4, 5), 'Example 1'

    print('all passed')
