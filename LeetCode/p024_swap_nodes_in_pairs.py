# P024 Swap Nodes in Pairs
# Medium


# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:

    ### 用list重排, 再重新连接
    ### O(N)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            new_head = head.next

            # 把node放入list
            node_list = []
            cur = head
            while cur:
                node_list.append(cur)
                cur = cur.next

            # swap in list
            for i in range(0, len(node_list), 2):
                if node_list[i].next:
                    node_list[i], node_list[i+1] = node_list[i+1], node_list[i]

            # re-link
            i = 0
            while i != len(node_list)-1:
                node_list[i].next = node_list[i+1]
                i += 1
            node_list[i].next = None

            return new_head

    ### 不使用list,直接原地改
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            new_head, next_head = head.next, head.next.next
            new_head.next, head.next = head, self.swapPairs(next_head)
            return new_head
        else:
            return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d

    # Given 1->2->3->4, you should return the list as 2->1->4->3.
    e = Solution().swapPairs(a)
    assert e.val == 2
    assert e.next.val == 1
    assert e.next.next.val == 4
    assert e.next.next.next.val == 3
    print('all passed')
