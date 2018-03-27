# P017 Number letter counts


# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens.
# 342 (three hundred and forty-two) contains 23 letters
# 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


def read_number(n):
    """in the range of 1 - 1000"""

    digit_dict_1 = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    digit_dict_2 = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
                    '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
                    '19': 'nineteen'}

    digit_dict_3 = {'1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
                    '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

    str_n = str(n).zfill(4)
    result = ''

    # thousand digit
    if str_n[0] != '0':
        result += (digit_dict_1[str_n[0]] + 'thousand')

    # hundred digit
    if str_n[1] != '0':  # '11xx' or '01xx'
        result += (digit_dict_1[str_n[1]]) + 'hundred' + 'and'
    elif str_n[0] != '0' and str_n[1] == '0':  # '10xx'
        result += 'and'

    # tens digit:
    if str_n[2] != '0' and str_n[2] != '1' and str_n[3] != '0':  # typical 'XX'
        result += digit_dict_3[str_n[2]] + digit_dict_1[str_n[3]]
    elif str_n[2] != '0' and str_n[2] != '1' and str_n[3] == '0':  # typical 'X0'
        result += digit_dict_3[str_n[2]]
    elif str_n[2] == '1' and str_n[3] != '0':
        result += digit_dict_2[str_n[2:4]]
    elif str_n[2] == '1' and str_n[3] == '0':
        result += 'ten'
    elif str_n[2] == '0' and str_n[3] != '0':
        result += digit_dict_1[str_n[3]]
    elif str_n[2] == '0' and str_n[3] == '0':
        result = result[:-3]

    return result


if __name__ == '__main__':
    print('test read_number()')
    print(read_number(1))
    print(read_number(3))
    print(read_number(10))
    print(read_number(12))
    print(read_number(22))
    print(read_number(36))
    print(read_number(45))
    print(read_number(80))
    print(read_number(115))
    print(read_number(140))
    print(read_number(500))
    print(read_number(811))
    print(read_number(901))
    print(read_number(1000))
    print()


def number_letter_counts(start, end):
    result = 0
    for i in range(start, end + 1):
        result += len(read_number(i))
    return result


if __name__ == '__main__':
    assert number_letter_counts(1, 5) == 19, 'regular 1 to 5'
    print(number_letter_counts(1, 1000))
    # >>> 21124
    # passed
