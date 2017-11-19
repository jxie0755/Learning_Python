# You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps.
# Input: String.
# Output: Int.

def double_substring(line):
    result = []
    n = 0
    m = 0
    word = len(line)
    while n < word:
        for m in range(0, word):
            if 1 + m + n <= word:
                result.append(line[m:1 + m + n])
        else:
            n += 1
    for i in result:
        if result.count(i) >=2:
            print(i)
    return 0

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert double_substring('aaaa') == 2, "First"
#     assert double_substring('abc') == 0, "Second"
#     assert double_substring('aghtfghkofgh') == 3, "Third"
#     print('"Run" is good. How is "Check"?')

double_substring('aaaa')
l = ['a', 'b', 'c', 'd', 'a']
print(l.count('a'))
