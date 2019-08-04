# https://leetcode.com/problems/trapping-rain-water/
# P042 Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

from typing import *


class Solution:

    # Version A
    # according to the peak and find the volume
    def trap(self, height: List[int]) -> int:

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

    def vol(self, height):
        """Calculate the volume between two peaks"""
        sec_peak = min(height[0], height[-1])
        volume = 0
        for i in height:
            if i < sec_peak:
                volume += sec_peak - i
        return volume

    def findPeaks(self, height):
        """To find the index of peaks, and sort reversely accoridng to the height value at the index"""
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


if __name__ == "__main__":
    # assert Solution().trap([]) == 0, "Edge 1"
    # assert Solution().trap([0]) == 0, "Edge 2"
    # assert Solution().trap([1]) == 0, "Edge 3"
    # assert Solution().trap([1, 1]) == 0, "Edge 4"
    # assert Solution().trap([2, 2, 2]) == 0, "Edge 5"
    # assert Solution().trap([2, 0, 2]) == 2, "Edge 6"
    #
    # assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Example 1"
    # assert Solution().trap([10, 1, 2, 1, 2, 1, 10]) == 43, "Example 2"
    # assert Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]) == 23, "Example 3"

    print(Solution().findPeaks([10, 1, 2, 1, 2, 1, 10]))



    print("all passed")
