# p021 Merge two sorted list
# Easy

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head

        while l1 is not None or l2 is not None:
            if l1 is None:
                current.next = l2
                l2 = l2.next


            elif l2 is None:
                current.next = l1
                l1 = l1.next


            elif l1.val < l2.val:
                current.next = l1
                l1 = l1.next

            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)

    l12 = ListNode(2)
    l13 = ListNode(4)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(1)

    l22 = ListNode(3)
    l23 = ListNode(4)
    l2.next = l22
    l22.next = l23


    # l1 is now 1->2->4
    # l2 is now 1->3->4
    check = Solution().mergeTwoLists(l1, l2)
    assert check.val == 1
    assert check.next.val == 1
    assert check.next.next.val == 2
    assert check.next.next.next.val == 3
    assert check.next.next.next.next.val == 4
    assert check.next.next.next.next.next.val == 4
    assert check.next.next.next.next.next.next is None
    # Output: 1->1->2->3->4->4->None
    print('all passed')
