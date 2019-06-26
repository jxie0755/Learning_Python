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

def genNode(nodes, end=None):
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None




