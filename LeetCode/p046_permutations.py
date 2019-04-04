# P046 Permutations
# Medium


# Given a collection of distinct (数字不会重复) integers, return all possible permutations.

from typing import *

import math
class Solution:
    def permute(self, nums: List[int]):

        length = len(nums)









# Solution().permute([1,2,3])
Solution().permute([1,2,3,4])


# if __name__ == '__main__':
#     assert Solution().permute([1]) == [
#         [1]
#     ], "Edge 1"
#
#
#     assert Solution().permute([1,2,3]) == [
#         [1, 2, 3],
#         [1, 3, 2],
#         [2, 1, 3],
#         [2, 3, 1],
#         [3, 1, 2],
#         [3, 2, 1]
#     ], "Example 1"
#
#     print('all passed')


# (1, 2, 3, 4)
# (1, 2, 4, 3)
# (1, 3, 2, 4)
# (1, 3, 4, 2)
# (1, 4, 2, 3)
# (1, 4, 3, 2)
# (2, 1, 3, 4)
# (2, 1, 4, 3)
# (2, 3, 1, 4)
# (2, 3, 4, 1)
# (2, 4, 1, 3)
# (2, 4, 3, 1)
# (3, 1, 2, 4)
# (3, 1, 4, 2)
# (3, 2, 1, 4)
# (3, 2, 4, 1)
# (3, 4, 1, 2)
# (3, 4, 2, 1)
# (4, 1, 2, 3)
# (4, 1, 3, 2)
# (4, 2, 1, 3)
# (4, 2, 3, 1)
# (4, 3, 1, 2)
# (4, 3, 2, 1)
