"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
P003 Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.
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

            hastable = {}
            for i in s:
                if i not in hastable:
                    hastable[i] = 1
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


class Solution_B1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(N^2), Space O(N)
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
            hashtable = {}
            i = 0
            while i != len(s):
                if s[
                    i] in hashtable:  # if repeat, then recursive compare to the next section, starting after the first repeating element.
                    new_start = hashtable[s[i]] + 1
                    return max(i, self.lengthOfLongestSubstring(s[new_start:]))
                hashtable[s[i]] = i
                i += 1
            else:  # if no repeat, go to the end and return the full length
                return len(s)



class Solution_B2:
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
            hashtable = {}
            while i != len(s):
                current = s[i]
                if current not in hashtable:
                    hashtable[current] = i
                    i += 1
                    if i == len(s):  # Define an end case as no repeating found at the last element
                        result.append(i - label)
                else:
                    result.append(i - label)
                    i = hashtable[current] + 1
                    label = i
                    hashtable = {}

            return max(result)


class Solution_STD:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time O(N), Space O(1)
        借字符表运算
        """
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
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
    print("all passed")
