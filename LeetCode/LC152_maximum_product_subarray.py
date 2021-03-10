# LC152 Maximum Product Subarray
# Medium

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.


class Solution(object):

    # Version A, brutal force, get all subsequence and find the product
    # Failed by exceeding max time limit
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -float("inf")
        for i in range(0, len(nums)):
            for j in range(1, len(nums) - i + 1):
                sub = nums[i:i + j]
                product = 1
                for k in sub:
                    product *= k
                if product > result:
                    result = product
        return result


class Solution(object):

    # Version B
    # The idea is to find:
    # If zero in is the lst
    # if zero is in the list, then product will be zero
    # it must compare with subarray before zero and subarray after zero, with 0
    # So the subarray is nums[:zero_index] and nums[zero_index+1:]
    # number of negative number in the list
    # if number is even, then the product will be non-negative, that is good
    # if number is odd, then we need to get rid of 1 odd number (first one or last one)
    # So the subarray is nums[:last_odd_index] and nums[first_odd_index+1:]
    # End case:
    # if lst is empty, return -float("inf"), to exclude from counting
    # if lst is 1 element, then return just the element itself
    # if lst contains no zero, and even negative numbers, then return the products of all elments
    # Any other case, we recursively break down the lst to get the end case

    def product(self, lst):
        result = 1
        for i in lst:
            result *= i
        return result

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -float("inf")
        elif len(nums) == 1:
            return nums[0]

        n_neg = 0
        i_odd_first, i_odd_last = -1, -1
        oddfound = False
        i_zero = -1
        for i in range(len(nums)):
            val = nums[i]
            if val < 0:
                n_neg += 1
                if not oddfound:
                    i_odd_first = i
                    i_odd_last = i
                    oddfound = True
                else:
                    i_odd_last = i
            if val == 0:
                i_zero = i

        if i_zero == -1:  # no zero
            if n_neg % 2 == 0:  # even number of negative numbers
                return self.product(nums)
            else:  # odd number of negative numbers
                return max(self.maxProduct(nums[:i_odd_last]), self.maxProduct(nums[i_odd_first + 1:]))
        else:
            return max(0, self.maxProduct(nums[:i_zero]), self.maxProduct(nums[i_zero + 1:]))


if __name__ == "__main__":
    assert Solution().maxProduct([-2]) == -2, "Edge 0"
    assert Solution().maxProduct([2, 3, -2, 4]) == 6, "Example 1"
    assert Solution().maxProduct([-2, 0, -1]) == 0, "Example 2"
    #
    print("All passed")
