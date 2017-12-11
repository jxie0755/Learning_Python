# All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

# Input: A number as an integer.
# Output: The string representation of the number as a string.
# Precondition: 0 < number < 1000

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number).zfill(3)  # format the number to 3 digit string
    result = ''

    # at hundreds
    for i in range(10):
        if number[0] == str(i) and number[0] != '0':
            result += FIRST_TEN[i-1] + ' ' + HUNDRED

    # at tens
    for i in range(10):
        if number[1] == str(i) and number[1] != '0' and number[1] != '1':
            result += ' ' + OTHER_TENS[i-2]

    # at ones
    for i in range(0, 10):
        if number[1] == '1' and number[2] == str(i) and number[2] != '0':
            result += ' ' + SECOND_TEN[i]
        elif number[1] == '1' and number[2] == str(i) and number[2] == '0':
            result += ' ' + SECOND_TEN[0]
        elif number[1] != '1' and number[2] == str(i) and number[2] != '0':
            result += ' ' + FIRST_TEN[i-1]

    return result.strip()


# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(4) == 'four', "1st example"
#     assert checkio(133) == 'one hundred thirty three', "2nd example"
#     assert checkio(12) == 'twelve', "3rd example"
#     assert checkio(101) == 'one hundred one', "4th example"
#     assert checkio(212) == 'two hundred twelve', "5th example"
#     assert checkio(40) == 'forty', "6th example"
#     assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
#     print('done')

print(checkio(202))

