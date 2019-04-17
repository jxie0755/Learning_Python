# P078 Subsets
# Medium


# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.



class Solution:
    def combinationSolo(self, nums, k):
        if k == 0:
            return [[]]
        if k == len(nums):
            return [nums]
        elif k == 1:
            return [[i] for i in nums]
        else:
            result = []
            next_list = nums[:]
            head = next_list.pop(0)
            result += [[head] + com for com in self.combinationSolo(next_list, k - 1)] + self.combinationSolo(nums[1:], k)
            return result


    ### passed but on the slow side
    def subsets(self, nums):
        result = []
        for i in range(0, len(nums)+1):
            result += self.combinationSolo(nums, i)
        return result



if __name__ == '__main__':
    nums = [1, 2, 3]
    assert sorted(Solution().subsets(nums)) == sorted([
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        []
    ])
    print('all passed')
