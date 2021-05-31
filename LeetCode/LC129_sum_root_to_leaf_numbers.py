"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
LC129 Sum Root to Leaf Numbers
Medium


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.
"""

from typing import *
from A02_TreeNode import *


class Solution:
    # This is also using the showPaths method from Leetcode LC112
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

    def translate(self, path):
        """
        translate a path into numbers by adding digit up
        example: path [1,2,3] returns number 123
        """
        N = len(path)
        result = 0
        for i in range(N):
            result += pow(10, N - 1 - i) * path[i]
        return result

    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        for path in self.allPath(root):
            result += self.translate(path)
        return result


if __name__ == "__main__":
    A = genTree([
        1,
        2, 3
    ])
    assert Solution().sumNumbers(A) == 25, "Example 1, 12 + 13 = 25"

    A = genTree([
        4,
        9, 0,
        5, 1, None, None
    ])
    assert Solution().sumNumbers(A) == 1026, "Example 2, 495 + 491 + 40 = 1036"
    print("All passed")
