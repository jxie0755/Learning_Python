# P124 Binary Tree Maximum Path Sum
# Hard


# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

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
    def showPerfectLayer(self, root):
        if not root:
            return []
        result = [root]
        layer = [root]
        while any(layer):
            new_layer = []
            for i in layer:
                if not i:
                    new_layer.append(None)
                    new_layer.append(None)
                else:
                    new_layer.append(i.left if i.left else None)
                    new_layer.append(i.right if i.right else None)
            result += new_layer
            layer = new_layer
        return result


    def maxPathSum(self, root: TreeNode) -> int:
        pass




A = genTree([
        -1,
        1,-1,
        1,1,-1,-1,
        -1,-1
    ])

Alist = Solution().showPerfectLayer(A)
AvaList =[]
for i in Alist:
    if i:
        AvaList.append(i.val)
    else:
        AvaList.append(None)
print(AvaList)









# if __name__ == '__main__':
#
#     A = TreeNode(1)
#     assert Solution().maxPathSum(A) == 1, 'Edge 1'
#
#     A = genTree([
#         1,
#         2,3
#     ])
#     assert Solution().maxPathSum(A) == 6, 'Example 1, 2+1+3 = 6'
#
#     A = genTree([
#         -10,
#         9, 20,
#         None, None, 15, 7
#     ])
#     assert Solution().maxPathSum(A) == 42, 'Example 2, 15+20+7 = 42'
#
#     A = genTree([
#         1,
#         2,3,
#         4,5,6,7,
#         8,9,100,11,12,100,14,15
#     ])
#     assert Solution().maxPathSum(A) == 217, 'Additional 1, 100+5+2+1+3+6+100=217'
#
#
#     A = genTree([
#         -1,
#         5, 6
#     ])
#     assert Solution().maxPathSum(A) == 10, 'Additional 2, 5+-1+6=10'
#
#     A = genTree([
#         -1,
#         5, -1
#     ])
#     assert Solution().maxPathSum(A) == 5, 'Additional 3, just 5'
#
#     A = genTree([
#         -1,
#         1,-1,
#         1,1,-1,-1,
#         -1,-1
#     ])
#     assert Solution().maxPathSum(A) == 3, 'Additional 4, 1+1+1=3'
#
#     print('all passed')
