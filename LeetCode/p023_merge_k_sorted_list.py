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
        dummy = ListNode('X')
        cur = dummy
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

    ### Exceeded time limit
    def mergeKLists(self, lst) -> ListNode:
        dummy = ListNode('X')
        cur = dummy
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

    def mergeKLists(self, lst) -> ListNode:
        result = []
        for node in lst:
            while node:
                result.append(node.val)
                node = node.next
        return genNode(sorted(result))


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
