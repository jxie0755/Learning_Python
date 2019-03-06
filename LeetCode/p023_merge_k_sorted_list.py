# P023 Merge k Sorted Lists
# Hard

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "{}->{}".format(self.val, repr(self.next))
        else:
            return "{}".format(self.val)

def genNode(*nodes, end=None):
    if len(nodes) == 1 and type(nodes[0]) == list:
        nodes = nodes[0]
    for i in nodes[::-1]:
        n = ListNode(i)
        n.next, end = end, n
    return n if nodes else None



class Solution:
    ### Exceeded time limit
    def mergeKLists(self, lst) -> ListNode:
        cur = dummy = ListNode('X')
        while any([i for i in lst]):
            i, min_val, min_idx = 0, float('inf'), float('inf')

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
    ### take all val out, then return the sorted linked list
    ### not recommended
    def mergeKLists(self, lst) -> ListNode:
        result = []
        for node in lst:
            while node:
                result.append(node.val)
                node = node.next
        return genNode(sorted(result))




class SolutionFinal:
    ### use merge two list, then use it multiple times
    def merge_two(self, l1, l2):
        """merge two sorted linked list"""
        global count
        curr = dummy = ListNode('X')
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
                count += 1
            else:
                curr.next, l2 = l2, l2.next
                count += 1
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    ### 但是这个合并的方法偏慢, 相当于要流经的重复节点太多次了
    def mergeKLists_X(self, lst) -> ListNode:
        dummy = ListNode(float('-inf'))
        for i in lst:
            dummy = self.merge_two(dummy, i)

        print("count: ", count)
        return dummy.next

    ### 这个方法采用收尾合并, 这样能显著减少重复流经的节点
    def mergeKLists_O(self, lst) -> ListNode:
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
        print("count: ", count)
        return lst[0]


count = 0
ls = [ListNode(i) for i in range(1000)]
SolutionFinal().mergeKLists_X(ls)
# >>>  count:  500500

count = 0
ls = [ListNode(i) for i in range(1000)]
SolutionFinal().mergeKLists_O(ls)
# >>> count:  8977


if __name__ == '__main__':
    assert Solution().mergeKLists([]) is None, 'Empty'
    single = genNode(1)
    e = Solution().mergeKLists([single])
    assert repr(e) == '1', 'single'

    a = genNode(1,4,5)
    b = genNode(1,3,4)
    c = genNode(2,6)
    lst = [a,b,c]
    check = Solution().mergeKLists(lst)
    assert repr(check) == '1->1->2->3->4->4->5->6', 'Example'

    print('all passed')
