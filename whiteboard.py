from typing import *

class Solution_A:
    def search(self, nums: List[int], target: int) -> int:
        """
        Recursion method, complicated binary search O(logN)
        Unecessary at all, method abandoned
        """
        L, H = 0, len(nums) - 1

        # 避免nums为空
        if not nums:
            return -1
        else:
            return self.search_helper(nums, L, H, target)

    def search_helper(self, nums, L: int, H: int, target:int) -> int:
        """Helper"""

        M = (L + H) // 2
        low, mid, high = nums[L], nums[M], nums[H]
        print("L", L, "M", M, "H", H)


        # 如果缩到最后,长度只有2了,还是没有发现target只能return -1
        if mid == target:
            return M
        elif L > H:
            return -1
        else:
            # 把list从中间切开,其中一半必为排序,另一半不确定是否排序
            # 如果target在排序的那一段其中,那么就接着二分法
            if low <= target < mid:
                return self.search_helper(nums, L, M-1, target)
            elif mid < target <= high:
                return self.search_helper(nums, M+1, H, target)


            # 如果没有出现以上情况,那target必在没有排序的一段中 (而且只可能有一段不是排序的)
            # 而且就算不是排序的, 二分法同样可以继续
            elif low > mid:
                return self.search_helper(nums, L, M-1, target)
            elif mid > high:
                return self.search_helper(nums, M+1, H, target)
            else:
                return -1



if __name__ == "__main__":
    testCase = Solution_A()
    # assert testCase.search([], 1) == -1, "Edge 1"
    # assert testCase.search([1], 1) == 0, "Edge 2"
    # assert testCase.search([0], 1) == -1, "Edge 3"
    #
    # assert testCase.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Example 1"
    # assert testCase.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Example 2"
    #
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 3) == 0, "Additional 1"
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 4) == 1, "Additional 2"
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 8) == 5, "Additional 3"
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 10) == 7, "Additional 4"
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 1) == 8, "Additional 5"
    # assert testCase.search([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 2) == 9, "Additional 6"
    #
    # assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 8) == 0, "Additional 7"
    # assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 1) == 3, "Additional 8"
    # assert testCase.search([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 6) == 8, "Additional 9"
    assert testCase.search([6, 6, 6, 6, 6, 6, 6, 6, 8, 6], 8) == 8, "Additional 10"

    # assert testCase.search([1, 3], 2) == -1, "Extra"
    #
    # print("all passed")
