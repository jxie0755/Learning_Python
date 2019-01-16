# P141 Linked List Cycle
# Easy


# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list,
# we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
# If pos is -1, then there is no cycle in the linked list.




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        ### Time O(N), Space O(N), Passed, but very slow.
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        node_list = []
        while head.next is not None:
            tail = head.next
            if tail in node_list:
                return True
            else:
                node_list.append(tail)
                head = tail
        return False


if __name__ == '__main__':
    assert Solution().hasCycle(None) is False, 'Edge'

    # Example 1
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)

    a.next = b
    b.next = c
    c.next = d
    d.next = b

    assert Solution().hasCycle(a) is True, 'Example 1'


    # Example 2
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    b.next = a

    assert Solution().hasCycle(a) is True, 'Example 2'


    # Example 3
    a = ListNode(1)

    assert Solution().hasCycle(a) is False, 'Example 3'

    print('all passed')
