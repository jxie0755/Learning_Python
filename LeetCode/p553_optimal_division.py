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
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return '/'.join(str(i) for i in nums)
        return str(nums.pop(0)) + '/' + '(' + '/'.join(str(i) for i in nums) + ')'
    # Another tricky question, there is no need to calculate how to place the parenthesis
    # The only way to gurantee for maximum result is to calculate {nums[0] / (nums[1]/nums[2]/nums[3]....)}
    # but when len(nums) == 1 or 2, special condition needs to be adjusted


if __name__ == '__main__':
    assert Solution().optimalDivision([1000,100,10,2]) == "1000/(100/10/2)"
    assert Solution().optimalDivision([2]) == "2"
    assert Solution().optimalDivision([2,3]) == "2/3"
    print('all passed')
