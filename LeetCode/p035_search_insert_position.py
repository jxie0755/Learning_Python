# p035 Search Insert Position
# Easy

# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array

# """
# :type nums: List[int]
# :type target: int
# :rtype: int
# """

class Solution:
    def searchInsert(self, nums, target):
        new_nums = sorted(nums + [target])
        index = 0
        while index <= len(new_nums):
            if new_nums[index] == target:
                return index
            index += 1


if __name__ == '__main__':
    assert Solution().searchInsert([1,3,5,6], 5) == 2, 'In the list'
    assert Solution().searchInsert([1,3,5,6], 2) == 1, 'Not in the list'
    assert Solution().searchInsert([1,3,5,6], 7) == 4, 'At the end'
    assert Solution().searchInsert([1,3,5,6], 0) == 0, 'At the beginning'
    print('all passed')
