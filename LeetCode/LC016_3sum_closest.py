"""
https://leetcode.com/problems/3sum-closest/
P016 3Sum Closest
Medium

Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""

from typing import *

class Solution_A:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Similar structure as 3Sum.
        Revise by checking the 3Sum with Target, and update the 3sum of lowest diff
        """

        nums = sorted(nums)
        diff = float("inf")
        result = float("inf")

        for i in range(len(nums) - 2):

            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1 # j 是下一个, k是尾部

                while j < k: # j和k后面两个数字头尾向中间推进
                    three_sum = nums[i] + nums[j] + nums[k]

                    check = abs(three_sum - target)
                    if check < diff: # update result by checking diff
                        diff = check
                        result = three_sum

                    if three_sum < target:
                        j += 1
                    elif three_sum > target:
                        k -= 1

                    # 如果找到一个解, 也就是刚好等于target, 那就直接return
                    # 不需要像LC015那样去重, 因为我们只找一个答案, 不是一组数组
                    else:
                        return result

        return result


if __name__ == "__main__":
    testCase = Solution_A()
    # No need to test edge as gurantee to have exactly one solution
    assert testCase.threeSumClosest([1, 1, 1], 1000) == 3, "Edge"
    assert testCase.threeSumClosest([-1, 2, 1, -4], 1) == 2, "Example 1"
    assert testCase.threeSumClosest([-1, 2, 1, -1], 0) == 0, "Match"

    print("all passed")
