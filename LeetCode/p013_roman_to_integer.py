# p013 Roman to Integer
# Easy

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, roman_string):
        """
        :type roman_string: str
        :rtype: int
        """
        result = 0
        # remove the possibility of 4 and 9
        checklst = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        for i in checklst.keys():
            if i in roman_string:
                result += checklst[i]
                roman_string = roman_string.replace(i, '')

        # Calculate the rest of it
        Roman_Nu = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in roman_string:
            result += Roman_Nu[i]

        return result

print(Solution().romanToInt('CDXCIX'))
