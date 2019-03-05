# P025 Reverse Nodes in k-group
# Hard


# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head

        cur = head            # 备份开头, 也就是将会变成结尾的节点

        # 先找到k-group的终点
        for i in range(k-1):
            if head.next:
                head = head.next
            else:  # 若是不满k个,就直接不要动
                return cur

        # 断开,但是不能忘记下一个节点,以备用
        head.next, next_head = None, head.next

        # reverse前k个节点, 此时k-group的最后一个节点变成了反转后的头
        new_head = self.reverseNodes(cur)

        # 反转后,cur也就是tail了
        cur.next = self.reverseKGroup(next_head, k)
        return new_head

    ### 参见Leetcode P206
    def reverseNodes(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next





if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f = Solution().reverseKGroup(a, 2)
    assert f.val == 2
    assert f.next.val == 1
    assert f.next.next.val == 4
    assert f.next.next.next.val == 3
    assert f.next.next.next.next.val == 5

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    g = Solution().reverseKGroup(a, 3)
    assert g.val == 3
    assert g.next.val == 2
    assert g.next.next.val == 1
    assert g.next.next.next.val == 4
    assert g.next.next.next.next.val == 5

    print('all passed')
