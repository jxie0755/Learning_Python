# p553 Optimal Division
# Easy

# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
# However, you can add any number of parenthesis at any position to change the priority of operations.
# You should find out how to add parenthesis to get the maximum result
# and return the corresponding expression in string format.
# Your expression should NOT contain redundant parenthesis.
# Note:
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.

# """
# :type nums: List[int]
# :rtype: str
# """

class Solution:
    def optimalDivision(self, nums):
        result = str(nums[0])
        segment = []
        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                segment.append(nums[i])
            if nums[i] <= nums[i+1]:
                if segment:
                    pass




# if __name__ == '__main__':
#     print(Solution().optimalDivision([1000,100,10,2]))
#     print(Solution().optimalDivision([1000,100,10,100,100,10]))
#     pass

