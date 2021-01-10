"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
P82 Remove Duplicates from Sorted List II
Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
"""

from a0_ListNode import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pass


if __name__ == "__main__":
    testCase = Solution()

    assert testCase.deleteDuplicates(None) is None, "Edge 1"
    assert testCase.deleteDuplicates(genNode([1, 1])) is None, "Edge 2"
    assert repr(testCase.deleteDuplicates(genNode([1]))) == "1", "Edge 3"

    assert repr(testCase.deleteDuplicates(genNode([1, 2, 3, 3, 4, 4, 5]))) == "1->2->5", "Example 1"
    assert repr(testCase.deleteDuplicates(genNode([1, 1, 1, 2, 3]))) == "2->3", "Example 2"

    print("all passed")
