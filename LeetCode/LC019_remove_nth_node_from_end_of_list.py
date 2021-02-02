"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
P019 Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.
Note:
Given n will always be valid.
"""

from typing import *
from a0_ListNode import *


class Solution_A:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        笨办法,先判断链表长度, 再正向解决
        """
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        dummy = ListNode('X')
        dummy.next = head
        new_cur = dummy

        for i in range(length - n):  # move to node right before removal
            new_cur = new_cur.next
        new_cur.next = new_cur.next.next

        return dummy.next


class Solution_STD:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Two flags slow and fast

        解读:
        D-1-2-3-4-5-N
        s   f          // 先定位s和f

        D-1-2-3-4-5-N
              s   f  // 一起移动s和f直到f.next碰到末尾

        为什么要设置dummy?
        D-1-2-3-4-5-N
        s         f     // # 不设置dummy的话无法应对正好是head需要被remove(倒数第n)的情况
        """

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n):   # 使得slow与fast之间刚好差距一个n
            fast = fast.next

        while fast.next:    # 把fast和slow同速移动到fast碰到末尾, 此时slow的idx正好是倒数第n之前一位
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next # 把slow后一位跳过,直接接上再下一位

        return dummy.next


if __name__ == "__main__":
    testCase = Solution_STD()
    # Given linked list: 1->2->3->4->5
    a = genNode([1])
    f = testCase.removeNthFromEnd(a, 1)
    assert repr(f) == "None", "Edge 1"

    a = genNode([1, 2])
    f = testCase.removeNthFromEnd(a, 2)
    assert repr(f) == "2", "Edge 2"

    a = genNode([1, 2, 3, 4, 5])
    f = testCase.removeNthFromEnd(a, 2)
    assert repr(f) == "1->2->3->5"

    print("All passed")
