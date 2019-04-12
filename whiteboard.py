import math

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


    def prevPermutation(self, nums):
        ### O(N), directly find next different permutations
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cur_i = None

        for i in range(-2, -length - 1, -1):
            if nums[i] > nums[i + 1]:
                cur_i = i
                break

        if not cur_i:
            nums[:] = nums[::-1]  # 直接结束,因为本身是倒着排序的,返回正排序即可
        else:
            for rev_i in range(-1, cur_i, -1):
                if nums[rev_i] < nums[cur_i]:
                    nums[cur_i], nums[rev_i] = nums[rev_i], nums[cur_i]  # switch
                    nums[cur_i + 1:] = nums[cur_i + 1:][::-1]
                    break
        return nums


p_dict = {
        i: math.factorial(i) for i in range(1,10)
    }

print(p_dict)

n = 5
i = 3
lst = list(range(1, n - i + 1)) + list(range(n-i+1, n + 1))[::-1]
print(lst)

L = [1,2,3,4]
for i in range(6-1):
   L = Solution().nextPermutation(L)
print(L)

L2 = [1,4,3,2]
for i in range(5):
   L2 = Solution().nextPermutation(L2)
print(L2)

print("!!!!!!!!!!!!!!!")
LP = [4,3,2,1]
for i in range(23):
    LP = Solution().prevPermutation(LP)
    print(LP)
