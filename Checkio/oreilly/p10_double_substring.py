# You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps.
# Input: String.
# Output: Int.

def double_substring(line):
    temp = []
    n, m = 0, 0
    word = len(line)
    while n < word:
        for m in range(0, word):
            if 1 + m + n <= word:
                temp.append(line[m:1 + m + n])
        else:
            n += 1
    try:
        str_target = (list(filter(lambda x: temp.count(x) >=2, temp))[-1])
        print(str_target)
        if str_target == str_target[0] * len(str_target):
            return len(str_target)//2 + 1
        else:
            return len(str_target)
    except IndexError:
        return 0


# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert double_substring('aaaa') == 2, "First"
#     assert double_substring('abc') == 0, "Second"
#     assert double_substring('aghtfghkofgh') == 3, "Third"
#     print('"Run" is good. How is "Check"?')

print(double_substring('abababaab'))

