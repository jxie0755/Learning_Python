# P077 Combinations
# Medium


# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

import itertools

class Solution:
    def combine(self, n: int, k: int):
        sample = list(range(1, n+1))

        # this can individually work as a combination of list of elements
        def helper(nums, k):
            if k == len(nums):
                return [nums]
            elif k == 1:
                return [[i] for i in nums]
            else:
                result = []
                next_list = nums[:]
                head = next_list.pop(0)
                result += [[head] + com for com in helper(next_list, k-1)] + helper(nums[1:], k)
                return result

        return helper(sample, k)


# Extracted from the combineationSolo to straight application
def combinationSolo(nums, k):
    if k == len(nums):
        return [nums]
    elif k == 1:
        return [[i] for i in nums]
    else:
        result = []
        next_list = nums[:]
        head = next_list.pop(0)
        result += [[head] + com for com in combinationSolo(next_list, k - 1)] + combinationSolo(nums[1:], k)
        return result



if __name__ == '__main__':

    print('Test solo')
    for i in combinationSolo([1, 2, 3, 4], 2):
        print(i)

    print('End of test solo')

    assert Solution().combine(1, 1) == [
        [1]
    ], "Edge 1"

    assert Solution().combine(4, 4) == [
        [1, 2, 3, 4]
    ], "Edge 2"

    assert Solution().combine(5, 3) == [list(i) for i in itertools.combinations([1,2,3,4,5], 3)]

    for i in Solution().combine(4, 2):
        print(i)



    print('all passed')
