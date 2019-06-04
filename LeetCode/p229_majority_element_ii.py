# P229 Majority Element II
# Medium

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space. - Not True (STD ans will use hashmap as well)


class Solution(object):

    # Version A1, use hashmap to record everything
    # It was not O(1) space
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        N = len(nums) // 3
        hmp = {}
        for i in nums:
            if i not in hmp:
                hmp[i] = 1
            else:
                hmp[i] += 1

        for i in hmp:
            if hmp[i] > N:
                result.append(i)

        return result


class Solution(object):

    # Version A2
    # There could be maximumly only two element to count more than 1/3
    # So, it shoud stop after two are found, no need to proceed
    # It was stil not O(1) space


    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        N = len(nums) // 3
        hmp = {}
        for i in nums:
            if i not in hmp:
                hmp[i] = 1
            else:
                hmp[i] += 1

            if hmp[i] > N and i not in result:
                result.append(i)
            if len(result) == 2:
                break

        return result

import collections
class Solution(object):
    # STD ans
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [i[0] for i in collections.Counter(nums).items() if i[1] > len(nums) / 3]


if __name__ == '__main__':
    assert Solution().majorityElement([]) == [], 'Edge'
    assert Solution().majorityElement([3,2,3]) == [3], 'Example 1'
    assert Solution().majorityElement([1,1,1,1,3,2,2,2,2]) == [1,2], 'Example 2'

    assert Solution().majorityElement([1,3,1,3,1,3,1,3,2]) == [1,3], 'Additional 1'


    print('all passed')
