# P572 Subtree of Another Tree
# Easy


# Given two non-empty binary trees s and t
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sameTree(self, s, t):
        if s is t is None:
            return True
        elif (not s and t) or (s and not t):
            return False
        else:
            return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s and s.val == t.val:
            return self.sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        elif s and s.val != t.val:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False




if __name__ == '__main__':
    s0 = TreeNode(0)
    s1 = TreeNode(1)
    s2 = TreeNode(2)
    s4 = TreeNode(4)
    s5 = TreeNode(5)

    E1 = TreeNode(3)
    E1.left, E1.right = s4, s5
    s4.left, s4.right = s1, s2

    s11 = TreeNode(1)
    s12 = TreeNode(2)

    E2 = TreeNode(4)
    E2.left, E2.right = s11, s12

    assert Solution().isSubtree(E1, E2)

    s2.left = s0
    assert not Solution().isSubtree(E1, E2)



    z0 = TreeNode(0)
    z1 = TreeNode(1)
    z2 = TreeNode(2)
    z4 = TreeNode(4)
    z5 = TreeNode(5)
    zx = TreeNode(9)


    E3 = TreeNode(3)
    E3.right = zx
    zx.left = z4
    z4.left, z4.right = z1, z2
    assert Solution().isSubtree(E3, E2)

    print('all passed!')