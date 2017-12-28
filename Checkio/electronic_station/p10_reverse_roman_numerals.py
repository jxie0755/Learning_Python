# You are given a roman number as a string and your job is to convert this number into its decimal representation.
# Input: A roman number as a string.
# Output: The decimal representation of the roman number as an int.


# 注意这里面dictionary的order问题!!!

def reverse_roman(roman_string):
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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
