"""
https://leetcode.com/problems/merge-k-sorted-lists/
P023 Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

from a0_ListNode import *

class Solution:

    def mergeKLists(self, lst) -> ListNode:
        """
        Version A
        Merge all through iteration
        Exceeded time limit
        """

        cur = dummy = ListNode("X")

        while any([i for i in lst]):
            i, min_val, min_idx = 0, float("inf"), float("inf")

            while i < len(lst):
                node = lst[i]
                if node:
                    if node.val < min_val:
                        min_val, min_idx = node.val, i
                i += 1

            cur.next = ListNode(min_val)
            lst[min_idx] = lst[min_idx].next
            cur = cur.next

        return dummy.next


class Solution:

    def mergeKLists(self, lst) -> ListNode:
        """
        Version B
        take all val out into an ArrayList, then sort and re-link to LinkedList
        not recommended
        """

        result = []
        for node in lst:
            while node:
                result.append(node.val)
                node = node.next
        return genNode(sorted(result))


class Solution:

    def mergeKLists_X(self, lst) -> ListNode:
        """
        Version C1
        use merge two list, then use it multiple times
        但是这个合并的方法偏慢, 相当于要流经的重复节点太多次了
        """

        dummy = ListNode(float("-inf"))
        for i in lst:
            dummy = self.merge_two(dummy, i)

        return dummy.next

    def merge_two(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Helper C1
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


class Solution:

    def mergeKLists_O(self, lst) -> ListNode:
        """
        Version C2, improved
        这个方法采用首尾合并, 这样能显著减少重复流经的节点
        首尾相遇后, 重置首为0, 尾不变(因为已经都被合并到前面去了)
        """

        if not lst:
            return None

        left, right = 0, len(lst) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lst[left] = self.merge_two(lst[left], lst[right])
                left += 1
                right -= 1
        return lst[0]


if __name__ == "__main__":
    assert Solution().mergeKLists_O([]) is None, "Empty"

    single = genNode([1])
    e = Solution().mergeKLists_O([single])
    assert repr(e) == "1", "single"

    a = genNode([1, 4, 5])
    b = genNode([1, 3, 4])
    c = genNode([2, 6])
    lst = [a, b, c]
    check = Solution().mergeKLists_O(lst)
    assert repr(check) == "1->1->2->3->4->4->5->6", "Example"

    print("all passed")
