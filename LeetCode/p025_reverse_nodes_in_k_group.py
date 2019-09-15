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

class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Version A, use reverse whole linked list
        Recursive
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
        cur.next, next_cur = None, cur.next

        # reverse前k个节点, 此时k-group的最后一个节点变成了反转后的头
        new_cur = self.reverseNodes(head)

        # 反转后,cur也就是tail了
        head.next = self.reverseKGroup(next_cur, k)
        return new_cur

    def reverseNodes(self, head: ListNode) -> ListNode:
        """
        Helper
        参见Leetcode P206, reverse the whole linked-list
        """

        dummy = ListNode(float("-inf"))
        while head:
            rest = head.next
            tail = dummy.next
            head.next = tail
            dummy.next = head
            head = rest
        return dummy.next

class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Version B, Non-recursive, using counter cycling
        Slower than recursive
        """

        if k == 1 or not head:
            return head

        flag = False  # 设立一个标记, 如果结束时未走完一个循环,要处理一下这个不完整尾部
        count = 1  # 设立一个counter, 以count % k == 0为发现完整k循环

        cur = head  # 备份一个head
        dummy = H = ListNode(0)

        while cur:
            next_node = cur.next  # 备份kgroup之后的下一个开头

            if count % k == 0:  # 若发现一个完整k循环
                flag = False  # 撤销flag
                cur.next = None  # 与后面断开
                H.next = self.reverseNodes(head)  # H接上反转的head (此时head就是反转后的最后一个节点)
                H = head  # 移动H到新链表的最后一个节点
                cur = head = next_node  # 把cur和head定位到next下一个开头

            else:
                flag = True  # 标记未完整k group
                cur = cur.next  # 普通后移
            count += 1

        if flag:  # 如果有不完整尾部, 要接上最后一个头部
            H.next = head

        return dummy.next


if __name__ == "__main__":
    assert Solution().reverseKGroup(genNode([1]), 2) == genNode([1]), "Single"

    a = genNode([1, 2, 3, 4, 5])
    f = Solution().reverseKGroup(a, 2)
    assert repr(f) == "2->1->4->3->5", "Example 1"

    b = genNode([1, 2, 3, 4, 5])
    g = Solution().reverseKGroup(b, 3)
    assert repr(g) == "3->2->1->4->5", "Example 2"

    print("all passed")
