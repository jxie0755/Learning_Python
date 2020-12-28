"""
https://leetcode.com/problems/search-a-2d-matrix/
P075 Sort Colors
Medium


Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0"s, 1"s, and 2"s, then overwrite array with total number of 0"s, then 1"s and followed by 2"s.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution_A:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        This uses pop which would change the length of array in process
        Move 0 to head and Move 2 to tail
        """
        i = 0
        L = len(nums)
        while i != L:
            if nums[i] == 0 and i != 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
            elif nums[i] == 2 and i != L - 1 and nums[i:] != [2] * (L - i):
                nums.pop(i)
                nums.append(2)
            else:
                i += 1

class Solution_B:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead
        This change by swapping, no need to change array length
        This tracks head and tail and keep moving 0 to head and 2 to tail
        """
        i = 0
        L = len(nums)
        head, tail = 0, L - 1 # label head and tail for moving 0 and 2 to

        while i != L:
            if nums[i] == 0 and i > head:
                nums[head], nums[i] = nums[i], nums[head]
                head += 1
            elif nums[i] == 2 and i < tail:
                nums[tail], nums[i] = nums[i], nums[tail]
                tail -= 1
            else:
                i += 1


if __name__ == "__main__":
    testCase = Solution_B()

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
