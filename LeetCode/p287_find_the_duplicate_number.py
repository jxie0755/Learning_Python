# P287 Find the Duplicate Number
# Medium


# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


class Solution:

    # 直立棉实质上存在一个等差数列
    def findDuplicate(self, nums: List[int]) -> int:
        pass



if __name__ == '__main__':
    assert Solution().findDuplicate([1,3,4,2,2]) == 2, 'Example 1'
    assert Solution().findDuplicate([3,1,3,4,2]) == 3, 'Example 2'
    assert Solution().findDuplicate([1,1,3,4,2]) == 1, 'Example 3'
    print('all passed')

