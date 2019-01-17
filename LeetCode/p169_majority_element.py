# P169 Majority Element
# Easy


# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.


# You may assume that the array is non-empty and the majority element always exist in the array.




class Solution:
    def majorityElement(self, nums):
        ### Hash table?
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = {}
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1

        return max(hashtable, key=hashtable.get)



if __name__ == '__main__':
    assert Solution().majorityElement([1]) == 1, 'Edge 1'
    assert Solution().majorityElement([3,2,3]) == 3, 'Example 1'
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2, 'Example 2'

    print('all passed')




