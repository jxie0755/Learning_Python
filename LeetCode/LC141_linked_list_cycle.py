"""
https://leetcode.com/problems/linked-list-cycle/
LC141 Linked List Cycle
Easy


Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
"""

from A01_ListNode import *


class Solution_A:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Time O(N^2), Space O(N), Passed, but very slow.
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


class Solution_B:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Time O(N), Space O(N), use hashtable to search faster
        ListNode instance is not hashable, this method search at O(1), and will not break down the original linked list
        """
        if not head:
            return False
        hmp = {}
        cur = head
        while cur:
            if cur not in hmp:
                hmp[cur] = 1
            else:
                return True  # cyling will force to return
            cur = cur.next

        return False  # if no cycle, while loop will end


class Solution_C:
    def hasCycle(self, head):
        """
        Time O(N), Space O(1)
        The Solution C is better as it only create one additional checknode for every previous node to point to
        """
        checkednode = ListNode(99)
        if not head:
            return False
        while head.next:
            if head.next == checkednode:
                return True
            checked = head  # mark previous head
            head = head.next  # move to next head
            checked.next = checkednode  # break down the previous head link to next head, force previous head all to link to the same checknode
            # if any node cycle back to a previous node, then it will be caught as the next of that previous node is a checknode

        return False


class Solution_D:
    def hasCycle(self, head):
        """
        Time O(N), Space O(N)
        The Solution Y forces every node pointed to a different node but has the same value.
        You can not guarantee that the value is not in orignal linked list. And it also uses much more space.
        """
        if not head:
            return False
        while head.next:
            if head.next.val == "X":  # assume "X" will not be in any of the original linked list node value
                return True
            checked = head
            head = head.next
            checked.next = ListNode(
                "X")  # break down the previous head link to next head, force previous head all to link to a ListNode
        return False



if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.hasCycle(None) is False, "Edge 1"

    # Example 1
    L1 = genNode([3,2,0,-4])
    L1.next.next.next.next = L1.next
    # 3 2 0 -4
    # a b c  d
    # d->b cycle
    assert testCase.hasCycle(L1) is True, "Example 1"

    L2 = genNode([1,2])
    L2.next.next = L2
    # 1 2
    # a b
    # b->a cycle
    assert testCase.hasCycle(L2) is True, "Example 2"

    L3 = ListNode(1)
    assert testCase.hasCycle(L3) is False, "Example 3"

    print("All passed")
