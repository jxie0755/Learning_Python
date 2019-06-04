# P230 Kth Smallest Element in a BST
# Medium


# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    ### Version A
    ### Indorder traverse to ge the sorted list, then get lst[k-1]
    ### This is slow as it forces to go through all BST first
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorderTraversal(root)[k-1]


class Solution(object):

    ### Version B


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorderTraversal(root)[k-1]



if __name__ == '__main__':
    A = genTree([
        3,
        1,4,
        None, 2
    ])
    assert Solution().kthSmallest(A, 1) == 1, 'Example 1'

    A = genTree([
        5,
        3,6,
        2,4,None,None,
        1,
    ])
    assert Solution().kthSmallest(A, 3) == 3, 'Example 2'

    print('all passed')
