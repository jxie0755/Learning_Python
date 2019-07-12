# P092 Reverse Linked List II
# Medium


# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        ans = prehead = ListNode("X")
        prehead.next = head
        idx = 1

        #  1   ->   2    ->    3    ->    4    ->    5
        # pre    tail                head
        #         m             n
        #  1   ->   4    ->    3    ->    2    ->    5
        #      dummy.next                tail       head

        while head and idx < m:
            # When this while loop ended, cur will be the first element to be reversed
            head = head.next
            prehead = prehead.next  # locate the pre-head for future connection
            idx += 1

        tail = head               # 此时位于第一个需要被reverse的节点, 也将是reverse之后的最后一个节点

        # 根据leetcode p206把这一段链表反转
        dummy = ListNode("D")
        while head and idx <= n:
            tempheadnext = head.next
            dummynext = dummy.next
            dummy.next = head
            head.next = dummynext
            head = tempheadnext    # 最终head被move到了反转段落之后的节点
            idx += 1

        prehead.next = dummy.next   # 把反转段落之前的节点连上翻转后的head
        tail.next = head            # 把tail接上反转段落之后的head节点

        return ans.next



if __name__ == "__main__":
    s1 = genNode([1])
    assert repr(Solution().reverseBetween(s1, 1, 1)) == "1", "Edge 1"

    s1 = genNode([1,2])
    assert repr(Solution().reverseBetween(s1, 1, 2)) == "2->1", "Edge 2"

    s1 = genNode([1,2,3,4,5])
    assert repr(Solution().reverseBetween(s1, 2, 4)) == "1->4->3->2->5", "Example 1"

    print("all passed")
