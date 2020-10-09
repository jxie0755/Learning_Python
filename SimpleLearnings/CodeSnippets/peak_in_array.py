"""THis is a cope snippet for finding all the peaks in an array"""

from typing import *


def find_peak(height: List[int]) -> List[Tuple[int]]:
    """
    Return a list of the peaks, in tuples:
        first element to be idx
        second delement to be the value
    """

    if not height:
        return []

    peaks = []
    trend = "flat"
    i = 0
    while i < len(height) - 1:
        cur = height[i]
        next = height[i + 1]
        if cur > next:
            if trend == "flat":
                peaks.append((i, cur))
                trend = "down"
            elif trend == "down":
                pass
            elif trend == "up":
                peaks.append((i, cur))
                trend = "down"
        elif cur < next:
            if trend == "flat":
                trend = "up"
            elif trend == "down":
                trend = "up"
            elif trend == "up":
                pass
        else:
            if trend == "flat":
                pass
            elif trend == "down":
                trend = "flat"
            elif trend == "up":
                peaks.append((i, cur))
                trend = "flat"
        i += 1

    if height[i] > height[i - 1]:  # check the end too!
        peaks.append((i, height[i]))

    return peaks


if __name__ == '__main__':
    assert find_peak([]) == [], "Empty"
    assert find_peak([1]) == [], "Single"

    assert find_peak([1, 2]) == [(1, 2)], "two up"
    assert find_peak([1, 2, 3]) == [(2, 3)], "three up"
    assert find_peak([2, 1]) == [(0, 2)], "two down"
    assert find_peak([3, 2, 1]) == [(0, 3)], "three down"

    assert find_peak([2, 2]) == [], "two flat"
    assert find_peak([2, 2, 2]) == [], "all flat"
    assert find_peak([2, 1, 2]) == [(0, 2), (2, 2)], "U shape"
    assert find_peak([2, 2, 1, 2]) == [(1, 2), (3, 2)], "U shape with flat"
    assert find_peak([2, 2, 1, 2, 2, 2, 2, 2, 2, ]) == [(1, 2), (3, 2)], "U shape with lots flat"

    assert find_peak([1, 2, 3, 2, 1]) == [(2, 3)], "Huge peak"
    assert find_peak([3, 2, 1, 3, 2, 1]) == [(0, 3), (3, 3)], "Two step down"
    assert find_peak([3, 1, 3, 1, 3, 1, 3]) == [(0, 3), (2, 3), (4, 3), (6, 3)], "Zig Zag"

    print("all passed")
