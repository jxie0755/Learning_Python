# P160 Instersection of Two Linked Lists
# Easy

# Write a program to find the node at which the intersection of two singly linked lists begins.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pass





if __name__ == '__main__':
    A = genNode(4,1)
    B = genNode(5,0,1)
    C = genNode(8,4,5)
    A.next.next = C
    B.next.next.next = C

    assert Solution().getIntersectionNode(A, B) == C, 'Example 1'

    A = genNode(0,9,1)
    B = genNode(3)
    C = genNode(2,4)
    A.next.next.next = C
    B.next = C
    assert Solution().getIntersectionNode(A, B) == C, 'Example 2'

    A = genNode(2,6,4)
    B = genNode(1,5)
    assert not Solution().getIntersectionNode(A, B) == C, 'Example 3, Edge'

    print('all passed')

