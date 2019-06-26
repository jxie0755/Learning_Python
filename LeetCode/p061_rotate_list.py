# P061 Rotate List
# Medium


# Given a linked list, rotate the list to the right by k places, where k is non-negative.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *



class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        length = 0
        check = head
        while check:
            check = check.next
            length += 1

        if k % length == 0:
            return head
        elif k > length:
            return self.rotateRight(head, k%length)

        cur = head
        new_head = head.next
        new_tail = head

        for i in range(k):
            cur = cur.next
        while cur.next:
            cur = cur.next
            new_head = new_head.next
            new_tail = new_tail.next

        cur.next = head
        new_tail.next = None
        return new_head





if __name__ == '__main__':
    E0 = genNode([])
    assert repr(Solution().rotateRight(E0, 2)) == 'None', 'Edge 0'

    E1 = genNode([1])
    assert repr(Solution().rotateRight(E1, 2)) == '1', 'Edge 1'

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(Solution().rotateRight(S1, 2)) == '4->5->1->2->3', 'Example 1'

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(Solution().rotateRight(S1, 0)) == '1->2->3->4->5', 'Example 1b'

    S2 = genNode([0, 1, 2])
    assert repr(Solution().rotateRight(S2, 4)) == '2->0->1', 'Example 2'

    print('all passed')



