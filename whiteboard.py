# P075 Sort Colors
# Medium
# https://leetcode.com/problems/sort-colors/


# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0"s, 1"s, and 2"s, then overwrite array with total number of 0"s, then 1"s and followed by 2"s.
# Could you come up with a one-pass algorithm using only constant space?


class Solution:
    def sortColors(self, nums) -> None:
        if not nums:
            return None
        i = 0
        k = len(nums) - 1
        while i != k:
            if nums[i] == 0:
                i += 1
            elif nums[i] == 1:
                j = i # 从i出发找下一个0所在的位置来交换
                while j <= k:
                    if nums[j] == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
                i += 1
            elif nums[i] == 2:
                while k != i: # 从k倒退,把2换到最后,不要管换到前面去的是0还是1
                              # 只要不变更i继续走前两个条件
                    if nums[k] != 2:
                        nums[i], nums[k] = nums[k], nums[i]
                        break
                    k -= 1


if __name__ == "__main__":
    testCase = Solution()

    e1 = []
    testCase.sortColors(e1)
    assert e1 == [], "Edge 1"

    e2 = [0, 0]
    testCase.sortColors(e2)
    assert e2 == [0, 0], "Edge 2"

    s1 = [2, 0, 2, 1, 1, 0]
    testCase.sortColors(s1)
    assert s1 == [0, 0, 1, 1, 2, 2], "Example 1"

    s2 = [0, 2, 1, 2, 0, 1, 2, 1]
    testCase.sortColors(s2)
    assert s2 == [0, 0, 1, 1, 1, 2, 2, 2], "Additional 1"

    s3 = [1, 0]
    testCase.sortColors(s3)
    assert s3 == [0, 1], "Additional 2"

    print("all passed")
