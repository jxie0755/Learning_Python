# P142 Linked List Cycle II
# Medium

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Time O(N), Space O(N), use hashtable to search faster
    # ListNode instance is hashable, this method search at O(1), and will not break down the original linked list
    def detectCycle(self, head):

        if not head:
            return None

        val = 0
        hmp = {}
        cur = head
        while cur:
            if cur not in hmp:
                hmp[cur] = val
                val += 1
            else:
                return cur  # cyling will force to return
            cur = cur.next

        return None  # if no cycle, while loop will end


if __name__ == "__main__":
    # Use is instead of == to avoid max recursion when comparing cycling linked list

    A = genNode([3, 2, 0, 4])
    A.next.next.next.next = A.next
    assert Solution().detectCycle(A) is A.next, "Example 1"

    A = genNode([1, 2])
    A.next.next = A
    assert Solution().detectCycle(A) is A, "Example 2"

    A = genNode([1])
    assert not Solution().detectCycle(A), "Edge 1, no cycle"
    print("all passed")
