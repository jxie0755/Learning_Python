# P003 Longest Substring Without Repeating Characters
# Medium


# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Brutal Force Time O(N^3)
        ### Get all substrings from long to short, then check each on repeating characters
        ### Fail as Maximum Time limit exceeded
        """
        :type s: str
        :rtype: int
        """
        def is_no_repeat(s):
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
            for i in range(0, len(s)-j+1):
                sample = s[i:i+j]
                if is_no_repeat(sample):
                    return len(sample)



class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Time O(N^2), Space O(N)
        ### Find repeating element and start again after the first repeating element
        ### Recursion is dangerous with maximum recursion depth limit, this one will fail at a long string test case!!
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:
            hashtable = {}
            i = 0
            while i != len(s):
                if s[i] in hashtable:  # if repeat, then recursive compare to the next section, starting after the first repeating element.
                    new_start = hashtable[s[i]]+1
                    return max(i, self.lengthOfLongestSubstring(s[new_start:]))
                hashtable[s[i]] = i
                i += 1
            else:   # if no repeat, go to the end and return the full length
                return len(s)


# Idea is like:
# abcdefghXijklmXoMqrstMuvwxyz
# abcdefghXijklmX.....            Find X occured twice, then stop and recalculate after the first X
#          ijklmXoMqrstM...       Find M occured twice, then stop and recalculate after the first M
#                  qrstMuvwxyz    until it ends, and compare each secion


class Solution:
    def lengthOfLongestSubstring(self, s):
        ### Time O(N^2), Space O(N)
        ### Non-recursive way to previous method
        """
        :type s: str
        :rtype: int
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
                        result.append(i-label)
                else:
                    result.append(i-label)
                    i = hashtable[current] + 1
                    label = i
                    hashtable = {}

            return max(result)


class Solution(object):
    ### Time O(N), Space O(N)
    ### No need to restart from first repeating element, just go iteration once
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        char_used = {}
        result = [0]

        for i,c in enumerate(s):  # use enumerate to record and iterate i and character at the same time!
            if c not in char_used:
                result.append(i - start+1)
            else:
                start = char_used[c] + 1
            char_used[c]=i

        return max(result)


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring("") == 0, 'Edge 1'
    assert Solution().lengthOfLongestSubstring(" ") == 1, 'Edge 2'
    assert Solution().lengthOfLongestSubstring("au") == 2, 'Edge 3'
    assert Solution().lengthOfLongestSubstring("aab") == 2, 'Edge 4'
    assert Solution().lengthOfLongestSubstring("dvdf") == 3, 'Edge 5'

    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3, 'Example 1, "abc"'
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1, 'Example 1, "b"'
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3, 'Example 1, "wke"'
    print('all passed')
