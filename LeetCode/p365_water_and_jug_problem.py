# Water and Jug Problem
# Medium


# You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

# If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

# Operations allowed:
# Fill any of the jugs completely with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


class Solution:

    # Version A1
    # Start from 0, 0 and record all possible status of the two bottle
    # The recursive funtion will reach to maximum depth in big case
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        all_possible = {}
        big, small = max(x, y), min(x, y)

        def helper(A, B):
            """
            calculate the status of two water jar
            A is the water in small jar
            B is the water in big jar
            """
            if 0 <= A <= small and 0 <= B <= big and (A, B) not in all_possible:
                all_possible[(A, B)] = 1

                helper(small, B)  # fill up small
                helper(A, big)  # fill up big
                helper(0, B)  # drain small
                helper(A, 0)  # drain big

                # poor from big to small
                if (small - A) >= B:
                    helper(A + B, 0)
                else:
                    helper(small, B - (small - A))

                # poor from small to big
                if (big - B) >= A:
                    helper(0, A + B)
                else:
                    helper(A - (big - B), big)

        helper(0, 0)
        lst = []
        for i in all_possible:
            for j in i:
                lst.append(j)

        # print(sorted(list(set(lst))))

        for key in all_possible:
            if z in key:
                return True
        return False


class Solution:

    # Version A2
    # math:
    # if big and small has no gcd (==1), then only 0, gcd, gcd*2, gcd*3....big+small
    # if big and small has gcd (==1), then only 0, gcd, gcd*2, gcd*3....big+small
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x == 0 or y == 0:
            return z == 0 or z == x or z == y
        g = self.gcd(x, y)
        return z <= x + y and z % g == 0


if __name__ == "__main__":
    assert Solution().canMeasureWater(0, 0, 0), "Edge 0"
    assert not Solution().canMeasureWater(0, 2, 1), "Edge 1"
    assert Solution().canMeasureWater(1, 2, 3), "Edge 2"

    assert Solution().canMeasureWater(3, 5, 4), "Example 1, Di Hard"
    assert not Solution().canMeasureWater(2, 6, 5), "Example 2"
    assert not Solution().canMeasureWater(6, 9, 1), "Example3"

    assert Solution().canMeasureWater(22003, 31237, 1), "Long"

    print("all passed")
