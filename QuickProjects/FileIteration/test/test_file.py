# P017 Letter Combination of a Phone Number
# Medium


# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

class Solution:

    # Version A, hashtable
    # Time:  O(n * 3^n)
    def letterCombinations(self, digits: str) -> List[str]:

        hashtable = {"0": [" "],
                     "1": [""],
                     "2": ["a", "b", "c"],
                     "3": ["d", "e", "f"],
                     "4": ["g", "h", "i"],
                     "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"],
                     "7": ["p", "q", "r", "s"],
                     "8": ["t", "u", "v"],
                     "9": ["w", "x", "y", "z"]
                     }

        result = []
        i = 0
        while i != len(digits):
            current = digits[i]

            if i == 0:
                result = hashtable[current]
            else:
                new = hashtable[current]
                result_len, new_len = len(result), len(new)
                result = sum([[i] * new_len for i in result], [])
                j, cycle = 0, 0
                while j != len(result):
                    result[j] = result[j] + new[cycle % new_len]
                    j += 1
                    cycle += 1
            i += 1
            a = r'"abc"'

        return result



if __name__ == "__main__":

    assert Solution().letterCombinations("") == [], "Edge 1"
    assert Solution().letterCombinations("1") == [""], "Edge 2"
    assert Solution().letterCombinations("0") == [" "], "Edge 3"

    assert Solution().letterCombinations("2") == ["a", "b", "c"], "Example 1"
    assert Solution().letterCombinations("20") == ["a ", "b ", "c "], "Example 2"
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 3"
    assert Solution().letterCombinations("213") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "Example 4"

    print("All passed")
