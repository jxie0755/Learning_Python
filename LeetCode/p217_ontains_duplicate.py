# P217 Contains Duplicate
# Easy

# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums):
        ### Use set() to check if length is changed
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums):
        ### Use hashtable for counting
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    assert Solution().containsDuplicate([]) == False, 'Edge 1'
    assert Solution().containsDuplicate([1]) == False, 'Edge 2'

    assert Solution().containsDuplicate([1,2,3,1]) == True, 'Example 1'
    assert Solution().containsDuplicate([1,2,3,4]) == False, 'Example 2'
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True, 'Example 3'

    print('all passed')

