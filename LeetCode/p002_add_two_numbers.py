# P002 Add Two Numbers
# Medium


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        new_val = a + b
        if new_val >= 10:
            new_val = new_val % 10
            carry_over = 1
        else:
            carry_over = 0

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
    # Input: (0) + (0 - > 1)
    # Output: 0 -> 1
    # Explanation: 0 + 10 = 10.

    a1 = ListNode(0)

    b1, b2 = ListNode(0), ListNode(1)
    b1.next = b2

    c = Solution().addTwoNumbers(a1, b1)
    assert c.val == 0, 'Edge 1a'
    assert c.next.val == 1, 'Edge 1b'


    # Input: (9) + (9)
    # Output: 8 -> 1
    # Explanation: 9 + 9 = 18.

    a1 = ListNode(9)
    b1 = ListNode(9)

    c = Solution().addTwoNumbers(a1, b1)
    assert c.val == 8, 'Edge 2a'
    assert c.next.val == 1, 'Edge 2b'


    # Example 1
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807.

    a1, a2, a3 = ListNode(2), ListNode(4), ListNode(3)
    a1.next = a2
    a2.next = a3

    b1, b2, b3 = ListNode(5), ListNode(6), ListNode(4)
    b1.next = b2
    b2.next = b3

    c = Solution().addTwoNumbers(a1, b1)
    assert c.val == 7, 'Example 1a'
    assert c.next.val == 0, 'Example 1b'
    assert c.next.next.val == 8, 'Example 1c'


    # Example 2
    # Input: (2 -> 4 -> 3) + (8 -> 9)
    # Output: 0 -> 4 -> 4
    # Explanation: 342 + 98 = 440.

    a1, a2, a3 = ListNode(2), ListNode(4), ListNode(3)
    a1.next = a2
    a2.next = a3

    b1, b2 = ListNode(8), ListNode(9)
    b1.next = b2

    c = Solution().addTwoNumbers(a1, b1)
    assert c.val == 0, 'Example 2a'
    assert c.next.val == 4, 'Example 2b'
    assert c.next.next.val == 4, 'Example 2c'

    print('all passed')
