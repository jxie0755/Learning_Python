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
                if B in A * i:
                    return i
        else:
            count = 1
            add_on = A
            while len(A) <= 3* len(B):  # not the best limit
                # if B longer than A, A needs to be maximumly repeated untill 3 times of B's length
                if B in A:
                    return count
                A += add_on
                count += 1
        return -1
        # this is quite slow

    def repeatedStringMatch(self, A, B):
        limit = 2 * len(A) + len(B)   # best limit should be 2A + B
        count = 1
        add = A
        while len(A) <= limit:
            if B in A:
                return count
            A += add
            count += 1
        return -1
        # but this is still quite slow
    
    def repeatedStringMatch(self, A, B):
        # This gives a quick examination and that hugely improved speed for not wasting time on long strings
        if not set(B).issubset(set(A)):
            return -1
        
        # The rest is the same as above
        limit = 2 * len(A) + len(B)
        count = 1
        add = A
        while len(A) <= limit:
            if B in A:
                return count
            A += add
            count += 1
        return -1
            
    
if __name__ == '__main__':
    # A > B
    assert Solution().repeatedStringMatch('aaaaaaaaaa', 'a') == 1, 'A>B, in'
    assert Solution().repeatedStringMatch('aaaaaaaaab', 'ba') == 2, 'A>B in 2'
    assert Solution().repeatedStringMatch('abababaaba', 'aabaaba') == 2, 'A>B 3'
    assert Solution().repeatedStringMatch('abcd', 'da') == 2, 'A>B, extra characters in A'
    # A <= B
    assert Solution().repeatedStringMatch('abcd', 'abcdabcd') == 2, 'A<B regular in'
    assert Solution().repeatedStringMatch('abcd', 'cccccccccccccc') == -1, 'A<B regular not in'
    assert Solution().repeatedStringMatch('abcd', 'abcd') == 1, 'A=B in'
    assert Solution().repeatedStringMatch('abcd', 'dabcda') == 3, 'A<=B one extra on both end 1'
    assert Solution().repeatedStringMatch('a', 'aaa') == 3, 'A<B one extra on both end 2'
    assert Solution().repeatedStringMatch('abcd', 'dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd') == 11, 'A<B long in 1'
    assert Solution().repeatedStringMatch('a', 'aaaaaaaaaa') == 10, 'A<B long in 2'
    assert Solution().repeatedStringMatch('a', 'aaaaaaaaaax') == -1, 'A<B long not in'
    print('all passed')
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
