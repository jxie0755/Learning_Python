# P235 Lowest Common Ancestor of a Binary Search Tree
# Easy


# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pass



if __name__ == '__main__':

    A = genTree([
        6,
        2,8,
        0,4,7,9,
        None,None,3,5
    ])
    assert Solution().lowestCommonAncestor(A, root.left, root.right) == A, 'Example 1'

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])

    assert Solution().lowestCommonAncestor(A, root.left, root.left.right) == root.left, 'Example 2'

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, root.left.left, root.left.right.left) == root.left, 'Additional'

    print('all passed')
