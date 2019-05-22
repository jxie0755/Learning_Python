# P142 Linked List Cycle II
# Medium

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.


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


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass


if __name__ == '__main__':


    A = genNode(3,2,0,4)
    A.next.next.next.next = A.next
    assert Solution().detectCycle(A) == 1, 'Example 1'

    A = genNode(1,2)
    A.next.next= A
    assert Solution().detectCycle(A) == 0, 'Example 2'

    A = genNode(1)
    assert not Solution().detectCycle(A), 'Edge 1, no cycle'
    print('all passe')
