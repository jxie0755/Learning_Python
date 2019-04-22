# P090 Subsets II
# Medium


# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.


class Solution:
    def subsetsWithDup(self, nums):
        pass


if __name__ == '__main__':
    assert sorted(Solution().subsetsWithDup([])) == [[]], 'Edge 0'
    assert sorted(Solution().subsetsWithDup([1])) == [[], [1]], 'Edge 1'

    assert sorted(Solution().subsetsWithDup([1, 2])) == [[], [1], [1, 2], [2]], 'Example 0'
    assert sorted(Solution().subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], 'Example 1'
    print('all passed')
