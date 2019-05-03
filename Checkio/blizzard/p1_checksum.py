# p1_checksum

# detail introduction: https://py.checkio.org/mission/check-digit/

# Input: Unsanitized numeric or alphanumeric due to formatting purpose
# Output: List of its final character and sum of digits

import string


def checkio(data):
    # get the numerals dict map_ppint
    digits = [i * 2 for i in range(10)]
    reduced = []
    for i in digits:
        if len(str(i)) == 2:
            reduced.append(int(str(i)[0]) + int(str(i)[1]))
        else:
            reduced.append(i)
    map_point = dict(zip(range(10), reduced))

    # get the data processed
    rdata = []
    for i in list((filter(str.isalnum, data))):
        if i in string.ascii_uppercase:
            rdata.append(str(ord(i) - 48))
        else:
            rdata.append(i)
    rvdata = rdata[::-1]

    # write a function to convert the data for both alpha and digits:
    def convert(x):
        if len(x) == 2:
            temp = str(int(x) * 2)
            return int(temp[0]) + int(temp[1])
        else:
            return map_point[int(x)]

    # process the data
    result = []
    for i in range(len(rvdata)):
        if i % 2 == 0:
            result.append(convert(rvdata[i]))
        else:
            result.append(int(rvdata[i]))

    # output the result
    F2 = sum(result)
    if F2 % 10 == 0:
        F1 = '0'
    else:
        F1 = str(10 - (F2 % 10))
    return [F1, F2]


if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"
    print("OK, done!")
