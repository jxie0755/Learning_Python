# P101 Symmetric Tree
# Easy

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):

        def layer(T, L=1):
            s = str(T.val)
            if T.left and T.right:
                return s + '\n' + '  ' * L + layer(T.left, L+1) + '\n' + '  ' * L + layer(T.right, L+1)
            elif T.left and not T.right:
                return s + '\n' + '  ' * L + layer(T.left, L+1) + '\n' + '  ' * L + 'N'
            elif not T.left and T.right:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + layer(T.right, L+1)
            else:
                return s + '\n' + '  ' * L + 'N' + '\n' + '  ' * L + 'N'

        return layer(self)

def genTree(lst):
    """
    generate a tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    root = TreeNode(lst[0])

    def helper(rt, lst):
        half_l = len(lst) // 2
        left, right = lst[1:1+half_l], lst[1+half_l:]
        b1, b2 = TreeNode(left[0]), TreeNode(right[0])
        rt.left, rt.right = b1, b2

        if len(left) == len(right) == 1:
            return root
        else:
            helper(b1, left)
            helper(b2, right)

    if len(lst) == 1:
        return root
    else:
        helper(root, lst)
        return root






A1 = TreeNode(1)
B1 = TreeNode(2)
B2 = TreeNode(2)
C1 = TreeNode(3)
C2 = TreeNode(4)
C3 = TreeNode(3)
C4 = TreeNode(4)

A1.left = B1
A1.right = B2
B1.left = C1
B2.right = C4

print(A1)

print(genTree([1, 2, 2, 3, None, None, 4]))



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        pass



# if __name__ == '__main__':
#     pass
