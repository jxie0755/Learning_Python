# P206 Reverse Linked List
# Easy

# Reverse a singly linked list
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import *
from a0_ListNode import *


class Solution:
    # iteration
    # @return {ListNode}
    def reverseList(self, head: ListNode) -> ListNode:  # @param {ListNode} head
        dummy = ListNode(float("-inf"))
        while head:
            # dummy.next, head.next, head = head, dummy.next, head.next
            # https://stackoverflow.com/q/55850332/8435726
            # The swap can cause confusions, avoid using swap like this in complicated data structures
            # Instead, use temp variables to implement the swap

            # catch head.next and dummy.next before break the link:
            rest = head.next
            tail = dummy.next
            # Build new link
            dummy.next = head
            head.next = tail
            # iterate the head to next node
            head = rest

        return dummy.next

    # 这个思路是造一个假头dummy, 然后每个值插入到dummy和dummy.next之间
    # d - N        |    1 - 2 - 3 - 4 - 5 - N
    #    d.nx           h  h.nx

    # d - 1 - N    |        2 - 3 - 4 - 5 - N
    #    d.nx               h  h.nx

    # d - 2 - 1 - N    |        3 - 4 - 5 - N
    #    d.nx                   h  h.nx

    # d - 3 - 2 - 1 - N    |        4 - 5 - N
    #    d.nx                       h  h.nx

    # d - 4 - 3 - 2 - 1 - N    |        5 - N
    #    d.nx                           h  h.nx

    # d - 5 - 4 - 3 - 2 - 1 - N    |        N
    #    d.nx                               h  h为None,终止

    def reverseList(self, head: ListNode) -> ListNode:  # @param {ListNode} head
        if not head or not head.next:
            return head

        end = None
        while head:
            # head.next, end, head = end, head, head.next
            # 一行写法可以避免temp的使用, 甚至避免if条件, 也不需要假头
            # 但不推荐, 原因同上

            nexthead = head.next  # t移动到h.next
            head.next = end  # h连上e
            end = head  # 然后e移动到h
            head = nexthead  # h移动到t
        return end

    # 反向推理
    # 1-2-3-4-5-N    N
    # h t            e

    # 新建一个尾部, 然后不停的把节点指向尾部, 然后把节点作为新的尾部, 这样就相当于不停的在加头部的节点
    # 1-N    2-3-4-5-N   t移动到h.next, h连上e, 然后e移动到h, h移动到t
    # e      h t
    # 重复
    # 2-1-N    3-4-5-N   t移动到h.next, h连上e, 然后e移动到h, h移动到t
    # e        h t
    # 3-2-1-N    4-5-N   t移动到h.next, h连上e, 然后e移动到h, h移动到t
    # e          h t
    # 4-3-2-1-N    5-N   t移动到h.next, h连上e, 然后e移动到h, h移动到t
    # e            h t
    # 5-4-3-2-1-N    N   t移动到h.next, h连上e, 然后e移动到h, h移动到t
    # e              h
    # 此时h=None,while loop终止,返回e


# Time:  O(n)
# Space: O(n)
# Recursive solution.
class Solution2(object):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin

    def reverseListRecu(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]


if __name__ == "__main__":
    emp = None
    f = Solution().reverseList(emp)
    assert repr(f) == "None", "Edge 0"

    single = genNode([99])
    f = Solution().reverseList(single)
    assert repr(f) == "99"

    a = genNode([1, 2, 3, 4, 5])
    f = Solution().reverseList(a)
    assert repr(f) == "5->4->3->2->1"
    print("All passed")
