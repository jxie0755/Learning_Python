"""Definition of a linked list node."""

from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)

    def __eq__(self, other):
        if not self and not other:
            return True
        elif not self or not other:
            return False
        else:
            return self.val == other.val and self.next == other.next

    # fix the unhashable issue with __eq__ method enabled
    def __hash__(self):
        return hash(id(self))


def genNode(nodes: List[int]) -> ListNode:
    if nodes:
        end = None
        for i in reversed(nodes):
            n = ListNode(i)
            n.next, end = end, n
        return n


if __name__ == '__main__':

    # test genNode
    assert genNode([]) is None, "Check empty"
    assert repr(genNode([1])) == "1", "Single node"
    assert repr(genNode([1,2,3])) == "1->2->3", "Single node"
