# P015 3Sum
# Medium


# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.


class Solution:
    def twoSum_for_3sum(self, numbers, target, jump):
        ### hastable method from P001
        result = []
        hashtable = {}
        for idx in range(0, len(numbers)):
            if idx == jump:
                pass  # jump over current check in 3sum, to avoid repeat use
            elif numbers[idx] not in hashtable.keys():
                hashtable[target-numbers[idx]] = idx
            else:
                result.append([numbers[hashtable[numbers[idx]]], numbers[idx]])
                # do not return, but get every possible group of target two sum
        return result

    def threeSum(self, nums):
        ### Use modified method of two_sum
        ### with every number, check the rest of array for two_sum of (0-number)
        ### O(N^2), max time limit exceeded
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while i != len(nums):
            current = nums[i]
            two_sum = self.twoSum_for_3sum(nums, 0 - current, i)
            if two_sum:
                for ts in two_sum:
                    ans = sorted([current] + ts)
                    if ans not in result:
                        result.append(ans)
            i += 1

        return result

class Solution:
    def threeSum(self, nums):
        ### Pure brutal force, O(N^3), max time limit exceeded
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)

        if length < 3:
            return []

        result = []
        i = 0
        while i != length - 2:
            first = nums[i]
            j = i+1
            while j != length - 1:
                second = nums[j]
                k = j+1
                while k != length:
                    third = nums[k]
                    if first + second + third == 0:
                        ans = sorted([first, second, third])
                        if ans not in result:
                            result.append(ans)
                    k += 1
                j += 1
            i += 1
        return result

class Solution:
    def threeSum_x(self, nums):
        ### Split the list to negative numbers and postive numbers
        ### handle [-i, 0, i] and [-i, -j, k] and [-i, j, k] individually
        ### Same O(N^2) max time limit exceeded
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        result = []
        nums = sorted(nums)
        if nums.count(0) >= 3:
            result.append([0,0,0])

        break_point, length = 0, len(nums)
        while break_point != length:
            if nums[break_point] >= 0:
                break
            break_point += 1

        neg = nums[:break_point]
        pos = nums[break_point:]

        def two_one(lst1, lst2):
            length = len(lst1)
            if length >= 2:
                i, j = 0, 1
                while i != length - 1:
                    first = lst1[i]
                    while j != length:
                        second = lst1[j]
                        last = 0 - first - second
                        if last in lst2:
                            ans = sorted([first, second, last])
                            if ans not in result:
                                result.append(ans)
                        j += 1
                    i += 1
                    j = i + 1

        two_one(neg, pos)
        two_one(pos, neg)

        return result

class Solution:
    def threeSum(self, nums):
        ### Since we only need to return numbers, it does not need to be indexed
        ### Break down the nums with a sort first, then move head and tail towards center
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, length = sorted(nums), len(nums)
        head, tail = 0, length - 1
        result = []

        if length < 3:
            return []

        while nums[head] <=0 and head != length - 1:
            first, last = nums[head], nums[tail]
            mid = 0 - first - last
            if mid in nums[head+1:tail]:
                ans = [first, mid, last]
                if ans not in result:
                    result.append(ans)

            if tail > head + 1:
                tail -= 1
            else:
                head += 1
                tail = length - 1

        return result



class Solution:
    def twoSum(self, numbers, target, jump):
        ### 提取p167 two sum II 中的头尾缩进法 O(N)

        result = []
        head, tail = 0, len(numbers) -1
        while head < tail:
            first, second = numbers[head], numbers[tail]
            if first + second > target or tail == jump:
                tail -= 1
            elif first + second < target or head == jump:
                head += 1
            else:
                result.append([first, second])
                tail -= 1

        return result


    def threeSum(self, nums):
        ### Use modified method of two_sum
        ### with every number, check the rest of array for two_sum of (0-number)
        ### O(N^2), max time limit exceeded
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        result = []
        i = 0

        while i != len(nums):
            current = nums[i]
            two_sum = self.twoSum(nums, 0 - current, i)
            if two_sum:
                for ts in two_sum:
                    ans = sorted([current] + ts)
                    if ans not in result:
                        result.append(ans)
            i += 1

        return result



if __name__ == '__main__':
    assert Solution().threeSum([]) == [], 'Edge 1'
    assert Solution().threeSum([1]) == [], 'Edge 2'
    assert Solution().threeSum([1,1]) == [], 'Edge 3'

    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]], 'Example 1'
    assert Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]) == [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]], 'Example 2'
    assert Solution().threeSum([-4,-2,-1]) == [], 'Example 3'
    assert Solution().threeSum([0,0,0]) == [[0,0,0]], 'Example 4'

    print('all passed')








