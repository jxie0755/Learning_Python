# P287 Find the Duplicate Number
# Medium


# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

from typing import *


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        maxx, minn = max(nums), min(nums)
        N = len(nums)
        rest_n = N - 2
        rest_sum = sum(nums) - maxx - minn

        # 保证max和min都没有在重复
        if nums.count(minn) > 1:
            return minn
        if nums.count(maxx) > 1:
            return maxx

        print("total length", N, "rest length", N - 2, "rest sum", rest_sum)
        print("min", minn, "max", maxx)
        mid = (maxx + minn) // 2
        while True:
            print("mid", mid, mid * rest_n, rest_sum)
            mid_sum = mid * rest_n
            if mid_sum < rest_sum:
                diff = rest_sum - mid_sum
                if diff > rest_n:
                    mid += diff // rest_n
                else:
                    for i in range(mid - diff, mid + diff + 1):
                        if nums.count(i) > 1:
                            return i

            elif mid_sum > rest_sum:
                diff = mid_sum - rest_sum
                if diff > rest_n:
                    mid -= diff // rest_n
                else:
                    for i in range(mid - diff, mid + diff + 1):
                        if nums.count(i) > 1:
                            return i
            else:
                return mid


class Solution(object):

    # STD ans 循环链表判断法
    # Time:  O(n)
    # Space: O(1)
    # 精妙!
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.

        # 假设list中的值v指向的就是list[v]
        # 出现重复值也就是意味着重复值会指回到同一个index上, 这就变成了一个死循环
        slow = nums[0]
        fast = nums[nums[0]]

        # 第一个循环, slow走一步,fast走两步
        # 假设循环之前有A步, 循环内有C步
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 当slow走了A步刚进入循环, fast走了2A步, 也就是在循环内走了A步
        # 此时slow和fast的位置关系是slow在分叉口,fast多走了A%C步, 可以认为A = k*C + A%C
        # 因为是个循环, 所以也同时是fast在slow后方C-A%C步
        # 继续向前走, fast追赶slow, 每次追赶一步, 所以slow再走C-A%C步被fast追上, 此时while loop结束
        # 此时slow刚好离分叉口A%C步

        # 第二个循环, slow继续走,每次走一步,fast从头开始, 每次走一步(速度相同)
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # 此时fast需要走A步到分叉口, 而slow离分叉口A%C步,
        # slow走回分叉口时走了A%C步, fast也走了A%C步, fast距离分叉口k*C + A%C - A%C = k*C步, 正好相差k个完整C循环
        # 所以fast和slow必将在分叉口相遇
        return slow


# print(Solution().findDuplicate([1, 8, 8, 2, 3, 4, 5, 6, 7, 9]))
# print(Solution().findDuplicate([1, 2, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(Solution().findDuplicate([18, 13, 14, 17, 9, 19, 7, 17, 4, 6, 17, 5, 11, 10, 2, 15, 8, 12, 16, 17]))
#                               0   1   2   3   4  5   6  7   8  9  10  11 12  13  14 15  16 17  18  19


class Solution(object):
    # STD ans Binary search method.
    # Time:  O(n*logn)
    # Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        # 利用中位数判断:
        # 如果1-n不出现重复, 那么数列中<=x的数的个数一定等于x, 大于x的数字的个数也等于x
        # 一旦出现重复, 那么这个就被打破了, 出现重复的数字必定在多于x的那一侧, 通过二分搜索推进区间
        while left <= right:
            mid = (left + right) // 2

            # Get count of num <= mid.
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
            print("count", count)
        return left


class Solution(object):

    # STD ans
    # Time:  O(n)
    # Space: O(1)
    def findDuplicate(self, nums: List[int]) -> int:

        # 遍历list,把值变成相反数,乘以-1, 然后专跳到下一个index
        # 由于出现重复,必定会在重复数跳回到之前的index, 这样就会跳到一个值为负数的情况
        i = 0
        while nums[i] > 0:
            next_i = nums[i]
            nums[i] = -1 * nums[i]
            i = next_i

        # 一旦nums[i]为负值, 也就是说明跳回去了, 这时终止loop, i正好停留在重复值
        duplicate = i

        # 再把list给改回去
        for k in range(len(nums)):
            nums[k] = abs(nums[k])

        return duplicate
        # 这招不完全符合题目要求, 它还是改了list, 但是最后又给改回去了, 可以参考


if __name__ == "__main__":
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2, "Example 1"
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3, "Example 2"
    assert Solution().findDuplicate([1, 1, 3, 4, 2]) == 1, "Example 3"
    assert Solution().findDuplicate([4, 4, 3, 2, 1]) == 4, "Example 4"
    assert Solution().findDuplicate([3, 4, 1, 2, 4]) == 4, "Example 5"

    assert Solution().findDuplicate([1, 1, 1, 1, 1]) == 1, "Example 6"
    assert Solution().findDuplicate([4, 4, 4, 4, 4]) == 4, "Example 7"

    assert Solution().findDuplicate([3, 3, 2, 3, 3]) == 3, "Example 8"
    assert Solution().findDuplicate([3, 2, 3, 4, 3]) == 3, "Example 9"
    assert Solution().findDuplicate([2, 1, 1, 1, 1]) == 1, "Example 10"

    assert Solution().findDuplicate([7, 9, 7, 4, 2, 8, 7, 7, 1, 5]) == 7, "Additional 1"
    assert Solution().findDuplicate([1, 8, 8, 2, 3, 4, 5, 6, 7, 9]) == 8, "Additional 2"
    assert Solution().findDuplicate([1, 2, 2, 3, 4, 5, 6, 7, 8, 9]) == 2, "Additional 3"
    assert Solution().findDuplicate([1, 2, 3, 4, 5, 6, 6, 6, 6, 9]) == 6, "Additional 4"

    assert Solution().findDuplicate(
        [18, 13, 14, 17, 9, 19, 7, 17, 4, 6, 17, 5, 11, 10, 2, 15, 8, 12, 16, 17]) == 17, "Additional 5"

    print("All passed")
