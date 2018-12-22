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
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.left != None and q.left != None and p.right != None and q.right != None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p.left != None and q.left != None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and p.right == q.right == None
        elif p.right != None and q.right != None:
            return p.val == q.val and self.isSameTree(p.right, q.right) and p.left == q.left == None
        else:
            return p.val == q.val and p.left == q.left == p.right == q.right == None


if __name__ == '__main__':
    T10 = TreeNode(1)
    T10.left = TreeNode(2)
    T10.right = TreeNode(3)
    T10.left.left = TreeNode(4)

    T20 = TreeNode(1)
    T20.left = TreeNode(2)
    T20.right = TreeNode(3)
    T20.left.left = TreeNode(4)

    assert Solution().isSameTree(T10, T20) == True, 'T1'

    T10 = TreeNode(1)
    T10.left = TreeNode(2)
    T10.right = TreeNode(3)
    T10.left.left = TreeNode(4)

    T20 = TreeNode(1)
    T20.left = TreeNode(3)
    T20.right = TreeNode(2)
    T20.left.left = TreeNode(4)

    assert Solution().isSameTree(T10, T20) == False, 'T2'

    print('all passed')
