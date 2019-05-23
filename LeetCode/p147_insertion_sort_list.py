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
    ### Version A
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


class Solution(object):

    ### Version B
    ### Direct method, but reverse, by putting bigger items to the back
    ### THis is actually slower than previous, because it takes too long to find_prev_node
    def find_prev_tail(self, head, tail):
        """find the node before the tail"""
        cur = head
        while cur.next != tail:
                cur = cur.next
        return cur


    def insertion(self, head):
        """
        insertion sort in-place from the head to end
        No need to swap nodes, only swap the values
        """
        if head.next:
            tail = head.next
            while tail:
                if head.val > tail.val:
                    head.val, tail.val = tail.val, head.val
                    head, tail = tail, tail.next
                else:
                    break

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # Locate the tail
        tail = head
        while tail.next:
            tail = tail.next

        while True:
            self.insertion(tail)
            if tail == head:
                break
            tail = self.find_prev_tail(head, tail)

        return head

class Solution(object):

    ### Version C1
    ### Create a dummy head and adding the nodes to dummy.next with insertion idea
    ### Take extra space, it create new nodes with values
    ### The speed is not very fast
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-float('inf'))
        cur = head

        while cur:
            prev = dummy
            while True:
                temp = prev.next
                if temp:
                    if cur.val < temp.val:
                        new = ListNode(cur.val)
                        prev.next = new
                        new.next = temp
                        break
                    else:
                        prev = prev.next
                else:
                    prev.next = ListNode(cur.val)
                    break
            cur = cur.next
        return dummy.next

class Solution(object):

    ### Version C1
    ### Same principle as C2, but actually change in place
    ### Speed is almos the same

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-float('inf'))

        cur = head
        while cur:
            prev = dummy
            temp = dummy.next
            temp_cur_next = cur.next
            cur.next = None
            while True:
                if temp:
                    if cur.val > temp.val:
                        prev = prev.next
                        temp = temp.next
                    else:
                        prev.next = cur
                        cur.next = temp
                        break
                else:
                    prev.next = cur
                    break
            cur = temp_cur_next

        return dummy.next




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
