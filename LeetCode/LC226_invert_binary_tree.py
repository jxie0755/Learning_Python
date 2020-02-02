# P226 Invert Binary Tree
# Easy

# Invert a binary tree.
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you canâ€™t invert a binary tree on a whiteboard so f*** off.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    # Version A, simple recursive way
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        L, R = root.left, root.right
        root.left = self.invertTree(R)
        root.right = self.invertTree(L)
        return root


if __name__ == "__main__":
    assert Solution().invertTree(None) is None, "Edge 0"

    A = genTree([1])
    assert Solution().invertTree(A) == A, "Edge 1"

    A = genTree([
        4,
        2, 7,
        1, 3, 6, 9
    ])

    B = genTree([
        4,
        7, 2,
        9, 6, 3, 1
    ])
    assert Solution().invertTree(A) == B, "Example 1"

    A = genTree([
        4,
        2, 7,
        None, 3, None, 9
    ])

    B = genTree([
        4,
        7, 2,
        9, None, 3, None
    ])
    assert Solution().invertTree(A) == B, "Example 1b"

    print("all passed")
