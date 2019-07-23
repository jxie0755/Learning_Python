# P031 Next Permutation
# Medium

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# Do not return anything, modify nums in-place instead!

# The replacement must be in-place and use only constant extra memory.
# Means you cannot list out all permutation and sort it, then find the next one.

# Correct sequence (sorted):
# 1 2 3 - 1 3 2 - 2 1 3 - 2 3 1 - 3 1 2 - 3 2 1

# [(1, 2, 3, 4),
#  (1, 2, 4, 3),
#  (1, 3, 2, 4),
#  (1, 3, 4, 2),
#  (1, 4, 2, 3),
#  (1, 4, 3, 2),
#  (2, 1, 3, 4),
#  (2, 1, 4, 3),
#  (2, 3, 1, 4),
#  (2, 3, 4, 1),
#  (2, 4, 1, 3),
#  (2, 4, 3, 1),
#  (3, 1, 2, 4),
#  (3, 1, 4, 2),
#  (3, 2, 1, 4),
#  (3, 2, 4, 1),
#  (3, 4, 1, 2),
#  (3, 4, 2, 1),
#  (4, 1, 2, 3),
#  (4, 1, 3, 2),
#  (4, 2, 1, 3),
#  (4, 2, 3, 1),
#  (4, 3, 1, 2),
#  (4, 3, 2, 1)]

from itertools import permutations
import math


class Solution:
    def nextPermutation(self, nums):
        # Use itertool.permutations itearate the permutation sequence from small to large,
        # and stop at the nums, then return the next one
        # Exceeded max time limit
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first_sample = False
        length = len(nums)

        for i in permutations(sorted(nums), length):
            check = list(i)
            if first_sample is False:
                first = check
                first_sample = True
            if check > nums:
                nums[:] = check
                first_sample = False
                break

        if first_sample:
            nums[:] = first


class Solution:
    def nextPermutation(self, nums):
        # O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] < nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] > nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break

    # Addtional: prevPermute, which is the reverse process
    def prevPermutation(self, nums):
        # O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] > nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] < nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break
        return nums


if __name__ == "__main__":
    a = []
    Solution().nextPermutation(a)
    assert a == [], "Edge 1"

    a = [1]
    Solution().nextPermutation(a)
    assert a == [1], "Edge 2"

    a = [1, 2]
    Solution().nextPermutation(a)
    assert a == [2, 1], "Edge 3"

    a = [1, 2, 3]
    Solution().nextPermutation(a)
    assert a == [1, 3, 2], "Example 1"

    a = [3, 2, 1]
    Solution().nextPermutation(a)
    assert a == [1, 2, 3], "Example 2"

    a = [1, 1, 5]
    Solution().nextPermutation(a)
    assert a == [1, 5, 1], "Example 3"

    a = [5, 1, 1]
    Solution().nextPermutation(a)
    assert a == [1, 1, 5], "Extra 1"

    a = [2, 2, 2]
    Solution().nextPermutation(a)
    assert a == [2, 2, 2], "Extra 2"

    a = [1, 2, 2, 2]
    Solution().nextPermutation(a)
    assert a == [2, 1, 2, 2], "Extra 3"

    a = [2, 3, 1]
    Solution().nextPermutation(a)
    assert a == [3, 1, 2]

    print("all passed")
