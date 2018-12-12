# p66 Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """




if __name__ == '__main__':
    assert Solution().plusOne([0]) == [1]
    assert Solution().plusOne([1,2,3]) == [1,2,4]
    assert Solution().plusOne([4,3,2,1]) == [4,3,2,2]
    assert Solution().plusOne([1,9,9]) == [2,0,0]
    assert Solution().plusOne([9,9,9]) == [1,0,0,0]
    print('all passed')