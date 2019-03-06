# P023 Merge k Sorted Lists
# Hard

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         pass


if __name__ == '__main__':
    a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e
    print(a)


