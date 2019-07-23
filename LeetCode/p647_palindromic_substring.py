# p647 Palindromic Substrings
# Medium

# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings
# even they consist of same characters.
# Note:
# The input string length won't exceed 1000.

# """
# :type s: str
# :rtype: int
# """

class Solution:
    def countSubstrings(self, s):
        # not very fast?
        # create a generator for all substrings, to save memory
        def substrings(x):
            for i in range(len(x)):
                for e in range(1, len(x) - i + 1):
                    yield x[i:i + e]

        count = 0
        for i in substrings(s):
            if i == i[::-1]:
                count += 1
        return count

    def countSubstrings(self, s):
        # without generator, even slower

        count = 0
        for i in range(len(s)):
            for e in range(1, len(s) - i + 1):
                if s[i:i + e] == s[i:i + e][::-1]:
                    count += 1
        return count

    def countSubstrings(self, s):
        # https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)

        N = len(s)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
        # This method evaluate each substrings from the center
        # if len = 1, obviously palindrome
        # if len > 1, check by expanding from the center to two side (with limitation to prevent out of index)
        # if left == right, then still palindrome, if left != right, then no more palindrome with this center, so move the next center
        # This method saves time by faster filtration the non-palindromes
        # Because once left != right, then no more check on longer substrings with this center.

    def countSubstrings(self, s):
        # # a modification from above center expanding algorithm

        # The oirignal way of assigning left and right is not very explicit
        ans = 0
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = left + j  # right will be lastly assigned as right = len(s), which is unnecessary
                # but the while loop has limited right < len(s), so it won't be executed

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans


if __name__ == '__main__':
    assert Solution().countSubstrings("abc") == 3, "regular"
    assert Solution().countSubstrings("aaa") == 6, "'a', 'a', 'a', 'aa', 'aa', 'aaa'"
    assert Solution().countSubstrings("abcba") == 7
    print("all passed")
