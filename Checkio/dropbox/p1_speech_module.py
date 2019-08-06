"""
All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.
Output: The string representation of the number as a string.
Precondition: 0 < number < 1000
"""


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    number = str(number).zfill(3)  # format the number to 3 digit string

    # at hundreds
    if int(number[0]) != 0:
        hundreds = FIRST_TEN[int(number[0])-1] + " hundred"
    else:
        hundreds = ""

    # at tens
    if int(number[1]) in range(2, 10):
        tens = " " + OTHER_TENS[int(number[1])-2]
    elif int(number[1]) == 1:
        tens, ones = "", " " + SECOND_TEN[int(number[2])]
    elif int(number[1]) == 0:
        tens = ""

    # at ones
    if int(number[2]) in range(1,10) and int(number[1]) != 1:
        ones = " " + FIRST_TEN[int(number[2]) -1]
    elif int(number[2]) == 0 and int(number[1]) != 1:
        ones = ""

    return (hundreds + tens + ones).strip()


# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(4) == "four", "1st example"
#     assert checkio(133) == "one hundred thirty three", "2nd example"
#     assert checkio(12) == "twelve", "3rd example"
#     assert checkio(101) == "one hundred one", "4th example"
#     assert checkio(212) == "two hundred twelve", "5th example"
#     assert checkio(40) == "forty", "6th example"
#     assert not checkio(212).endswith(" "), "Don't forget strip whitespaces at the end of string"
#     print("done")

print(checkio(202))
