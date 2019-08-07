"""
https://leetcode.com/problems/4sum/
P018 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
"""

from typing import *

class Solution:

    """
    Version A
    Same idea from 3Sum O(N*3^N)
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        length = len(nums)
        if length < 4:
            return []

        nums = sorted(nums)
        result, i = [], 0

        while i < length - 3:
            if i == 0 or nums[i] != nums[i - 1]:  # 跳跃i
                ii = i + 1  # ii是第二个

                while ii < length - 2:
                    if ii == i + 1 or nums[ii] != nums[ii - 1]:  # 同样不要忘了跳跃ii
                        j, k = ii + 1, length - 1
                        # j 是第三个, k是尾部

                        while j < k:
                            # print([nums[i], nums[ii], nums[j], nums[k]], nums[i] + nums[ii] + nums[j] + nums[k])
                            # 正常情况就是后面两个数字头尾向中间推进
                            if nums[i] + nums[ii] + nums[j] + nums[k] < target:
                                j += 1
                            elif nums[i] + nums[ii] + nums[j] + nums[k] > target:
                                k -= 1

                            # 如果找到一个解,头尾一起动, 而且跳过一些相同解
                            else:
                                result.append([nums[i], nums[ii], nums[j], nums[k]])
                                j, k = j + 1, k - 1
                                # 这一部分必须是找到一个答案才能做,不然可能会跳过一些解

                                while j < k and nums[j] == nums[j - 1]:
                                    j += 1
                                while j < k and nums[k] == nums[k + 1]:
                                    k -= 1
                    ii += 1
            i += 1
        return result


if __name__ == "__main__":
    assert Solution().fourSum([], 0) == [], "Edge 1"
    assert Solution().fourSum([1], 0) == [], "Edge 2"
    assert Solution().fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]], "Edge 3"

    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], "Example 1"
    assert Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0) == [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3],
                                                                  [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
                                                                  [-2, 0, 0, 2], [-1, 0, 0, 1]], "Exmaple 2"
    print("all passed")
