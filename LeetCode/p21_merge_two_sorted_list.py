# p21 Merge two sorted list
# Easy

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode([1,2,4])
l2 = ListNode([1,3,4])

print(l1)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return ListNode(sorted(l1.val + l2.val))


# print(Solution().mergeTwoLists(l1, l2))
# TODO not finished, come back when data structure is learned






