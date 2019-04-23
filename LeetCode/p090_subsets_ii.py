# P090 Subsets II
# Medium


# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.


class Solution:
    def comniantion(self, nums, k):
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in nums]
        elif len(nums) == k:
            return [nums]
        else:
            result = []
            subnums = nums[:]
            head = subnums.pop(0)
            result += [[head] + com for com in self.comniantion(subnums, k-1)]
            result += [self.comniantion(nums[1:], k)]
            return result


    def subsetsWithDup(self, nums):

        def helper(comb):
            result = []
            if not nums_hmp:
                return [comb]

            for i in nums_hmp:
                if i in comb:
                    for n in range(nums_hmp[i]):
                        result.append(comb[:] + [i]*n)
                else:
                    return [comb]
            return result

        if not nums:
            return [nums]

        nums_set = list(set(nums))
        nums_hmp = {i:nums.count(i) for i in nums_set if nums.count(i) > 1}

        no_repeat_result = []
        for k in range(len(nums_set)+1):
            no_repeat_result += self.comniantion(nums_set,k)

        result = []
        for i in no_repeat_result:
            result += helper(i)

        return result

print(Solution().subsetsWithDup([1,2,3]))

# if __name__ == '__main__':
#     assert sorted(Solution().subsetsWithDup([])) == [[]], 'Edge 0'
#     assert sorted(Solution().subsetsWithDup([1])) == [[], [1]], 'Edge 1'
#
#     assert sorted(Solution().subsetsWithDup([1, 2])) == [[], [1], [1, 2], [2]], 'Example 0'
#     assert sorted(Solution().subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 'Example 1'
#     assert sorted(Solution().subsetsWithDup([1,2,3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], "Additional 1"
#
#     print('all passed')
