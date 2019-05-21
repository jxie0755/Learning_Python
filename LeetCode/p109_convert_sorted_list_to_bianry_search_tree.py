# P109 Convert Sorted List to Binary Search Tree
# Medium


# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


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

# Definition for a binary tree node.
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)


def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


from typing import *

class Solution:
    ### Convert linked list to an arrayList then solve the problem like Leetcode P108



    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None

        nums = []
        while head:
            nums.append(head.val)
            head = head.next


        mid_idx = len(nums) // 2
        mid = nums[mid_idx]
        ans = TreeNode(mid)

        def helper(root, left_list, right_list):
            if left_list:
                left_mid_idx = len(left_list) // 2
                left_val = left_list[left_mid_idx]
                root.left = TreeNode(left_val)
                LL, LR = left_list[:left_mid_idx], left_list[left_mid_idx+1:]
                helper(root.left, LL, LR)

            if right_list:
                right_mid_idx = len(right_list) // 2
                right_val = right_list[right_mid_idx]
                root.right = TreeNode(right_val)
                RL, RR = right_list[:right_mid_idx], right_list[right_mid_idx + 1:]
                helper(root.right, RL, RR)

        helper(ans, nums[:mid_idx], nums[mid_idx+1:])
        return ans


if __name__ == '__main__':
    if __name__ == '__main__':
        A = None
        assert Solution().sortedListToBST(A) is None, 'Edge 0'

        A = genNode(1)
        assert Solution().sortedListToBST(A) == genTree([1]), 'Edge 1'

        A = genNode(-10, -3, 0, 5, 9)
        assert Solution().sortedListToBST(A) == genTree([0, -3, 9, -10, None, 5, None]), 'Example 1'

        print('all passed')
