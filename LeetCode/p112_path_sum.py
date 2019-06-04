# P112 Path Sum
# Easy

# Given a binary tree and a sum,
# determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    def allPath(self, root):
        """show all the paths in a non-empty root"""
        result = []

        def helper(root, cur=[]):
            if not root:
                return None
            elif not root.left and not root.right:
                cur.append(root.val)
                result.append(cur)
            else:
                if root.left:
                    new_cur = cur[:]
                    new_cur.append(root.val)
                    helper(root.left, new_cur)
                if root.right:
                    new_cur = cur[:]
                    new_cur.append(root.val)
                    helper(root.right, new_cur)

        helper(root)
        return result


    def hasPathSum(self, root: TreeNode, target: int) -> bool:

        # Borrow the idea of allPath
        def helper(root, cur=[]):
            if not root:
                return False

            elif not root.left and not root.right:
                cur.append(root.val)
                return sum(cur) == target

            else:
                left_cur, right_cur = cur[:], cur[:]
                left_cur.append(root.val)
                right_cur.append(root.val)
                return helper(root.left, left_cur) or helper(root.right, right_cur)

        return helper(root)




if __name__ == '__main__':
    A = None
    assert not Solution().hasPathSum(A, 0), "Edge 0"

    A = genTree([1])
    assert Solution().hasPathSum(A, 1), "Edge 1"

    A = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, None, 1
    ])
    assert Solution().hasPathSum(A, 22), "Example 1"

    print('All passed')
