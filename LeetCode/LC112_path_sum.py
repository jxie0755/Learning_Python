"""
https://leetcode.com/problems/path-sum/
P112 Path Sum
Easy

Given a binary tree and a sum,
determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""

from a0_TreeNode import *


class Solution_A:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        """
        Borrow the idea of allPath
        """
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


if __name__ == "__main__":
    testCase = Solution_A()

    T0 = None
    assert not testCase.hasPathSum(T0, 0), "Edge 0"

    T1 = genTree([1])
    assert testCase.hasPathSum(T1, 1), "Edge 1"

    T2 = genTree([
        5,
        4, 8,
        11, None, 13, 4,
        7, 2, None, None, None, None, None, 1
    ])
    assert testCase.hasPathSum(T2, 22), "Example 1, 5+4+11+2"

    T3 = genTree([
        1,
        2, 3
    ])
    assert not testCase.hasPathSum(T3, 5), "Example 2"

    T4 = genTree([
        1,
        2, None
    ])
    assert not testCase.hasPathSum(T4, 0), "Example 3"

    print("All passed")
