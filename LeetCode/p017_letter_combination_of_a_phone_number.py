# P017 Letter Combination of a Phone Number
# Medium


# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pass



if __name__ == '__main__':
    assert Solution().letterCombinations('') == [], 'Edge 1'
    assert Solution().letterCombinations('1') == [], 'Edge 2'

    assert Solution().letterCombinations('2') == ['a', 'b', 'c'], 'Example 1'
    assert Solution().letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 'Example 1'
    assert Solution().letterCombinations('213') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 'Example 2'

    print('all passed')
