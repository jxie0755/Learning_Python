class Solution:
    def nextPermutation(self, nums):
        ### O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] < nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] > nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break
        return nums

lst = [1,2,4,5]
for i in range(7):
    lst = Solution().nextPermutation(lst)

print(lst)
