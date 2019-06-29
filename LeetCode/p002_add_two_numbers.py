# P002 Add Two Numbers
# Medium


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *

class Solution(object):

    # Version A, Time:  O(n), Space: O(1)
    # Non-recursion  method
    # This will protect l1 and l2 from changing
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


class Solution:

    # Version B, Time:  O(n), Space: O(1)
    # Recursion method
    # This will break down l1 and l2
    # 加一个parameter就可以避免改变l1和l2
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        new_val = a + b
        carry_over, new_val = divmod(new_val, 10)

        new_node = ListNode(new_val)
        if l1.next and not l2.next:
            l1.next.val += carry_over
            new_node.next = self.addTwoNumbers(l1.next, ListNode(0))
        elif l2.next and not l1.next:
            l2.next.val += carry_over
            new_node.next = self.addTwoNumbers(ListNode(0), l2.next)
        elif l1.next and l2.next:
            l1.next.val += carry_over
            new_node.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            new_node.next = None if not carry_over else ListNode(1)

        return new_node


if __name__ == '__main__':

    a1 = genNode([0])
    b1 = genNode([0, 1])

    c = Solution().addTwoNumbers(a1, b1)
    assert repr(c) == '0->1'

    a1 = genNode([9])
    b1 = genNode([9])

    c = Solution().addTwoNumbers(a1, b1)
    assert repr(c) == '8->1'


    # Example 1
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.

    a1 = genNode([2,4,3])
    b1 = genNode([5,6,4])
    c = Solution().addTwoNumbers(a1, b1)
    assert repr(c) == '7->0->8'


    # Example 2
    # Input: (2 -> 4 -> 3) + (8 -> 9)
    # Output: 0 -> 4 -> 4
    # Explanation: 342 + 98 = 440.

    a1 = genNode([2,4,3])
    b1 = genNode([8,9])

    c = Solution().addTwoNumbers(a1, b1)
    assert repr(c) == '0->4->4'
    print('all passed')
