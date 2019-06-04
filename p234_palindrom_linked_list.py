# P234 Palindrome Linked List
# Easy

# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A, O(N) time and O(N) space as requireed
    # Move to a list and check the list
    # This will pass quickly but space complexity is not perfect
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result == result[::-1]


    # Version B1, O(N) time and O(1) space as requireed
    # Recursively check head and tail
    # This will fail by exceeding max time limit
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        headval = head.val
        pre_tail = head
        while pre_tail.next.next:
            pre_tail = pre_tail.next
        tailval = pre_tail.next.val

        head = head.next
        pre_tail.next = None
        return headval == tailval and self.isPalindrome(head)

class Solution(object):

    # Version B2, O(N) time and O(1) space as requireed
    # Same idea of B1, but non-recursive
    # Still fail, so it is not about recursive depth
    def palindromeUpdate(self, head):
        """for linked list that is length >= 2"""
        headval = head.val
        pre_tail = head
        while pre_tail.next.next:
            pre_tail = pre_tail.next
        tailval = pre_tail.next.val
        head = head.next
        pre_tail.next = None
        return (headval == tailval, head)

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        while head.next:
            pal, head = self.palindromeUpdate(head)
            if not pal:
                return False
        return True




if __name__ == '__main__':
    assert Solution().isPalindrome(None), 'Edge'
    assert Solution().isPalindrome(genNode(1)), 'Edge 1'
    assert not Solution().isPalindrome(genNode(1,2)), 'Example 1'
    assert Solution().isPalindrome(genNode(1,2,2,1)), 'Example 2'
    assert Solution().isPalindrome(genNode(1,2,1)), 'Example 3'
    assert Solution().isPalindrome(genNode(1,2,3,2,1)), 'Example 4'

    print('all passed')

