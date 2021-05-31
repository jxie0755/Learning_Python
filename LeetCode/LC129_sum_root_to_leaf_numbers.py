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


class Solution_A:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        for path in self.allPath(root):
            result += self.translate(path)
        return result

    def allPath(self, root) -> List[List[int]]:
        """
        show all the paths in a non-empty root
        Helper funcion from Leetcode LC112
        """
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

    def translate(self, path) -> int:
        """
        translate a path into numbers by adding digit up
        example: path [1,2,3] returns number 123
        """
        N = len(path)
        result = 0
        for i in range(N):
            result += pow(10, N - 1 - i) * path[i]
        return result


class Solution_B:
    all_path_num = []

    def sumNumbers(self, root: TreeNode) -> int:
        """
        Use a helper function to split recursion to collect all paths
        At the same time, move carried value in the path up by 1 decimal point during the recursion
        """
        self.convert_all_path(0, root)
        result = sum(self.all_path_num)
        self.all_path_num.clear()
        return result

    def convert_all_path(self, cur_num: int, root: TreeNode) -> None:
        """
        A helper function to collect all paths and convert the path into numbers at the same time
        """
        if not root:
            pass
        elif not root.left and not root.right:  # root is leaf
            cur_num = cur_num * 10 + root.val  # convert numbers up 1 decimal point
            self.all_path_num.append(cur_num)
        else:
            # convert decimal and split left and right
            if root.left:
                self.convert_all_path(cur_num * 10 + root.val, root.left)
            if root.right:
                self.convert_all_path(cur_num * 10 + root.val, root.right)


if __name__ == "__main__":
    testCase = Solution_B()

    A = genTree([
        1,
        2, 3
    ])
    assert testCase.sumNumbers(A) == 25, "Example 1, 12 + 13 = 25"

    A = genTree([
        4,
        9, 0,
        5, 1, None, None
    ])
    assert testCase.sumNumbers(A) == 1026, "Example 2, 495 + 491 + 40 = 1036"
    print("All passed")
