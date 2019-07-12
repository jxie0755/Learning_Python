# p344 Reverse String
# Easy

# Write a function that takes a string as input and returns the string reversed.

# """
# :type s: str
# :rtype: str
# """

class Solution:
    def reverseString(self, s):
        return s[::-1]

    def reverseString(self, s):
        return "".join(reversed(s))


if __name__ == "__main__":
    assert Solution().reverseString("hello") == "olleh"
    print("all passed")
