# p443 String Compression
# Easy

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# Follow up:
# Could you solve it using only O(1) extra space?
# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.

# """
# :type chars: List[str]
# :rtype: int
# """

class Solution:
    def compress(self, chars):  # this actually compress chars
        chars.append('end')
        index, count = 0, 1  # set index as the editing position for compress
        for i in range(1, len(chars)):  # iterate the two continguous element
            if chars[i - 1] == chars[i]:
                count += 1
            else:
                if count == 1:
                    chars[index] = chars[i - 1]
                    index += 1
                else:
                    string_to_add = chars[i-1] + str(count)
                    for i in range(len(string_to_add)):
                        chars[index] = string_to_add[i]
                        index += 1
                    count = 1
        print(chars)
        return index

if __name__ == '__main__':
    assert Solution().compress(['a','a','b','b','c','c','c']) == 6, "regular, ['a', '2', 'b', '2', 'c', '3']"
    assert Solution().compress(['a']) == 1, "length of one, ['a']"
    assert Solution().compress(['a','b','b','b','b','b','b','b','b','b','b','b','b']) == 4, "high count, ['a', 'b', '1', '2']"

    print('all passed')
