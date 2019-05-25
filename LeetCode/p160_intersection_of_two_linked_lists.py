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


def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None



class Solution(object):

    ### Version A
    ### O(N) time, but O(N) memory
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hmp = {}
        while headA:
            hmp[headA] = 1
            headA = headA.next

        while headB:
            if headB in hmp:
                return headB
            headB = headB.next

        return None


class Solution(object):

    ### Version B, optimized
    ### O(N) time, and O(1) memory
    ### But this will modify the linked list (structure retained, but value changed)
    ### This will fail as Leetcode does not accept value to be String
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while headA:
            headA.val = None
            headA = headA.next

        while headB:
            if headB.val == None:
                return headB
            headB = headB.next

        return None

class Solution(object):

    ### Version C,
    ### O(N) time, and O(1) memory
    ### Break the linkage of headA, point each to a dummy
    ### This will also fail, because it changed structure
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while headA:
            nex = headA.next
            headA.next = dummy
            headA = nex

        while headB:
            if headB.next == dummy:
                return headB
            headB = headB.next

        return None


class Solution(object):

    ### Version D, final version
    ### O(N) time, and O(1) memory
    ### No break, check length of each linked list
        ### same length: move to next togethter
        ### different length: move the longer linkedlist until same length, then move togeterh

    def linkedlength(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def findinter(self, headA, headB):
        """find intersection of headA and headB if they are the same length"""
        if not headA or not headB:
            return None

        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = self.linkedlength(headA)
        B = self.linkedlength(headB)

        if A == B:
            return self.findinter(headA, headB)
        elif A > B:
            for i in range(A-B):
                headA = headA.next
            return self.findinter(headA, headB)
        elif A < B:
            for i in range(B-A):
                headB = headB.next
            return self.findinter(headA, headB)



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

