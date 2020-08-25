"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
P025 Reverse Nodes in k-group
Hard


Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Note:
    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

from a0_ListNode import *

class Solution_A:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Recursively use reverse whole linked list
        """
        if k == 1 or not head:
            return head

        cur = head  # 备份开头, 也就是将会变成结尾的节点

        # 先找到k-group的终点, 就走一次k节
        for i in range(k - 1):
            if cur.next:
                cur = cur.next
            else:  # 若是不满k个,就直接不要动
                return head

        # 断开,但是不能忘记下一个节点,以备用
        cur.next, next_head = None, cur.next

        # reverse前k个节点, 此时k-group的最后一个节点变成了反转后的头
        new_head = self.reverseNodes(head)

        # 反转后,原来的的head也就是新的tail了,这里接上下一组k group
        head.next = self.reverseKGroup(next_head, k)
        return new_head

    def reverseNodes(self, head: ListNode) -> ListNode:
        """
        Helper for both Solution A and Solution B
        参见Leetcode P206, reverse the whole linked-list
        """

        dummy = ListNode(float("-inf"))
        while head:
            rest = head.next
            head.next = dummy.next
            dummy.next = head
            head = rest
        return dummy.next


class Solution_B:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Non-recursive, using counter cycling
        Slower than recursive
        """

        if k == 1 or not head:
            return head

        full_cycle = False  # 设立一个标记, 如果结束时未走完一个循环,要处理一下这个不完整尾部
        count = 1  # 设立一个counter, 以count % k == 0为发现完整k循环

        cur = head  # 备份一个head
        dummy = new_head = ListNode(0)

        while cur:
            next_head = cur.next  # 时刻备份kgroup之后的下一个开头

            if count % k != 0:
                full_cycle = False  # 标记未完整k group
                cur = cur.next  # 普通后移

            else:  # 若发现一个完整k循环
                full_cycle = True  # 标记完整k group
                cur.next = None  # 与后面断开
                new_head.next = self.reverseNodes(head)  # new_head接上反转的head (此时head就是反转后的最后一个节点)
                new_head = head  # 移动new_head到新链表的最后一个节点(准备连接下一组k group)
                cur = head = next_head  # 把cur和head定位到next下一个开头

            count += 1

        if not full_cycle:  # 如果有不完整尾部, 要接上最后一个头部
            new_head.next = head

        return dummy.next

    def reverseNodes(self, head: ListNode) -> ListNode:
        """
        Helper for both Solution A and Solution B
        参见Leetcode P206, reverse the whole linked-list
        """

        dummy = ListNode(float("-inf"))
        while head:
            rest = head.next
            head.next = dummy.next
            dummy.next = head
            head = rest
        return dummy.next



if __name__ == "__main__":
    testCase = Solution_B()

    assert repr(testCase.reverseKGroup(genNode([1]), 2)) == "1", "Single"

    a = genNode([1, 2, 3, 4, 5])
    f = testCase.reverseKGroup(a, 1)
    assert repr(f) == "1->2->3->4->5", "k=1"

    a = genNode([1, 2])
    f = testCase.reverseKGroup(a, 2)
    assert repr(f) == "2->1", "k = length"

    a = genNode([1, 2, 3, 4, 5])
    f = testCase.reverseKGroup(a, 2)
    assert repr(f) == "2->1->4->3->5", "Example 1"

    b = genNode([1, 2, 3, 4, 5])
    g = testCase.reverseKGroup(b, 3)
    assert repr(g) == "3->2->1->4->5", "Example 2"

    print("all passed")
