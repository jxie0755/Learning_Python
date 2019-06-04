# P090 Subsets II
# Medium


# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.


class Solution:
    def combination(self, nums, k):
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
            result += [[head] + com for com in self.combination(subnums, k - 1)]
            result += self.combination(nums[1:], k)
            return result

    def subsetsWithDup(self, nums):

        def helper(comb):
            # this is actually the tricky part
            """
            according to a dictionary suggesting the maximum occurance of an element
            it is like a cross multiply:
            [[x, y] for x in range(i) for y in range(j)]
            """
            result = [[]]
            for d in nums_hmp:
                if d in comb:
                    # Updating the list by list concatenation of adding the every sub-list in result with newest
                    result = [x + y for x in result for y in [[d] * n for n in range(1, nums_hmp[d]+1)]]

            return result

        nums_set = list(set(nums))
        nums_hmp = {i: nums.count(i) for i in nums_set}

        result = []
        for k in range(len(nums_set)+1):
            for i in self.combination(nums_set,k):
                result += helper(i)

        return result



if __name__ == '__main__':
    assert sorted(Solution().subsetsWithDup([])) == [[]], 'Edge 0'
    assert sorted(Solution().subsetsWithDup([1])) == [[], [1]], 'Edge 1'

    assert sorted(Solution().subsetsWithDup([1, 2])) == [[], [1], [1, 2], [2]], 'Example 0'
    assert sorted(Solution().subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 'Example 1'

    assert sorted(Solution().subsetsWithDup([1,2,3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], 'Additional 1'
    assert sorted(Solution().subsetsWithDup([1,1,2,2])) == [[], [1], [1, 1], [1, 1, 2], [1, 1, 2, 2], [1, 2], [1, 2, 2], [2], [2, 2]], 'Additional 2'

    print('all passed')


