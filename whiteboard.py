"""
https://leetcode.com/problems/reorder-list/
LC143 Reorder List
Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

from typing import *
from A01_ListNode import *


class Solution_A:
    def reorderList(self, head: ListNode) -> None:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    A = genNode([1, 2, 3, 4])
    testCase.reorderList(A)
    assert A == genNode([1, 4, 2, 3]), "Example 1"

    A = genNode([1, 2, 3, 4, 5])
    testCase.reorderList(A)
    assert A == genNode([1, 5, 2, 4, 3]), "Example 2"

    print("All passed")


