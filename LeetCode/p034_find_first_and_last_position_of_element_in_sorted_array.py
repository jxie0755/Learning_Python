# P033 Find First and Last Positions of Element in Sorted Array
# Medium


# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1]


class Solution:
    # 3 binary search, find catch mid value, and Low/High of the section,
    # Then according to mid value and Low/High to find head and tail by 2 additional binary search
    # O(LogN)
    # Space O(1)

    def searchRange(self, nums, target):

        if not nums:  # 处理空list
            return [-1, -1]
        if len(nums) == 1: # 处理单元素list
            return [0,0] if nums[0] == target else [-1,-1]


        L, H = 0, len(nums) -1
        M = (L+H) // 2 + 1

        while nums[M] != target:
            if H-L <= 1 and nums[H] == target:
                return [H, H]
            elif H-L <= 1 and nums[L] != target and nums[H] != target:   # if cannot find M, target not in list
                return [-1,-1]
            if target < nums[M]:
                H = M
            elif target > nums[M]:
                L = M

            M = (L+H) // 2

        # Locate head
        head = L
        while True:
            head_value = nums[head]
            if head_value == target and head == L:
                break
            elif head_value < target:
                L = head
                head = (L + M+1) // 2
            elif head_value == target and nums[head-1] == target:
                head = (head + L+1) // 2
            else:
                break

        # locate tail
        tail = H
        while True:
            tail_value = nums[tail]
            if tail_value == target and tail == H:
                break
            elif tail_value > target:
                H = tail
                tail = (H + M) // 2
            elif nums[tail] == target and nums[tail+1] == target:
                tail = (tail + H) // 2
            else:
                break

        return [head, tail]



class Solution:
    # improved binary search
    # 3 binary search, find catch mid value, and Low/High of the section,
    # Then according to mid value and Low/High to find head and tail by 2 additional binary search
    # O(LogN)
    # Space O(1)

    def searchRange(self, nums, target):
        if not nums:  # 处理空list
            return [-1, -1]
        if len(nums) == 1: # 处理单元素list
            return [0,0] if nums[0] == target else [-1,-1]


        L, H = 0, len(nums) -1
        M = (L+H) // 2
        while L <= H:
            check = nums[M]
            if check < target:
                L = M + 1
            elif check > target:
                H = M - 1
            else:
                break
            M = (L+H) // 2

        if L > M:  # can't find M match target
            return [-1, -1]

        # Locate head
        Lo, Hi = L, M
        while True:
            head = (Lo + Hi) // 2
            head_value = nums[head]
            if head_value == target and head == 0:
                break
            elif head_value < target:
                Lo = head + 1
            elif head_value == target and nums[head-1] == target:
                Hi = head - 1
            else:
                break

        # locate tail
        Lo, Hi = M, H
        while True:
            tail = (Lo + Hi) // 2
            tail_value = nums[tail]
            if tail_value == target and tail == Hi:
                break
            elif tail_value > target:
                Hi = tail - 1
            elif nums[tail] == target and nums[tail+1] == target:
                Lo = tail + 1
            else:
                break

        return [head, tail]


if __name__ == '__main__':
    assert Solution().searchRange([], 8) == [-1, -1], 'Edge 1'
    assert Solution().searchRange([8], 8) == [0, 0], 'Edge 2'
    assert Solution().searchRange([0], 8) == [-1, -1], 'Edge 3'

    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4], 'Example 1'
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1], 'Example 2'

    assert Solution().searchRange([5,7,7,7,8,10], 8) == [4,4], 'Addtional 1'
    assert Solution().searchRange([5,7,7,7,8,10], 7) == [1,3], 'Addtional 2'

    assert Solution().searchRange([1,4], 4) == [1,1], 'Extra 1'
    assert Solution().searchRange([1,3], 1) == [0,0], 'Extra 2'
    assert Solution().searchRange([-3,-2, -1], 0) == [-1,-1], 'Extra 3'
    assert Solution().searchRange([0,0,2,3,4,4,4,5], 5) == [7,7], 'Extra 4'
    assert Solution().searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4) == [10, 13], 'Extra 5'
    assert Solution().searchRange([1,2,3,3,3,3,4,5,9], 3) == [2, 5], 'Extra 6'

    print('all passed')
