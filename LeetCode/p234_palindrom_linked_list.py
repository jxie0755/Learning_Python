# P234 Palindrome Linked List
# Easy

# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A, O(N^2) time and O(N) space as requireed
    # Move to a list and check the list
    # This will pass quickly but space complexity is not perfect
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        result = []
        while head:
            result.append(head.val)
            head = head.next

        return result == result[::-1]

class Solution(object):

    # Version B1, O(N^2) time and O(1) space as requireed
    # Recursively check head and tail
    # This will fail by exceeding max time limit
    def isPalindrome(self, head: ListNode) -> bool:
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

    # Version B2, O(N^2) time and O(1) space as requireed
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

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        while head.next:
            pal, head = self.palindromeUpdate(head)
            if not pal:
                return False
        return True


class Solution(object):

    # Version C, O(N) time and O(1) space as requireed
    # Walk halfway and reverse the second half
    def reverselink(self, head):
        dummy = ListNode("X")
        tail = dummy.next
        while head:
            nex = head.next
            head.next = tail
            dummy.next = head
            tail = head
            head = nex
        return dummy.next

    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev_half = self.reverselink(slow)

        while rev_half:
            if rev_half.val != head.val:
                return False
            rev_half = rev_half.next
            head = head.next
        return True

class Solution(object):
    # STD ans
    # @param {ListNode} head
    # @return {boolean}
    # Same idea of Version C, but reverse first half, and do it at the same time to get second half

    # Disadvantage: need to handle the odd length
    def isPalindrome(self, head: ListNode) -> bool:
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palindrome



if __name__ == "__main__":
    assert Solution().isPalindrome(None), "Edge"
    assert Solution().isPalindrome(genNode([1])), "Edge 1"
    assert not Solution().isPalindrome(genNode([1,2])), "Example 1"
    assert Solution().isPalindrome(genNode([1,2,2,1])), "Example 2"
    assert Solution().isPalindrome(genNode([1,2,1])), "Example 3"
    assert Solution().isPalindrome(genNode([1,2,3,2,1])), "Example 4"

    print("all passed")

