# P234 Palindrome Linked List
# Easy

# Given a singly linked list, determine if it is a palindrome.
# Follow up:
# Could you do it in O(n) time and O(1) space?

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pass




if __name__ == '__main__':
    assert Solution().isPalindrome(None), 'Edge'
    assert Solution().isPalindrome(genNode(1)), 'Edge 1'
    assert not Solution().isPalindrome(genNode(1,2)), 'Example 1'
    assert Solution().isPalindrome(genNode(1,2,2,1)), 'Example 2'
    assert Solution().isPalindrome(genNode(1,2,1)), 'Example 3'
    assert Solution().isPalindrome(genNode(1,2,3,2,1)), 'Example 4'

    print('all passed')

