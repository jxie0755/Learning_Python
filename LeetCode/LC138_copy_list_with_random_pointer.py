"""
https://leetcode.com/problems/copy-list-with-random-pointer/
LC139 Copy List with Random Pointer
Medium

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Note:
You must return the copy of the given head as a reference to the cloned list.
"""
from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution_A:

    def copyRandomList(self, head: Node) -> Node:
        """
        Use Hashmap to correlate the new_node to respective original node
        """
        check_list = {}

        def helper(head):
            """
            A helper to use memoization method to avoid repeating the cycling chain
            """

            if head:
                if head not in check_list:
                    new_head = Node(head.val, head.next, head.random)
                    check_list[head] = new_head # correlate the new node to original node
                    new_head.next = helper(head.next)
                    new_head.random = helper(head.random)
                    return new_head
                else:
                    return check_list[head] # if cycling, this can help to find the respective cycling in the new node

        return helper(head)


if __name__ == "__main__":
    testCase = Solution_A()

    B = Node(2, None, None)
    B.random = B
    A = Node(1, B, B)

    AA = testCase.copyRandomList(A)
    assert AA.val == 1, "Val"
    assert AA.next.val == 2, "next val"
    assert AA.random.val == 2, "random val"
    assert AA.next.random.val == 2, "cycling"
    assert AA.next.random == AA.next, "True self poiting"

    print("All passed")
