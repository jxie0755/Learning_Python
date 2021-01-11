"""
https://leetcode.com/problems/longest-palindromic-substring/
P005 Longest Palindromic String
Medium

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""


class Solution_A:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(N^2) + O(1/2N) = O(N^2)
        Space: O(N)
        Maximum time limit exceeded
        """
        def is_palindrome(s: str) -> bool:
            """Helper"""
            return s == s[::-1]

        if not s:
            return ""

        length, L = len(s), len(s)

        while L != 0:
            for i in range(0, length - L + 1):
                sample = s[i:i + L]
                if is_palindrome(sample):
                    return sample
            L -= 1


class Solution_B:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(N^2)
        Space: O(1)
        Interate the center points and expand on each
        """
        length = len(s)
        result = ""
        for a in range(0, len(s)):

            theoretical_length = (min(a - 0, length - a) + 1) * 2

            if theoretical_length < len(result):  # 此处得到一个该中心点的理论最长回文长度, 如果仍然不够当前result
                break  # 就可以break, 因为后面也不可能出现更长的回文了

            for b in range(a + 1, a + 3):  # 这里控制起始字符要么就是a, 要么就是aa, 用于奇数和偶数回文
                head, tail = a, b

                while head >= 0 and tail <= length and s[head] == s[tail - 1]:
                    sample = s[head:tail]  # 根据起始点,向两侧扩展, 直到发现不是回文为止
                    if len(sample) > len(result):  # 如果发现长于result就取代
                        result = sample
                    head -= 1
                    tail += 1

        return result


class Solution_C:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(N^2) + O(1/2N) = O(N^2)
        Space: O(N)
        Interate the center points and expand on each, easier to read than Solution B
        """

        result = ""

        # two checks in one iteration, odd length check and even length check
        for i in range(len(s)):

            # first odd length check
            odd_j = i
            odd_k = i
            while odd_j >= 0 and odd_k <= len(s) -1 and s[odd_j] == s[odd_k]:
                result = max(result, s[odd_j:odd_k + 1], key=len)
                odd_j -= 1
                odd_k += 1

            # second even length check, only when found two consecutuve identical
            even_j = i
            even_k = i + 1
            while even_j >= 0 and even_k <= len(s) -1 and s[even_j] == s[even_k]:
                result = max(result, s[even_j:even_k + 1], key=len)
                even_j -= 1
                even_k += 1

        return result


# TODO: Practice Manacher's algorithm (Dynamic Programming)
# class Solution_STD:
#     def longestPalindrome(self, s: str) -> str:
#         """
#         Manacher's algorithm (Dynamic programming)
#         Time: O(N)
#         """
#         pass


if __name__ == "__main__":
    testCase = Solution_C()
    assert testCase.longestPalindrome("") == "", "Edge 1"
    assert testCase.longestPalindrome("a") == "a", "Edge 2"
    assert testCase.longestPalindrome("aaa") == "aaa", "Edge 3"

    assert testCase.longestPalindrome("babad") == "bab" or "aba", "Example 1"
    assert testCase.longestPalindrome("cbbd") == "bb", "Example 2"

    assert testCase.longestPalindrome("bababadddddddddddd") == "dddddddddddd", "Extra 1"
    assert testCase.longestPalindrome("babababa") == "abababa" or "bababab", "Extra 2"

    a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    b = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert testCase.longestPalindrome(a) == b, "Long string"

    print("All passed")
