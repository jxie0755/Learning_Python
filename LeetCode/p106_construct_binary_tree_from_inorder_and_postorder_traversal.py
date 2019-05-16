# P106 Construct Binary Tree from Inorder and Postorder Traversal
# Medium


# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.


from typing import *

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

    def isLeaf(self):
        try:
            leftval = self.left.val
        except AttributeError:
            leftval = None
        try:
            rightval = self.right.val
        except AttributeError:
            rightval = None

        return leftval and rightval

def genTree(lst):
    """
    generate a binary tree according to a non-empty list of values
    The lst must be all filled, even the branch is empty, then use None to suggest the empty treeNode
    """
    if not lst:
        return None

    LLL = log(len(lst)+1,2)
    if int(LLL) != LLL:
        print("List length is not complete, it must be 2^n - 1")
        raise ZeroDivisionError

    layers = []
    i, L = 0, 1

    while i != len(lst):
        layers.append(lst[i:i + L])
        i += L
        L *= 2
    pre_root = [TreeNode(i) for i in layers[0]]
    root_to_return = pre_root[0]

    for k in range(1, len(layers)):
        cur = []
        for i in layers[k]:
            if i is not None:
                cur.append(TreeNode(i))
            else:
                cur.append(None)

        for j in range(len(cur)):
            rt_idx, brc_side = divmod(j, 2)
            if brc_side == 0 and cur[j] is not None:
                pre_root[rt_idx].left = cur[j]
            elif brc_side != 0 and cur[j] is not None:
                pre_root[rt_idx].right = cur[j]
        pre_root = cur

    return root_to_return


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        pass


A = genTree([
        3,
        9,20,
        None,None,15,7
    ])

print(Solution().postorderTraversal(A))


# if __name__ == '__main__':
#     assert not Solution().buildTree([],[]), 'Edge 0'
#     assert Solution().buildTree([1],[1]) == genTree([1]), 'Edge 1'
#     assert Solution().buildTree([9,3,15,20,7],[9,15,7,20,3]) == genTree([
#         3,
#         9,20,
#         None,None,15,7
#     ]), 'Example 1'
#
#     print('all passed')
