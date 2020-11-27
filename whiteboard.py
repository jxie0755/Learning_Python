"""
https://leetcode.com/problems/rotate-list/
P061 Rotate List
Medium

Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""

from a0_ListNode import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        pass



if __name__ == "__main__":
    testCase = Solution()

    E0 = genNode([])
    assert repr(testCase.rotateRight(E0, 2)) == "None", "Edge 0"

    E1 = genNode([1])
    assert repr(testCase.rotateRight(E1, 2)) == "1", "Edge 1"

    E2 = genNode([1, 2])
    assert repr(testCase.rotateRight(E2, 1)) == "2->1", "Edge 2"

    S1 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S1, 2)) == "4->5->1->2->3", "Example 1"

    S2 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.rotateRight(S2, 0)) == "1->2->3->4->5", "Example 2"

    S3 = genNode([0, 1, 2])
    assert repr(testCase.rotateRight(S3, 4)) == "2->0->1", "Example 3"

    print("all passed")




