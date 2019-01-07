# P219 Contains Duplicate II
# Easy



# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        ### Brutal force, O(N^2), max time limit exceeded
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        if k > len(nums):
            k = len(nums)

        z = 1
        while z <= k:
            i = 0
            while i != len(nums) - z:
                if nums[i] == nums[i+z]:
                    return True
                i += 1
            z += 1
        return False

    def containsNearbyDuplicate(self, nums, k):
        ### Hashtable O(N)
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashtable = {}
        i = 0
        while i != len(nums):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = i
            else:
                if i - hashtable[nums[i]] <= k:
                    return True             # 每次出现重复就检查距离是否小于k
                else:
                    hashtable[nums[i]] = i  # 更新index
            i += 1
        return False


if __name__ == '__main__':
    assert Solution().containsNearbyDuplicate([], 0) == False, 'Edge 1'
    assert Solution().containsNearbyDuplicate([1], 1) == False, 'Edge 2'

    assert Solution().containsNearbyDuplicate([1,2,3,1], 3) == True, 'Example 1'
    assert Solution().containsNearbyDuplicate([1,0,1,1], 1) == True, 'Example 2'
    assert Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2) == False, 'Example 3'
    assert Solution().containsNearbyDuplicate([2,2], 3) == True, 'Example 3'

    assert Solution().containsNearbyDuplicate([0,1,2,3,2,5], 3) == True, 'Additional 1'

    print('all passed')
