# p696 Count Binary Substrings
# Easy

# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

# """
# :type s: str
# :rtype: int
# """

class Solution:
    def countBinarySubstrings(self, s):
        # this is another way of modification of substring method
        substring = []
        i = 0
        while i < len(s):
            for lenth in range(1, len(s) - i + 1):
                substring.append(s[i:i + lenth])
            i += 1

        def check(s):
            fst_half, sec_half = s[:len(s) // 2], s[len(s) // 2:]
            if len(s) % 2 != 0:
                return False
            if fst_half == '0' * len(fst_half) and sec_half == '1' * len(sec_half):
                return True
            elif fst_half == '1' * len(fst_half) and sec_half == '0' * len(sec_half):
                return True
            else:
                return False

        result = list(filter(check, substring))
        return len(result)
        # O(n^2), brutal force, time limit exceeded

    def countBinarySubstrings(self, s):
        # two step method, no need to get all substrings

        # first split the string into groups of '0' and '1', O(n)

        # original codes:
        # s += ' '
        # start, end = 0, 1
        # groups = []
        # while end < len(s):
        #     if s[start] == s[end]:
        #         end += 1
        #     else:
        #         groups.append(s[start:end])
        #         start, end = end, end + 1

        # replace by simple python string method:
        groups = s.replace('01', '0 1').replace('10', '1 0').split()

        # then calculate the possible count of
        # loop over every two contiuguous group, the number of possible substring is len(shorter_group), O(n)
        count = 0
        for i in range(len(groups) - 1):
            count += min(len(groups[i]), len(groups[i + 1]))
        return count
        # Overall O(n), a better algorithm


if __name__ == '__main__':
    assert Solution().countBinarySubstrings('00110011') == 6, 'test 1'
    assert Solution().countBinarySubstrings('10101') == 4, 'test 2'
    print('all passed')
