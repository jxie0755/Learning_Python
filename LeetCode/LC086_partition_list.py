"""
https://leetcode.com/problems/partition-list/
P086 Partition List
Medium


Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


from a0_ListNode import *


class Solution_A:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        This will have to create new nodes (not the best way)
        """

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


class Solution_B:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Move in-place, no need to create new node
        """

        if not head:
            return head

        pre = dumb = ListNode("X")
        dumb.next = head

        # First find where is the partition node
        while pre and pre.next:
            if pre.next.val >= x:  # find the first partition point
                break
            else:
                pre = pre.next
        else:  # if find no partition point just return head
            return head

        partition_head = partition_tail = pre.next  # partition can have length
        check = partition_tail.next
        while check:
            if check.val < x:
                this_node = check  # record current check
                check = check.next  # move check to next

                # move this current node between pre and partition head
                pre.next = this_node
                this_node.next = partition_head

                partition_tail.next = check  # link partition_tail to next node
                pre = pre.next  # move pre after squeeze in
            else:
                partition_tail = partition_tail.next  # extend the partition part
                check = check.next
        return dumb.next


if __name__ == "__main__":
    testCase = Solution_A()

    q1 = None
    assert repr(testCase.partition(q1, 5)) == "None", "Edge 0"

    q2 = genNode([9, 1, 4, 3, 2, 5, 2])
    assert repr(testCase.partition(q2, 9)) == "1->4->3->2->5->2->9", "Edge 1"

    q3 = genNode([1])
    assert repr(testCase.partition(q3, 2)) == "1", "Edge 2"

    q4 = genNode([1, 4, 3, 2, 5, 2])
    assert repr(testCase.partition(q4, 3)) == "1->2->2->4->3->5", "Example 1"
    # only move 2 and 2 before 3, but 4 will still be before 3.

    print("All passed")
