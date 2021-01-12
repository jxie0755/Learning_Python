"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
p083 Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.
"""

from a0_ListNode import *


class Solution_A:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert repr(testCase.deleteDuplicates(None)) == "None", "Empty"
    assert repr(testCase.deleteDuplicates(genNode([4]))) == "4", "Single Node"

    assert repr(testCase.deleteDuplicates(genNode([1, 1, 2, 3, 3]))) == "1->2->3", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 2]))) == "1->2", "Example 2"

    print("All passed")
