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
        ### Time O(N^2), Space O(N), Passed, but very slow.
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

class Solution(object):
    def hasCycle(self, head):
        ### Time O(N), Space O(N), use hashtable to search faster
        ### ListNode instance is not hashable, this method search at O(1), and will not break down the original linked list
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        hashtable = {head:1}
        tail = head.next
        while tail is not None:
            if tail not in hashtable:
                hashtable[tail] = 1
            elif hashtable[tail] == 1:
                return True
            else:
                hashtable[tail] += 1
            tail = tail.next

        return False

class Solution_X(object):
    def hasCycle(self, head):
        ### Time O(N), Space O(1)
        """
        :type head: ListNode
        :rtype: bool
        """
        checkednode = ListNode(99)
        if not head:
            return False
        while head.next:
            if head.next == checkednode:
                return True
            checked = head    # mark previous head
            head = head.next  # move to next head
            checked.next = checkednode  # break down the previous head link to next head, force previous head all to link to the same checknode
            # if any node cycle back to a previous node, then it will be caught as the next of that previous node is a checknode

        return False

class Solution_Y(object):
    def hasCycle(self, head):
        ### Time O(N), Space O(N)
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        while head.next:
            if head.next.val == 'X': # assume 'X' will not be in any of the original linked list node value
                return True
            checked = head
            head = head.next
            checked.next = ListNode('X')  # break down the previous head link to next head, force previous head all to link to a ListNode
        return False

# The Solution X is better as it only create one additional checknode for every previous node to point to
# The Solution Y forces every node pointed to a different node but has the same value. You can not guarantee that the value is not in orignal linked list. And it also uses much more space.

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

    # assert Solution().hasCycle(a) is True, 'Example 2'


    # Example 3
    a = ListNode(1)

    # assert Solution().hasCycle(a) is False, 'Example 3'

    print('all passed')
