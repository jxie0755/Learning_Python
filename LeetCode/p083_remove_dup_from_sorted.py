# p083 Remove Duplicates from Sorted List
# Easy


# Given a sorted linked list, delete all duplicates such that each element appear only once.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        result = ListNode(head.val)
        current = result
        tail = head.next
        while tail is not None:
            if current.val != tail.val:
                current.next = tail
                current = current.next
            elif current.val == tail.val and tail.next is None:
                current.next = None
            tail = tail.next
        return result


    def deleteDuplicates(self, head):
        cur = head
        prev = None
        duplicates = dict()
        while cur:
            if cur.val in duplicates:
                prev.next = cur.next
                cur = None
            else:
                duplicates[cur.val] = 1
                prev = cur
            cur = prev.next
        return head


if __name__ == '__main__':

    l1 = ListNode(1)

    l12 = ListNode(1)
    l13 = ListNode(2)
    l14 = ListNode(3)
    l15 = ListNode(3)
    l1.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15


    # l1 is now 1->1->2->3->3
    check = Solution().deleteDuplicates(l1)
    assert check.val == 1
    assert check.next.val == 2
    assert check.next.next.val == 3
    assert check.next.next.next is None
    # Output: 1->2->3->None

    l2 = ListNode(1)
    l22 = ListNode(1)
    l23 = ListNode(2)
    l2.next = l22
    l22.next = l23

    check = Solution().deleteDuplicates(l2)
    assert check.val == 1
    assert check.next.val == 2
    assert check.next.next is None

    l3 = None
    check = Solution().deleteDuplicates(l3)
    assert check is None

    l4 = ListNode(4)
    check = Solution().deleteDuplicates(l4)
    assert check.val == 4
    assert check.next is None

    print('all passed')

