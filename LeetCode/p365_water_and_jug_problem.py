# Water and Jug Problem
# Medium


# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

# Operations allowed:
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


class Solution_A1:

    # Version A1
    # Start from 0, 0 and record all possible status of the two bottle
    # The recursive funtion will reach to maximum depth in big case
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        all_possible = {(0,0)}
        found = False

        def helper(A, B):
            nonlocal found

            # A_to_B
            available_B = y - B
            if A >= available_B:
                A_to_B = (A - available_B, y)
            else:
                A_to_B = (0, B + A)

            # B_to_A
            available_A = x - A
            if B >= available_A:
                B_to_A = (x, B - available_A)
            else:
                B_to_A = (A + B, 0)

            candidates = [(0, B), (A, 0), (x, B), (A, y), A_to_B, B_to_A]
                         # drainA drainB  fillA   fillB

            for status in candidates:
                if z in status:
                    found = True
                if 0 <= A <= x and 0 <= B <= y and status not in all_possible:
                    all_possible.add(status)
                    helper(status[0], status[1])

        helper(0, 0)
        return found


# class Solution:
#
#     # Version A2
#     # math:
#     # if big and small has no gcd (==1), then only 0, gcd, gcd*2, gcd*3....big+small
#     # if big and small has gcd (==1), then only 0, gcd, gcd*2, gcd*3....big+small
#     def gcd(self, a, b):
#         while b:
#             a, b = b, a % b
#         return a
#
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         if x == 0 or y == 0:
#             return z == 0 or z == x or z == y
#         g = self.gcd(x, y)
#         return z <= x + y and z % g == 0


if __name__ == "__main__":
    testCase = Solution_A1()
    assert testCase.canMeasureWater(0, 0, 0), "Edge 0"
    assert not testCase.canMeasureWater(0, 2, 1), "Edge 1"
    assert not testCase.canMeasureWater(1, 2, 3), "Edge 2"

    assert testCase.canMeasureWater(3, 5, 4), "Example 1, Di Hard"
    assert not testCase.canMeasureWater(2, 6, 5), "Example 2"
    assert not testCase.canMeasureWater(6, 9, 1), "Example3"

    assert testCase.canMeasureWater(22003, 31237, 1), "Long"

    print("all passed")
