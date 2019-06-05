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

    # Version A1
    # use a helper function to recursive check
    # first get the range of the root (min and max)
    # if p's val and q's val within the range, check the left and right until neither's range covers
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pv, qv = p.val, q.val
        minn = maxx = root
        while minn.left:
            minn = minn.left
        while maxx.right:
            maxx = maxx.right

        result = []
        def helper(root, A, B):
            rv = root.val
            if A <= pv <= B and A <= qv <= B:
                result.append(root)
                if root.left:
                    helper(root.left, A, rv-1)
                if root.right:
                    helper(root.right, rv+1, B)

        helper(root, minn.val, maxx.val)
        return result[-1]

    # Version A2
    # Non-recursive version
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pv, qv = p.val, q.val
        minn = maxx = root
        while minn.left:
            minn = minn.left
        while maxx.right:
            maxx = maxx.right
        minv, maxv = minn.val, maxx.val

        while minv <= pv <= maxv and minv <= qv <= maxv:
            rv = root.val
            if minv <= pv <= rv-1 and minv <= qv <= rv-1:
                root = root.left
            elif rv+1 <= pv <= maxv and rv+1 <= qv <= maxv:
                root = root.right
            else:
                return root

if __name__ == '__main__':

    A = genTree([
        6,
        2,8,
        0,4,7,9,
        None,None,3,5
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.right) == A, 'Example 1'

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, A.left, A.left.right) == A.left, 'Example 2'

    A = genTree([
        6,
        2, 8,
        0, 4, 7, 9,
        None, None, 3, 5
    ])
    assert Solution().lowestCommonAncestor(A, A.left.left, A.left.right.left) == A.left, 'Additional 1'

    A = genTree([
        2,
        None, 3
    ])
    assert Solution().lowestCommonAncestor(A, A, A.right) == A, 'Additional 2'

    A = genTree([
        2,
        1, None
    ])
    assert Solution().lowestCommonAncestor(A, A, A.left) == A, 'Additional 3'

    print('all passed')
