from typing import *

class Solution_C2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Add a recursive process method to update result
        """

        def process(candidates: List[int], start: int, intermediate: List[int], target: int) -> None:
            """
            Helper
            """

            if target == 0:
                result.append(list(intermediate))  # 终止case, target降到0就完成
                # 这里使用list其实就是复制一个itermediate, 可以用interme[:]取代

            while start < len(candidates) and candidates[start] <= target:  # while loop 走完全部candidates
                intermediate.append(candidates[start])
                process(candidates, start, intermediate, target - candidates[start])
                intermediate.pop()  # 这里退回相当于,即使满足条件, 也可以跳过
                start += 1

        candidates = sorted(candidates)
        result = []
        intermediate = []
        start = 0

        while start < len(candidates) and candidates[start] <= target:  # while loop 走完全部candidates
            intermediate.append(candidates[start])
            process(candidates, start, intermediate, target - candidates[start])
            intermediate.pop()  # 这里退回相当于,即使满足条件, 也可以跳过
            start += 1


        return result





if __name__ == "__main__":
    testCase = Solution_C2()

    # Test cases are check after sorting, to avoid sequence error
    assert sorted(testCase.combinationSum([], 1)) == [], "Edge 1"
    assert sorted(testCase.combinationSum([1], 1)) == [[1]], "Edge 2"
    assert sorted(testCase.combinationSum([1], 2)) == [[1, 1]], "Edge 3"
    assert sorted(testCase.combinationSum([2], 1)) == [], "Edge 4"
    assert sorted(testCase.combinationSum([2], 5)) == [], "Edge 5"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 3, 6, 7], 7)]) == [
        [2, 2, 3],
        [7]
    ], "Example 1"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 3, 5], 8)]) == [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ], "Example 2"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([2, 4], 10)]) == [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 4],
        [2, 4, 4]
    ], "Extra 1"

    assert sorted([sorted(comb) for comb in testCase.combinationSum([7, 3, 2], 18)]) == [
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 3, 3],
        [2, 2, 2, 2, 3, 7],
        [2, 2, 2, 3, 3, 3, 3],
        [2, 2, 7, 7],
        [2, 3, 3, 3, 7],
        [3, 3, 3, 3, 3, 3]
    ], "Extra 2"

    print("all passed")
