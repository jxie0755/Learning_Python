# P092 Reverse Linked List II
# Medium


# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.


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


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pass


if __name__ == '__main__':
    s1 = genNode(1)
    assert repr(Solution().reverseBetween(s1, 1, 1)) == '1', 'Edge 1'

    s1 = genNode(1,2)
    assert repr(Solution().reverseBetween(s1, 1, 2)) == '2->1', 'Edge 2'

    s1 = genNode(1,2,3,4,5)
    assert repr(Solution().reverseBetween(s1, 2, 4)) == '1->4->3->2->5', "Example 1"

    print('all passed')
