# p100 Same Tree
# Easy


# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Note:
# Mirrored trees are considered not the same


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """





if __name__ == '__main__':
    T10 = TreeNode(1)
    T10.left = TreeNode(2)
    T10.right = TreeNode(3)
    T10.left.left = TreeNode(4)

    T20 = TreeNode(1)
    T20.left = TreeNode(2)
    T20.right = TreeNode(3)
    T20.left.left = TreeNode(4)

    assert Solution().isSameTree(T10, T20) == True

    T10 = TreeNode(1)
    T10.left = TreeNode(2)
    T10.right = TreeNode(3)
    T10.left.left = TreeNode(4)

    T20 = TreeNode(1)
    T20.left = TreeNode(3)
    T20.right = TreeNode(2)
    T20.left.left = TreeNode(4)

    assert Solution().isSameTree(T10, T20) == False

    print('all passed')
