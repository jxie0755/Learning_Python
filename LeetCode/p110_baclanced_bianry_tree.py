# P110 Balanced Binary Tree
# Easy


# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



# Definition for a binary tree node.
from math import log

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            if T.val is None:
                return 'N'

            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + layer(T.right, L + 1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L + 1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L + 1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

    def __eq__(self, other):
        return str(self) == str(other)


def genTree(lst, i=1):
    """
    To generate a perfect binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if lst and i <= len(lst) and lst[i-1] is not None:
        node = TreeNode(lst[i-1])
        node.left = genTree(lst, i*2)
        node.right = genTree(lst, i*2+1)
        return node


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)



if __name__ == '__main__':
    A = None
    assert Solution().isBalanced(A), 'Edge 0'

    A = genTree([1])
    assert Solution().isBalanced(A), 'Edge 1'

    A = genTree([
        3,
        9,20,
        None,None,15,7])

    assert Solution().isBalanced(A), 'Example 1'

    A = genTree([
        1,
        2, 2,
        3, 3, None, None,
        4, 4, None, None, None, None, None, None
    ])

    assert not Solution().isBalanced(A), 'Example 2'

    A = genTree([
        1,
        2,2,
        3,3,3,3,
        4,4,4,4,4,4,None,None,
        5,5,None,None,None,None,None,None,None,None,None,None,None,None,None,None,
    ])

    assert Solution().isBalanced(A), 'Additional 1'


    A = genTree([
        1,
        None, 2,
        None, None, None, 3
    ])
    assert not Solution().isBalanced(A), 'Additional 2'

    print('all passed')



