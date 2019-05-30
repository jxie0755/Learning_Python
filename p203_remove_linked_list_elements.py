# 203 Remove Linked List Elements
# Easy

# Remove all elements from a linked list of integers that have value val.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pass


if __name__ == '__main__':
    assert Solution().removeElements(None, 1) is None, 'Edge 0'

    A = genNode(1,2,3,4,5)
    assert Solution().removeElements(A, 6) == A, 'Edge 1'

    A = genNode(1, 2, 3, 4, 5)
    assert Solution().removeElements(A, 1) == genNode(2,3,4,5), 'Edge 2'

    A = genNode(1, 1, 1, 1, 1)
    assert Solution().removeElements(A, 1) is None, 'Edge 3'

    A = genNode(1,2,3,2,3,2,3,2)
    assert Solution().removeElements(A, 2) == genNode(1,3,3,3), 'Edge 4'

    A = genNode(1,2,6,3,4,5,6)
    assert Solution().removeElements(A, 6) == genNode(1,2,3,4, 5), 'Example 1'

    print('all passed')
