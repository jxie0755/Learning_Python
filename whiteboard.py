# LC129 Sum Root to Leaf Numbers
# Medium


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

from typing import *
from A02_TreeNode import *


class Solution:
    all_path_num = []

    def sumNumbers(self, root: TreeNode) -> int:
        """
        Use a helper function to split recursion to collect all paths
        At the same time, move carried value in the path up by 1 decimal point during the recursion
        """
        self.convert_path_to_num(0, root)
        result = sum(self.all_path_num)
        self.all_path_num.clear()
        return result

    def convert_path_to_num(self, cur_num: int, root: TreeNode) -> None:
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
                self.convert_path_to_num(cur_num * 10 + root.val, root.left)
            if root.right:
                self.convert_path_to_num(cur_num * 10 + root.val, root.right)


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
