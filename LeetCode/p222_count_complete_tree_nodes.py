# P222 Count Complete Tree Nodes
# Medium


# Given a complete binary tree, count the number of nodes.

# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):

    ### Version A1
    ### Use memorization to tell if a node is complete or not and exam every node
    ### Passed, but slow

    def isComplete(self, root):
        completes = {}

        def helper(root):
            if root in completes:
                return True
            if not root.left and not root.right:
                completes[root] = 1
                return True
            elif root.left and not root.left.left and not root.left.right and not root.right:
                completes[root] = 1
                return True
            elif root.left and helper(root.left) and root.right and helper(root.right):
                completes[root] = 1
                return True
            else:
                return False

        return helper(root)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        count = []
        def helper(root):
            if self.isComplete(root):
                count.append(1)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return len(count)


class Solution(object):

    ### Version A2
    ### Do not use memorization, direct tell a node is complete or not and exam every node
    ### Same spped, but still slow

    def isComplete(self, root):

        if not root.left and not root.right:
            return True
        elif root.left and not root.left.left and not root.left.right and not root.right:
            return True
        elif root.left and self.isComplete(root.left) and root.right and self.isComplete(root.right):
            return True
        else:
            return False

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        count = []
        def helper(root):
            if self.isComplete(root):
                count.append(1)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(root)
        return len(count)


class Solution(object):

    ### Version B
    ### Combine isComplete and count in one function, through a recursive call on helper
    ### by Examine the isComplete in helper(root), it forced to check isComplete every node in the root
    ### use memorization, direct tell a node is complete or not and exam every node
    ### As a side effect, when checking the isComplete in helper, add to count if it is the first time found as isComplete
    ### passed much faster

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        hmp = {}
        def helper(root):

            # memorization from hmp
            if root in hmp:
                return True

            if not root:
                return False

            # if node as leaf
            elif not root.left and not root.right:
                hmp[root] = root.val
                return True

            # if node has two childrien, force to check both
            elif root.left and root.right:
                A = helper(root.left)
                B = helper(root.right)
                if A and B: # avoid shortcircuit, must check A and B ahead
                    hmp[root] = root.val
                    return True
                else:
                    return False

            elif root.left:
                # check node anyway to cover all nodes
                helper(root.left)
                if not root.left.left and not root.left.right:
                    hmp[root] = root.val
                    return True
                else:
                    return False
            else:
                # check node anyway to cover all nodes
                helper(root.right)
                return False

        helper(root)

        # as a side effect, hmp will record all nodes that is complete
        return len(hmp)




if __name__ == '__main__':
    assert Solution().countNodes(None) == 0, 'Edge'

    A = genTree([
        1,
        2,3,
        4,5,6,None
    ])

    assert Solution().countNodes(A) == 6, 'Example 1'

    A = genTree([
        1,
        2,None,
        4,5,None,None
    ])

    assert Solution().countNodes(A) == 3, 'Additional 1'

    A = genTree([
        1,
        None, 3,
        None, None, None, 5,
    ])

    assert Solution().countNodes(A) == 1, 'Additional 2'

    print('all passed')
