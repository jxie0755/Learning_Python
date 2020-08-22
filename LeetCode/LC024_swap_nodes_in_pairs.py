"""
https://leetcode.com/problems/swap-nodes-in-pairs/
P024 Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

from a0_ListNode import *

class Solution_A:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        用list重排, 再重新连接
        O(N)
        """
        if not head or not head.next:
            return head
        else:

            # 把node放入list
            node_list = []
            cur = head
            while cur:
                node_list.append(cur)
                cur = cur.next

            # swap in list
            for i in range(0, len(node_list), 2):
                if node_list[i].next:
                    node_list[i], node_list[i + 1] = node_list[i + 1], node_list[i]

            # re-link
            i = 0
            while i != len(node_list) - 1:
                node_list[i].next = node_list[i + 1]
                i += 1
            node_list[i].next = None

            return node_list[0]

class Solution_B1:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        不使用list,直接原地改
        Recursive method
        """
        if head and head.next:
            new_head, next_head = head.next, head.next.next
            new_head.next, head.next = head, self.swapPairs(next_head)
            return new_head
        else:
            return head

class Solution_B2:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        不使用list,直接原地改
        Iteration method
        """
        pre = dummy = ListNode('X')
        dummy.next = head

        while head and head.next:
            # 标记4个节点,交换pair之前(pre), 交换pair(first and second), 交换pair之后(tail)
            first = head
            second = head.next
            tail = head.next.next

            pre.next = second
            second.next = first
            first.next = tail

            pre = first
            head = tail

        return dummy.next



if __name__ == "__main__":
    testCase = Solution_B2()
    assert testCase.swapPairs(None) is None, "Empty"
    assert testCase.swapPairs(genNode([1])) == genNode([1]), "Single"

    assert repr(testCase.swapPairs(genNode([1, 2]))) == "2->1", "1 pair"
    assert repr(testCase.swapPairs(genNode([1, 2, 3, 4]))) == "2->1->4->3", "Even Pairs"
    assert repr(testCase.swapPairs(genNode([1, 2, 3, 4, 5]))) == "2->1->4->3->5", "with Odd"

    print("all passed")
