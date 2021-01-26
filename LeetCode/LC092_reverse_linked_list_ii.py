"""
https://leetcode.com/problems/reverse-linked-list-ii/
P092 Reverse Linked List II
Medium


Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
"""

from a0_ListNode import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        One pass method.
        First locate the head of reverse section
        Gradually insert each node between pre and a None node (to reverse, same as LC206) for n-m+1 steps
        The true tail will be found automatically after the reverse

         1   ->   2    ->    3    ->    4    ->    5
        pre      end                           true_tail
                start
                  m                     n
         1   ->   4    ->    3    ->    2    ->    5
                start                  end       true tail
        """
        dummy = ListNode(0)
        dummy.next = head

        # locate the note before reverse section
        pre = dummy
        for i in range(m - 1):
            pre = pre.next

        # start reverse in place
        end = start = pre.next  # record the end (not moving

        insert_point = None  # a premade tail after the section is reversed
        for j in range(n - m + 1):
            tail = start.next

            # insert the reverse head between pre_reverse and inserting point
            start.next = insert_point
            pre.next = start
            insert_point = start  # move insert point to left to keep insert reversely
            start = tail

        end.next = tail  # link the
        return dummy.next



if __name__ == "__main__":
    testCase = Solution()

    s1 = genNode([1])
    assert repr(testCase.reverseBetween(s1, 1, 1)) == "1", "Edge 1"

    s1 = genNode([1, 2])
    assert repr(testCase.reverseBetween(s1, 1, 2)) == "2->1", "Edge 2"

    s1 = genNode([1, 2, 3, 4, 5])
    assert repr(testCase.reverseBetween(s1, 2, 4)) == "1->4->3->2->5", "Example 1"

    print("All passed")
