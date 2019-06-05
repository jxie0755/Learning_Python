# P235 Lowest Common Ancestor of a Binary Tree
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.


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
        3,
        5,1,
        6,2,0,8,
        None,None,7,4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.right) == A, 'Example 1'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.left.right.right) == A.left, 'Example 2'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left.left, A.left.right.right) == A.left, 'Additional 1'

    A = genTree([
        3,
        5, 1,
        6, 2, 0, 8,
        None, None, 7, 4,
    ])
    assert Solution().lowestCommonAncestor(A, A.left.right, A.right.left) == A, 'Additional 2'

    A = genTree([
        2,
        None, 3
    ])
    assert Solution().lowestCommonAncestor(A, A, A.right) == A, 'Additional 3'

    A = genTree([
        2,
        1, None
    ])
    assert Solution().lowestCommonAncestor(A, A, A.left) == A, 'Additional 4'

    print('all passed')
