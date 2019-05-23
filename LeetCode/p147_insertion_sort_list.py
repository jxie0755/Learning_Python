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
    ### Indirect Insertion method using the list other than linked-list
    ### Move the val into a list and insertion sort the list
    ### Then reassign the val of each node according to the list
    ### This will pass but runs slow
    def insertionsort(self, lst):

        for i in range(1, len(lst)):
            j = i-1
            cur = lst[i]
            while j >= 0:
                pre = lst[j]
                if pre > cur:
                    lst[i], lst[j] = lst[j], lst[i]
                    i -= 1
                    j -= 1
                else:
                    break
        return lst


    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next

        self.insertionsort(lst)
        cur = head
        i = 0
        while cur:
            cur.val = lst[i]
            i += 1
            cur = cur.next

        return head



if __name__ == '__main__':
    A = None
    assert Solution().insertionSortList(A) == A, 'Edge 0'

    A = genNode(1)
    assert Solution().insertionSortList(A) == A, 'Edge 1'

    A = genNode(4,2,1,3)
    assert Solution().insertionSortList(A) == genNode(1,2,3,4), 'Example 1'

    A = genNode(-1, 5, 3, 4, 0)
    assert Solution().insertionSortList(A) == genNode(-1, 0, 3, 4, 5), 'Example 2'

    print('all passed')
