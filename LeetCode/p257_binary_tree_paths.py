# P257 Bianry Tree Paths
# Easy


# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        pass



if __name__ == '__main__':
    assert Solution().binaryTreePaths(None) == [], 'Edge 0'

    A = genTree([
        1,
        2,3,
        None, 5
    ])
    assert Solution().binaryTreePaths(None) ==  ["1->2->5", "1->3"], 'Example 1'

    print('all passed')
