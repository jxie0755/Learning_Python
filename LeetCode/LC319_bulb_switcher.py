# P319 Bulb Switcher
# Medium


# There are n bulbs that are initially off.
# You first turn on all the bulbs.
# Then, you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it"s off or turning off if it"s on).
# For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb.

# Find how many bulbs are on after n rounds.

class Solution:

    # Version A, brutal force
    # just go with the instruction
    # failed by exceeding max time limit
    def bulbSwitch(self, n: int) -> int:
        if n <= 1:
            return n
        # first round
        bulbs = [0] + [1] * n
        # idx fix

        # start from second round to n round
        i = 2
        while i <= n:
            for k in range(i, n + 1, i):
                bulbs[k] = 0 if bulbs[k] == 1 else 1
            i += 1
        return sum(bulbs)


import math


class Solution(object):

    # STD ans, O(1)
    # The number of full squares
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


class Solution(object):

    # Version B, # O(logN)  observation
    # every 1 on follow n off:
    # [on 2 off ] [on 4 off ] [on 6 off ] [on 8 off ]....
    def bulbSwitch(self, n: int) -> int:
        jump = 2
        factor = 1
        count = 0
        while n > 0:
            count += 1
            n -= jump * factor + 1
            factor += 1

        return count


if __name__ == "__main__":
    assert Solution().bulbSwitch(0) == 0, "Edge 0"
    assert Solution().bulbSwitch(1) == 1, "Edge 1"
    assert Solution().bulbSwitch(2) == 1, "Edge 2"

    assert Solution().bulbSwitch(3) == 1, "Example 1"
    assert Solution().bulbSwitch(4) == 2, "Example 2"
    assert Solution().bulbSwitch(5) == 2, "Example 3"
    assert Solution().bulbSwitch(6) == 2, "Example 4"

    assert Solution().bulbSwitch(9999999) == 3162, "Long"

    print("All passed")
