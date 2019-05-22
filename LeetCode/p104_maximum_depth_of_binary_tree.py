# P104 Maximum Depth of Binary Tree
# Easy


# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

from typing import *

from typing import *
from a0_TreeNode import *
from a0_ListNode import *



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    A = None
    assert Solution().maxDepth(A) == 0, 'Edge 0'

    A = TreeNode([1])
    assert Solution().maxDepth(A) == 1, 'Edge 1'

    A = genTree([3,9,20,None, None, 15, 7])
    assert Solution().maxDepth(A) == 3, 'Example'

    print('All passed')
