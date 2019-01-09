# P015 3Sum
# Medium


# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.


class Solution:
    def twoSum_for_3sum(self, numbers, target, jump):
        ### hastable method from P001
        result = []
        hashtable = {}
        for idx in range(0, len(numbers)):
            if idx == jump:
                pass  # jump over current check in 3sum, to avoid repeat use
            elif numbers[idx] not in hashtable.keys():
                hashtable[target-numbers[idx]] = idx
            else:
                result.append([numbers[hashtable[numbers[idx]]], numbers[idx]])
                # do not return, but get every possible group of target two sum
        return result

    def threeSum(self, nums):
        ### Use modified method of two_sum
        ### with every number, check the rest of array for two_sum of (0-number)
        ### O(N^2), max time limit exceeded
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while i != len(nums):
            current = nums[i]
            two_sum = self.twoSum_for_3sum(nums, 0 - current, i)
            if two_sum:
                for ts in two_sum:
                    ans = sorted([current] + ts)
                    if ans not in result:
                        result.append(ans)
            i += 1

        return result

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass





if __name__ == '__main__':
    assert Solution().threeSum([]) == [
    ], 'Edge 1'
    assert Solution().threeSum([1]) == [
    ], 'Edge 2'
    assert Solution().threeSum([1,1]) == [
    ], 'Edge 3'

    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, 0, 1],
        [-1, -1, 2]
    ]

    print('all passed')








