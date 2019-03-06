# p083 Remove Duplicates from Sorted List
# Easy


# Given a sorted linked list, delete all duplicates such that each element appear only once.


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

    a = genNode(1,1,2,3,3)
    check = Solution().deleteDuplicates(a)
    assert repr(check) == '1->2->3'

    b = genNode(1,1,2)
    check = Solution().deleteDuplicates(b)
    assert repr(check) == '1->2'

    a = None
    check = Solution().deleteDuplicates(a)
    assert check is None

    a = genNode(4)
    check = Solution().deleteDuplicates(a)
    assert repr(check) == '4'

    print('all passed')

