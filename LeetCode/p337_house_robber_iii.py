# P337 House Robber III
# Medium


# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:

    # Version A1
    # Recursive check next layer and next next layer
    # Exceeded max time limit
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            L, LL, LR, R, RL, RR = 0,0,0,0,0,0

            if root.left:
                L = self.rob(root.left)
                if root.left.left:
                    LL = self.rob(root.left.left)
                if root.left.right:
                    LR = self.rob(root.left.right)

            if root.right:
                R = self.rob(root.right)
                if root.right.left:
                    RL = self.rob(root.right.left)
                if root.right.right:
                    RR = self.rob(root.right.right)

            return max(root.val + LL + LR + RL + RR, L + R)


class Solution:

    # Version A2
    # Recursive check next layer and next next layer with help of memorization (twice faster)
    # Exceeded max time limit
    def rob(self, root: TreeNode) -> int:

        hmp = {}

        def helper(root):

            if not root:
                return 0

            elif root in hmp:
                return hmp[root]

            else:
                L, LL, LR, R, RL, RR = 0, 0, 0, 0, 0, 0

                if root.left:
                    L = helper(root.left)
                    if root.left.left:
                        LL = helper(root.left.left)
                    if root.left.right:
                        LR = helper(root.left.right)

                if root.right:
                    R = self.rob(root.right)
                    if root.right.left:
                        RL = helper(root.right.left)
                    if root.right.right:
                        RR = helper(root.right.right)


                ans = max(root.val + LL + LR + RL + RR, L + R)
                hmp[root] = ans
                return ans

        return helper(root)

# class Solution:
#
#     # Version B
#     # Do it by checking the layers
#     def showLayerSums(self, root):  # Omit None
#         """Show the tree layer by layer from top to bottom"""
#         if root is None:
#             return []
#
#         result, current = [], [root]
#         while current:
#             next_level, vals = [], []
#             for node in current:
#                 vals.append(node.val)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             current = next_level
#             result.append(sum(vals)) # revised to get the sum of layers
#
#         return result
#
#
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         layersums = self.showLayerSums(root)
#         N = len(layersums)
#         print(layersums)
#         def helper(i):
#             """recursive calculate like Version A but in list"""
#             if i > N-1:
#                 return 0
#             elif i == N-1:
#                 return layersums[i]
#             else:
#                 return max(layersums[i] + helper(i+2), helper(i+1))
#         return helper(0)





if __name__ == '__main__':

    assert Solution().rob(None) == 0, 'Edge'

    A = genTree([
        3,
        2,3,
        None,3,None,1
    ])

    assert Solution().rob(A) == 7, 'Example 1'


    A = genTree([
        3,
        4,5,
        1,3,None,1
    ])
    assert Solution().rob(A) == 9, 'Example 2'


    A = genTree([
        10,
        1,2,
        20,2,3,4

    ])
    assert Solution().rob(A) == 39, 'Example 3'

    A = genTree([
        100,
        1, 1,
        10, 10, 10, 10,
        1000,1000,1000,1000,1000,1000,1000,1000,
    ])
    assert Solution().rob(A) == 8100, 'Example 4'

    A = genTree([
        2,
        1, 3,
        None, 4,
    ])
    assert Solution().rob(A) == 7, 'Example 5'

    print('all passed')
