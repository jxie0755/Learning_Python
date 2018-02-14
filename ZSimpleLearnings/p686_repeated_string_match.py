# p686 Repeated String Match
# Easy

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
# Note:
# The length of A and B will be between 1 and 10000.

# """
# :type A: str
# :type B: str
# :rtype: int
# """

class Solution:
    def repeatedStringMatch(self, A, B):  # two conditions
        if len(A) >= len(B):
            # if A longer than B, A only need to maximumly repeat 3 times
            for i in [1, 2, 3]:
                if B in A*i:
                    return i
        else:
            count = 1
            add_on = A
            while len(A) <= 3 * len(B):
                # if B longer than A, A needs to be maximumly repeated untill 3 times of B's length
                if B in A:
                    return count
                A += add_on
                count += 1
        return -1
        # However, this method is not very fast

if __name__ == '__main__':
    assert Solution().repeatedStringMatch('abcd', 'cdabcdab') == 3, 'regular in'
    assert Solution().repeatedStringMatch('abcd', 'cccccccccccccc') == -1, 'regular not in'
    assert Solution().repeatedStringMatch('abcd', 'abcd') == 1, 'just one'
    assert Solution().repeatedStringMatch('abcd', 'dabcda') == 3, 'one extra on both end 1'
    assert Solution().repeatedStringMatch('a', 'aaa') == 3, 'one extra on both end 1'
    assert Solution().repeatedStringMatch('abcd', 'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd') == 11, 'long'
    assert Solution().repeatedStringMatch('aaaaaaaaaa', 'a') == 1, 'A longer than B'
    assert Solution().repeatedStringMatch('aaaaaaaaab', 'ba') == 2, 'A longer than B 2'
    assert Solution().repeatedStringMatch('a', 'aaaaaaaaaa') == 10, 'B longer than A'
    assert Solution().repeatedStringMatch('abababaaba', 'aabaaba') == 2, 'A longer than B 2'
    print('all passed')
