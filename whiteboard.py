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


class Solution:

    # Use Hashmap to save the
    def copyRandomList(self, head: Node) -> Node:
        pass



if __name__ == "__main__":
    B = Node(2, None, None)
    B.random = B
    A = Node(1, B, B)

    AA = Solution().copyRandomList(A)
    assert AA.val == 1, "Val"
    assert AA.next.val == 2, "next val"
    assert AA.random.val == 2, "random val"
    assert AA.next.random.val == 2, "cycling"
    assert AA.next.random == AA.next, "True self poiting"

    print("All passed")
