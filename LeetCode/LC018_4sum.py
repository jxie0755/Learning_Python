"""
https://leetcode.com/problems/4sum/
LC018 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
"""

from typing import *


class Solution_A:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Same idea from 3Sum STD solution
        Time O(N*3^N)
        """
        length = len(nums)
        if length < 4:
            return []

        nums = sorted(nums)
        result = []

        for i in range(length - 3):
            if i == 0 or nums[i] != nums[i - 1]:  # 跳跃i

                for ii in range(i+1, length - 2):
                    if ii == i + 1 or nums[ii] != nums[ii - 1]:  # 同样不要忘了跳跃ii

                        j = ii + 1     # j是第三个
                        k = length - 1 # k是尾部

                        while j < k:
                            # print([nums[i], nums[ii], nums[j], nums[k]], nums[i] + nums[ii] + nums[j] + nums[k])
                            # 正常情况就是后面两个数字头尾向中间推进

                            four_sum = nums[i] + nums[ii] + nums[j] + nums[k]
                            if four_sum < target:
                                j += 1
                            elif four_sum > target:
                                k -= 1

                            # 如果找到一个解,头尾一起动, 而且跳过一些相同解
                            else:
                                temp = [nums[i], nums[ii], nums[j], nums[k]]
                                result.append(temp)
                                j = j + 1
                                k = k - 1

                                # 类似3Sum一样的去重
                                # 这一部分必须是找到一个答案才能做,不然可能会跳过一些解
                                while j < k and nums[j] == nums[j - 1]:
                                    j += 1
                                while j < k and nums[k] == nums[k + 1]:
                                    k -= 1
        return result


if __name__ == "__main__":
    testCase = Solution_A()
    assert testCase.fourSum([], 0) == [], "Edge 0"
    assert testCase.fourSum([1], 0) == [], "Edge 1"
    assert testCase.fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]], "Edge 2"

    assert testCase.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], "Example 1"
    assert testCase.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0) == [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3],
                                                                  [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
                                                                  [-2, 0, 0, 2], [-1, 0, 0, 1]], "Exmaple 2"
    print("All passed")
