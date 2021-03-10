# LC345 Reverse Vowels of a String
# Easy

# Write a function that takes a string as input and reverse only the vowels of a string.
# Note:
# The vowels does not include the letter "y".

# """
# :type s: str
# :rtype: str
# """

class Solution:
    def reverseVowels(self, s):
        # O(n), n as len(s)
        vowels = "aeiouAEIOU"

        # Extract the vowels out as a string
        vowel_string = []
        for i in s:
            if i in vowels:
                vowel_string.append(i)

        # Replace the vowels
        result = ""
        for i in s:
            if i in vowels:
                result += vowel_string.pop()  # use pop() to reverse
            else:
                result += i
        return result

    def reverseVowels(self, s):
        # two pointer method
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while i < j and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i]
            i += 1
            j -= 1
        return "".join(L)


if __name__ == "__main__":
    assert Solution().reverseVowels("hello") == "holle", "test 1"
    assert Solution().reverseVowels("leetcode") == "leotcede", "test 2"
    assert Solution().reverseVowels("aA") == "Aa", "vowel mixed case"
    print("All passed")
