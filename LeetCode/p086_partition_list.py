# P086 Partition List
# Medium


# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        cur = head
        swappoint = False
        ans = prev = ListNode("X")
        newlink = ListNode("Y")
        prev.next = newlink
        tgt = None

        while cur:
            if cur.val >= x:
                newlink.next = ListNode(cur.val)
                if not swappoint:
                    tgt = newlink.next
                    prev = prev.next
                    swappoint = True
                newlink = newlink.next

            elif cur.val < x:
                if tgt:
                    temp = ListNode(cur.val)
                    prev.next = temp
                    temp.next = tgt
                else:
                    newlink.next = ListNode(cur.val)
                    newlink = newlink.next
                prev = prev.next
            cur = cur.next

        return ans.next.next


if __name__ == "__main__":
    sample = None
    assert repr(Solution().partition(sample, 5)) == "None", "Edge 1"

    sample = genNode([9, 1, 4, 3, 2, 5, 2])
    assert repr(Solution().partition(sample, 9)) == "1->4->3->2->5->2->9", "Edge 2"

    sample = genNode([1, 4, 3, 2, 5, 2])
    assert repr(Solution().partition(sample, 3)) == "1->2->2->4->3->5", "Example 1"
    print("all passed")
