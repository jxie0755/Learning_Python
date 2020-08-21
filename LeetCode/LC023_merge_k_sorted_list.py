"""
https://leetcode.com/problems/merge-k-sorted-lists/
P023 Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

from a0_ListNode import *
from typing import *

class Solution_A:

    def mergeKLists(self, lists) -> ListNode:
        """
        Use iteration to merge all sorted
        Max Time limit reached
        """

        result = dummy = ListNode('X')
        while True:
            empty = 0  # 设立一个检查lst全部为空的的值
            min_idx, min_val = 0, float('inf')
            for i in range(len(lists)):  # 这里用一个循环来找出lst内部哪个链表是最小值
                if lists[i]:
                    val = lists[i].val
                    if val < min_val:
                        min_idx = i
                        min_val = val
                else:
                    empty += 1  # 同时筛选出空链表,如果链表为空就+1

            if empty == len(lists):  # 先核实这一轮是不是全空
                break  # 如果全空就没必要操作了
            else:
                dummy.next = ListNode(min_val)
                dummy = dummy.next
                lists[min_idx] = lists[min_idx].next

        return result.next



class Solution_B:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        take all val out into an ArrayList, then sort and re-link to LinkedList
        kind of cheating, not recommended
        """
        result = []
        for node in lists:
            while node:
                result.append(node.val)
                node = node.next
        return genNode(sorted(result))



class SolutionC1:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        use merge two list, then use it multiple times
        但是这个合并的方法偏慢, 相当于要流经的重复节点太多次了
        """
        dummy = ListNode(float("-inf"))
        for i in lists:
            dummy = self.merge_two(dummy, i)

        return dummy.next

    def merge_two(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Helper for Solution C1 and C2 (now set out side of the Solution)
        merge two sorted linked list
        """
        curr = dummy = ListNode("X")
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


class Solution_C2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Improved from C1
        这个方法采用首尾合并, 这样能显著减少重复流经的节点
        首尾相遇后, 重置首为0, 尾不变(因为已经都被合并到前面去了)
        """

        if not lists:
            return None

        left, right = 0, len(lists) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = self.merge_two(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

    def merge_two(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Helper for Solution C1 and C2 (now set out side of the Solution)
        merge two sorted linked list
        """
        curr = dummy = ListNode("X")
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    testCase = Solution_C2()
    assert testCase.mergeKLists([]) is None, "Empty"

    single = genNode([1])
    e = testCase.mergeKLists([single])
    assert repr(e) == "1", "single"

    a = genNode([1, 4, 5])
    b = genNode([1, 3, 4])
    c = genNode([2, 6])
    lists = [a, b, c]
    check = testCase.mergeKLists(lists)
    assert repr(check) == "1->1->2->3->4->4->5->6", "Example"

    print("all passed")
