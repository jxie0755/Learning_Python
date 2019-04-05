# P077 Combinations
# Medium


# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

import itertools

class Solution:
    def combine(self, n: int, k: int):
        sample = list(range(1, n+1))

        def helper(nums, k):
            if k == len(nums):
                return [nums]
            elif k == 1:
                return [[i] for i in nums]
            else:
                result = []
                next = nums[:]
                head = next.pop(0)
                result += helper(nums[1:], k)
                result += [[head] + com for com in helper(next, k-1)]

                return result

        return helper(sample, k)



if __name__ == '__main__':

    assert Solution().combine(1, 1) == [
        [1]
    ], "Edge 1"

    assert Solution().combine(4, 4) == [
        [1, 2, 3, 4]
    ], "Edge 2"

    assert sorted(Solution().combine(5, 3)) == [list(i) for i in itertools.combinations([1,2,3,4,5], 3)]

    print('all passed')



