# P023 Merge k Sorted Lists
# Hard

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

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
    def mergeKLists(self, lst) -> ListNode:
        pass


if __name__ == '__main__':
    a = genNode(1,2,3,4,5)
    print(a)


