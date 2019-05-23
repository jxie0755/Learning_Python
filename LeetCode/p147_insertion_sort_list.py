# P147 Insertion Sort List
# Medium

# Sort a linked list using insertion sort.

# Algorithm of Insertion Sort:
    # Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    # At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    # It repeats until no input elements remain.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass



if __name__ == '__main__':
    A = None
    assert Solution().insertionSortList(A) == A, 'Edge -'

    A = genNode(1)
    assert Solution().insertionSortList(A) == A, 'Edge 1'

    A = genNode(4,2,1,3)
    assert Solution().insertionSortList(A) == genNode(1,2,3,4), 'Example 1'

    A = genNode(-1, 5, 3, 4, 0)
    assert Solution().insertionSortList(A) == genNode(-1, 0, 3, 4, 5), 'Example 2'

    print('all passed')
