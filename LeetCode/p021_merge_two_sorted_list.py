# p021 Merge two sorted list
# Easy

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)

def genNode(*nodes, end=None):
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None


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

    l1 = genNode(1,2,4)
    l2 = genNode(1,3,4)

    check = Solution().mergeTwoLists(l1, l2)
    assert repr(check) == '1->1->2->3->4->4'

    print('all passed')
