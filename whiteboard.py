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
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None



def rev(head):
    dummy = ListNode('X')
    while head:
        tempheadnext = head.next
        dummynext = dummy.next
        dummy.next = head
        head.next = dummynext
        head = tempheadnext

    return dummy.next


a = genNode(1,2,3,4)
print(repr(rev(a)))
