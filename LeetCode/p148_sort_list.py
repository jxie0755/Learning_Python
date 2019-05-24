# P148 Sort List
# Medium


# Sort a linked list in O(n log n) time using constant space complexity.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Use mergesort method
    # Create divide and merge function
    # Divide: break the linked list at mid point and return two parts
    # Merge: merge two sorted linked list

    def mergesort(self, A, B):
        """
        merge two sorted linked list into one linked list
        """
        cur = dummy = ListNode('X')
        while A and B:
            if A.val < B.val:
                cur.next, A = A, A.next
            else:
                cur.next, B = B, B.next
            cur = cur.next
        cur.next = A if A else B
        return dummy.next

    def divide(self, head):
        """
        divide a linked list into half and break the linkage in between
        only divide a linked list that has 2 element and more
        """
        if head.next:
            fast, slow, prev = head, head, None
            while fast is not None and fast.next is not None:
                fast, slow, prev = fast.next.next, slow.next, slow

            prev.next = None
            return head, slow

    def sortList(self, head):
        """
        merge sort the linked list, in place, but reorganize the pointer
        return the new head
        """
        # if lenght is 1 or 0, do not divide, just return
        if not head or not head.next:
            return head
        else:
            # Merge the divided sorted linked list
            first, second = self.divide(head)
            return self.mergesort(self.sortList(first), self.sortList(second))


if __name__ == '__main__':
    A = None
    assert Solution().sortList(A) is None, 'Edge 0'

    A = genNode(1)
    assert Solution().sortList(A) == A, 'Edge 1'

    A = genNode(4,2,1,3)
    assert Solution().sortList(A) == genNode(1,2,3,4), 'Example 1'

    A = genNode(-1, 5, 3, 4, 0)
    assert Solution().sortList(A) == genNode(-1, 0, 3, 4, 5), 'Example 2'

    print('all passed')
