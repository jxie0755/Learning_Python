# This is to find out why a data structure's hasbility can be impacted by some internal methods
# https://stackoverflow.com/q/56298727/8435726


from hashlib import md5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)

    # def __eq__(self, other):
    #     if not self and not other:
    #         return True
    #     elif not self or not other:
    #         return False
    #     else:
    #         return self.val == other.val and self.next == other.next

    # def __eq__(self, other):
    #     return str(self) == str(other)


def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None


# Notice that I blocked the __eq__ method. Now if I create an instance:
# Then it is hashable, however, I do get different output number everytime I run it.

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
A.next = B
B.next = C
print(hash(A))

# Now if I unblock the __eq__ method, all of sudden it is not hashable anymore. Why?
# It seems that the hash method will use __eq__. And how does it know it is not hashable after __eq__ is enabled?

# Additional: If I write the __eq__ method to just compare the str version of the two linked list (the second __eq__ method), I thought this could solve the problem, because by converting the linked list into a string, it becomes an hashable data, but I still get the unhashable error message

