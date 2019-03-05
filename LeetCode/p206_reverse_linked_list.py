# P206 Reverse Linked List
# Easy

# Reverse a singly linked list
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iteration
    # @return {ListNode}
    def reverseList(self, head: ListNode) -> ListNode:# @param {ListNode} head
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
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



    def reverseList(self, head: ListNode) -> ListNode:# @param {ListNode} head
        if not head or not head.next:
            return head

        end = None
        while head:
            temp = head.next    # t移动到h.next
            head.next = end     # h连上e
            end = head          # 然后e移动到h
            head = temp         # h移动到t
        return end

    def reverseList(self, head: ListNode) -> ListNode:# @param {ListNode} head
        end = None
        while head:
            head.next, end, head = end, head, head.next   # 一行写法可以避免temp的使用, 甚至避免if条件, 也不需要假头
        return end

    # 反向推理
    # 1-2-3-4-5-N    N
    # h t            e

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




if __name__ == '__main__':
    emp = None
    f = Solution().reverseList(emp)
    assert not f, 'Edge 1'

    single = ListNode(99)
    f = Solution().reverseList(single)
    assert f.val == 99
    assert not f.next, 'Edge 2'

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f = Solution().reverseList(a)
    assert f.val == 5
    assert f.next.val == 4
    assert f.next.next.val == 3
    assert f.next.next.next.val == 2
    assert f.next.next.next.next.val == 1
    assert not f.next.next.next.next.next
    print('all passed!')
