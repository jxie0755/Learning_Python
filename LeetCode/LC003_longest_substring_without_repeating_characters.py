"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
P003 Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.
possible characters are 26*2 (alphabetic) + >42 (other symboles) + 1(space) >= 95
"""


class Solution_A:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brutal Force Time O(N^3)
        Get all substrings from long to short, then check each on repeating characters
        Fail as Maximum Time limit exceeded
        """

        def is_no_repeat(s: str) -> bool:
            """Helper"""

            hmp = {}
            for i in s:
                if i not in hmp:
                    hmp[i] = 1
                else:
                    return False
            return True

        if not s:
            return 0

        for j in range(len(s), 0, -1):
            for i in range(0, len(s) - j + 1):
                sample = s[i:i + j]
                if is_no_repeat(sample):
                    return len(sample)


class Solution_B:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brutal Force Time O(N)
        Interate substrate in the level of 26 character length only (because max length is 26)

        Cannot Save time by check fixed length of 95 characters,
        but iterate each sub from length = 1 to 95 characeters

        This will pass but very slow
        """
        ans = 0
        for i in range(0, len(s)):
            sub = s[i:i + 100]
            for j in range(1, len(sub) + 1):
                subsub = sub[0:j]
                if len(subsub) == len(set(subsub)):
                    if ans < j:
                        ans = j
                else:
                    break
        return ans


class Solution_C1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(N^2), Space O(N)
        Recursive
        Find repeating element and start again after the first repeating element
        This wil pass, but may reach maximum recursion depth in long cases

        解读:
        abcdefghXijklmXoMqrstMuvwxyz
        abcdefghXijklmX.....            Find X occured twice, then stop and recalculate after the first X
                 ijklmXoMqrstM...       Find M occured twice, then stop and recalculate after the first M
                         qrstMuvwxyz    until it ends, and compare each secion
        """

        if not s:
            return 0
        else:
            hmp = {}
            i = 0
            while i != len(s):
                if s[i] not in hmp:
                    hmp[s[i]] = i
                else:
                    # if repeat, then recursive compare to the next section, starting after the first repeating element.
                    new_start = hmp[s[i]] + 1
                    return max(i, self.lengthOfLongestSubstring(s[new_start:]))
                i += 1

            else:  # base case for recursion
                # if no repeat, go to the end and return the full length
                return len(s)


class Solution_C2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(N^2), Space O(N)
        Non-recursive way of B1
        """

        result = []

        if not s:
            return 0
        else:
            i, label = 0, 0
            hmp = {}
            while i != len(s):
                if s[i] not in hmp:
                    hmp[s[i]] = i
                    i += 1
                    if i == len(s):  # Define an end case as no repeating found at the last element
                        result.append(i - label)
                else:
                    result.append(i - label)
                    i = hmp[s[i]] + 1
                    label = i
                    hmp = {}

            return max(result)


class Solution_STD:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(N), Space O(1)
        借字符表运算
        """
        longest, start, visited = 0, 0, [False for _ in range(256)]
        # 建立一个字符表list,256位长,默认全部都是false,因为一开始没有字符被找到

        for i, char in enumerate(s):  # 遍历字符串和其索引
            if not visited[ord(char)]:  # 如果字符之前没被找到过(也就是无重复)
                visited[ord(char)] = True  # 则标记True表示找到
            else:  # 一旦出现重复
                while char != s[start]:  # 从开始位置一直到这个出现重复位置的字符全部被清零
                    visited[ord(s[start])] = False
                    start += 1
                start += 1  # 下一次统计就从这个重复位置之后开始

            longest = max(longest, i - start + 1)  # 更新一下目前最大值
        return longest



if __name__ == "__main__":
    testCase = Solution_STD()
    assert testCase.lengthOfLongestSubstring("") == 0, "Edge 1"
    assert testCase.lengthOfLongestSubstring(" ") == 1, "Edge 2"
    assert testCase.lengthOfLongestSubstring("au") == 2, "Edge 3"
    assert testCase.lengthOfLongestSubstring("aab") == 2, "Edge 4"
    assert testCase.lengthOfLongestSubstring("dvdf") == 3, "Edge 5"

    assert testCase.lengthOfLongestSubstring("abcabcbb") == 3, "Example 1, abc"
    assert testCase.lengthOfLongestSubstring("bbbbb") == 1, "Example 2, b"
    assert testCase.lengthOfLongestSubstring("pwwkew") == 3, "Example 3, wke"
    assert testCase.lengthOfLongestSubstring("tmmzuxt") == 5, "Example 4, mzuxt"
    print("All passed")
