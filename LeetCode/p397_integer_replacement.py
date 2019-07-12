# P397 Integer Replacement
# Medium


# Given a positive integer n and you can do operations as follow:

# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.

# What is the minimum number of replacements needed for n to become 1?


class Solution:

    # Version A1, Dynammic programming
    # calculate each i until i == n
    # Exceed max time limit
    def integerReplacement(self, n: int) -> int:
        result = [0, 0, 1, 2]  # initialize from 0 - 3, idx as the current i, 0 as placeholder

        if n < 4:
            return result[n]

        i = 4
        while i <= n:
            if i % 2 == 0:
                result.append(result[i//2]+1)
            else:
                result.append(min(result[(i+1)//2], result[(i-1)//2]) + 2)
            i += 1

        return result[-1]


    # Version A2, same idea but pre-fill the result list and then fill all the value that is double-able
    def integerReplacement(self, n: int) -> int:


        result = [0, 0, 1, 2] + [None] * (n-3) # initialize from 0 - 3, idx as the current i, 0 as placeholder

        if n < 4:
            return result[n]

        i = 4
        while i <= n:
            if result[n]:  # This is important, when developing future index, it may hit n early
                return result[n]

            if not result[i]:
                if i % 2 == 0:
                    pre = result[i//2]
                    k = i
                    while k <= n:
                        pre += 1
                        result[k] = pre
                        k *= 2
                else:
                    result[i] = min(result[(i+1)//2] + 2, result[i-1] + 1)
                    pre = result[i]
                    k = 2 * i
                    while k <= n:
                        pre += 1
                        result[k] = pre
                        k *= 2
            i += 1

        return result[-1]



class Solution:

    # Version B1
    # Shrink the size of the problem first
    # This will pass, but slow
    def integerReplacement(self, n: int) -> int:
        if n <= 3:
            return n - 1
        elif n % 2 == 0:
            return self.integerReplacement(n//2) + 1
        else:
            return min(self.integerReplacement(n-1) + 1, self.integerReplacement((n+1)//2)+2)


    # Version B2, with memorization
    # This will pass much faster
    def integerReplacement(self, n: int) -> int:

        hmp = {1:0, 2:1, 3:2}

        def helper(n):
            if n in hmp:
                return hmp[n]
            else:
                if n % 2 == 0:
                    ans = helper(n//2) + 1
                else:
                    ans = min(helper(n-1) + 1, helper((n+1)//2)+2)
                hmp[n] = ans
                return ans

        result = helper(n)
        return result



if __name__ == "__main__":

    assert Solution().integerReplacement(1) == 0, "Edge 1"

    assert Solution().integerReplacement(8) == 3, "Example 1"
    assert Solution().integerReplacement(7) == 4, "Example 2"
    assert Solution().integerReplacement(13) == 5, "Example 3"

    assert Solution().integerReplacement(10000000) == 30, "Long 1"
    assert Solution().integerReplacement(100000000) == 31, "Long 2"

    print("all passed")
