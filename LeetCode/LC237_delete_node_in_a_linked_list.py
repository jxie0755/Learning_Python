# P237 Delete Node in a Linked List
# Easy


# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Given linked list -- head = [4,5,1,9], which looks like following:
# 4 -> 5 -> 1 -> 9

# Note:
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


from a0_ListNode import *


class Solution(object):

    # Version A
    # Revise on chain, change the value to next value all the way to the end then cut the end link
    # need to create a dummy to record the previous node of this node
    def deleteNode(self, node: ListNode) -> None:
        pre = ListNode("X")
        pre.next = node
        while node.next:
            node.val = node.next.val
            node = node.next
            pre = pre.next
        pre.next = None

        # Avoid dummy:
        # while node.next != None:
        #     node.val = node.next.val
        #     pre = node
        #     node = node.next
        # pre.next = None


if __name__ == "__main__":
    A = genNode([4, 5, 1, 9])
    Solution().deleteNode(A.next)
    assert A == genNode([4, 1, 9]), "Example 1"

    A = genNode([4, 5, 1, 9])
    Solution().deleteNode(A.next.next)
    assert A == genNode([4, 5, 9]), "Example 2"

    A = genNode([4, 5, 1, 9])
    Solution().deleteNode(A)
    assert A == genNode([5, 1, 9]), "Example 3"
    print("All passed")
