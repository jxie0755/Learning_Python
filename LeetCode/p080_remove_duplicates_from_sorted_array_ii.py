# P080 Remove Duplicates from Sorted Array II
# Medium



# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hmp = dict()
        i = 0
        count = 0
        while i != len(nums):
            cur = nums[i]
            if cur not in hmp:
                hmp[cur] = 1
                count += 1
                i += 1
            elif hmp[cur] <= 1:
                hmp[cur] += 1
                count += 1
                i += 1
            else:
                nums.pop(i)

        return count


if __name__ == '__main__':
    a = []
    assert Solution().removeDuplicates(a) == 0, 'Edge 0'

    a = [1]
    assert Solution().removeDuplicates(a) == 1, 'Edge 1'

    a = [1,1,1,2,2,3]
    assert Solution().removeDuplicates(a) == 5, 'Example 1'
    print(a)

    a = [0,0,1,1,1,1,2,3,3]
    assert Solution().removeDuplicates(a) == 7, 'Example 2'
    print(a)

    print('all passed')
