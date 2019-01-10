# P031 Next Permutation
# Medium

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == '__main__':
    assert Solution().nextPermutation([]) == [], 'Edge 1'
    assert Solution().nextPermutation([1]) == [1], 'Edge 2'

    assert Solution().nextPermutation([1,2]) == [2,1], 'Edge 2'
    assert Solution().nextPermutation([1,2,3]) == [1,3,2], 'Example 1'
    assert Solution().nextPermutation([3,2,1]) == [1,2,3], 'Example 2'
    assert Solution().nextPermutation([1,1,5]) == [1,5,1], 'Example 3'

    print('all passed')









