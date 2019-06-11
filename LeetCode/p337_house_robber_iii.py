# P337 House Robber III
# Medium


# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.


from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution:
    def rob(self, root: TreeNode) -> int:
        pass







if not __name__ == '__main__':

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
    print('all passed')
