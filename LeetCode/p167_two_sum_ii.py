# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.



class Solution:
    def twoSum(self, numbers, target):
        ### This will work but fail in long list, as exceed time limit
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while numbers[i] <= target // 2:
            j = 1
            while i + j <= len(numbers) -1:
                two_sum = numbers[i] + numbers[i+j]
                if two_sum > target:
                    break
                elif two_sum == target:
                    return [i+1, i+j+1]
                j += 1
            i += 1




if __name__ == '__main__':
    assert Solution().twoSum([2,7,11,15], 9) == [1, 2], 'Example'
    assert Solution().twoSum([5,25,75], 100) == [2, 3], 'T1'
    assert Solution().twoSum([-1, 0], -1) == [1, 2], 'T2'
    assert Solution().twoSum([1,2,3,4,4,9,56,90], 8) == [4, 5], 'T3'
    print('all passed')



