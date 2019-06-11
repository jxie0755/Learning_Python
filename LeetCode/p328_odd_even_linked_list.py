# P328 Odd Even Linked List
# Medium


# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place.
# The program should run in O(1) space complexity and O(nodes) time complexity.


# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:

    # Veriosn A
    # Move Nodes out and combine back, O(1) but not in-Place
    def oddEvenList(self, head: ListNode) -> ListNode:
        O = odd = ListNode('O')
        E = even = ListNode('E')

        idx = 1
        while head:
            next_head = head.next
            head.next = None
            if idx % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = next_head
            idx += 1

        # Merge Odd and Even
        odd.next = E.next
        return O.next



if __name__ == '__main__':
    assert not Solution().oddEvenList(None), 'Edge 0'

    assert Solution().oddEvenList(genNode(1,2,3,4,5)) == genNode(1,3,5,2,4), 'Example 1'
    assert Solution().oddEvenList(genNode(1,2,3,4,5,6)) == genNode(1,3,5,2,4,6), 'Example 1b'
    assert Solution().oddEvenList(genNode(2,1,3,5,6,4,7)) == genNode(2,3,6,7,1,5,4), 'Example 2'

    print('all passed')
