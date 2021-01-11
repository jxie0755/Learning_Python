"""
https://leetcode.com/problems/trapping-rain-water/
P042 Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

from typing import *


class Solution_A:
    def trap(self, height: List[int]) -> int:
        """
        according to the peak and find the volume
        """

        peak_list = self.findPeaks(height)

        if len(peak_list) <= 1:  # If there is only 1 peak, then no water will be hold
            return 0

        else:  # If there is two or more than two peak,
            # we have to check if the later peaks are between the first two peak
            # or a peak outside of the two peak range

            start, end = min(peak_list[0], peak_list[1]), max(peak_list[0], peak_list[1])
            peak_list = peak_list[2:]
            volume = self.vol(height[start:end + 1])

            while peak_list:  # consume all the peaks by poping
                next_peak_idx = peak_list.pop(0)
                if next_peak_idx < start:
                    volume += self.vol(height[next_peak_idx:start + 1])
                    start = next_peak_idx
                elif next_peak_idx > end:
                    volume += self.vol(height[end:next_peak_idx + 1])
                    end = next_peak_idx
                else:  # this is when the peak is between the current two peaks, so no calculation is needed
                    pass

            return volume

    def vol(self, height: List[int]) -> int:
        """
        Helper Aa
        Calculate the volume between two peaks
        """

        sec_peak = min(height[0], height[-1])
        volume = 0
        for i in height:
            if i < sec_peak:
                volume += sec_peak - i
        return volume

    def findPeaks(self, height: List[int]) -> List[int]:
        """
        Helper Ab
        To find the index of peaks, and sort reversely accoridng to the height value at the index
        """

        hmp = {}
        temp = [0] + height + [0]
        rst = []
        for i in range(0, len(height)):
            prev, mid, aft = temp[i], temp[i + 1], temp[i + 2]
            if prev <= mid >= aft:
                hmp[i] = mid
                rst.append(i)

        lst = sorted(hmp, key=lambda k: hmp[k])[::-1]
        return lst


class Solution_B:

    VOLUME = 0  # Set a class attribute volume so that the helper can refer to

    def trap(self, height: List[int]) -> int:
        """
        This method no longer needs to generate a peak list, but to recursive check in-place
        First, find the max peak idx
        Then Sweep from the max peak idx bi-directional to head and to tail
            Sweep from max peak to head, finding the next highest peak, and calculate the volume between
            Sweep from max peak to end, finding the next highest peak, and calculate the volume between
            In both cases, use the next highest peak to be the new high point and recursively move
        """
        peak_idx = self.find_max_idx(height, 0, len(height))  # first locate the max peak idx
        self.trap_helper(height, 0, peak_idx, peak_idx)  # find everything before max_idx
        self.trap_helper(height, peak_idx + 1, len(height), peak_idx)  # find everything after max_idx
        ans = self.VOLUME
        self.VOLUME = 0  # reset the class attributes for next run
        return ans

    def find_max_idx(self, height: List[int], start: int, end: int) -> int:
        """
        Helper A: find out the max idx
        This function use start and end to specify the range to check
        """
        max_so_far = -1
        max_idx = -1
        for i in range(start, end):
            if height[i] > max_so_far:
                max_so_far = height[i]
                max_idx = i
        return max_idx

    def trap_helper(self, height: List[int], start: int, end: int, cur_max_idx) -> None:
        """
        Helper B: recursively calcualte the volume between two peaks, bidirectional search:
            if the new max idx < pre_max_i, means continously sweeping to head
            if the new max idx > pre_max_i, means continously sweeping to end
        This function use start and end to specify the range to check
        """
        if end - start >= 1:
            new_max_idx = self.find_max_idx(height, start, end)
            if new_max_idx < cur_max_idx:
                for i in range(new_max_idx, cur_max_idx):
                    self.VOLUME += (height[new_max_idx] - height[i])
                self.trap_helper(height, 0, new_max_idx, new_max_idx)  # sweeping to head
            else:
                for i in range(cur_max_idx + 1, new_max_idx):
                    self.VOLUME += (height[new_max_idx] - height[i])
                self.trap_helper(height, new_max_idx + 1, len(height), new_max_idx)  # sweeping to end


if __name__ == "__main__":
    testCase = Solution_B()
    assert testCase.trap([]) == 0, "Edge 1"
    assert testCase.trap([0]) == 0, "Edge 2"
    assert testCase.trap([1]) == 0, "Edge 3"
    assert testCase.trap([1, 1]) == 0, "Edge 4"
    assert testCase.trap([2, 2, 2]) == 0, "Edge 5"
    assert testCase.trap([2, 0, 2]) == 2, "Edge 6"

    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Example 1"
    assert testCase.trap([10, 1, 2, 1, 2, 1, 10]) == 43, "Example 2"
    assert testCase.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23, "Example 3"
    assert testCase.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Extra 1"
    assert testCase.trap([8, 5, 4, 1, 8, 9, 3, 0, 0]) == 14, "Extra 2"

    print("All passed")
