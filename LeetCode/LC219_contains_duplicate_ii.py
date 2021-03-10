# LC219 Contains Duplicate II
# Easy


# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

from typing import *


class Solution:

    # Brutal force, O(N^2), max time limit exceeded
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False

        if k > len(nums):
            k = len(nums)

        z = 1
        while z <= k:
            i = 0
            while i != len(nums) - z:
                if nums[i] == nums[i + z]:
                    return True
                i += 1
            z += 1
        return False

    # Hashtable O(N)
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmp = {}
        i = 0
        while i != len(nums):
            if nums[i] not in hmp:
                hmp[nums[i]] = i
            else:
                if i - hmp[nums[i]] <= k:
                    return True  # 每次出现重复就检查距离是否小于k
                else:
                    hmp[nums[i]] = i  # 更新index
            i += 1
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate([], 0) == False, "Edge 0"
    assert Solution().containsNearbyDuplicate([1], 1) == False, "Edge 1"

    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) == True, "Example 1"
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) == True, "Example 2"
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False, "Example 3"
    assert Solution().containsNearbyDuplicate([2, 2], 3) == True, "Example 4"

    assert Solution().containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3) == True, "Additional 1"

    print("All passed")
