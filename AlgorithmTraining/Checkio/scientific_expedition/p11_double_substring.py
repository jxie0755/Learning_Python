"""
You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps.
Input: String.
Output: Int.
"""


import re
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

    # 注意这里同样也是用了全部的sub-string,但是筛选了里面重复出现的元素,放到一个list
    # 然后将得到的list中的重复的元素去除,使用set功能.
    target_list = sorted(set(list(filter(lambda x: temp.count(x) >=2, temp))), key=len)[::-1]
    if len(target_list) == 0:
        return 0
    else:
        # 利用re的finall,把太长的字符串(重叠情况)去掉,最后得到结果.
        for i in target_list:
            if len(re.findall(i, line)) == 2:
                return len(i)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring("aaaa") == 2, "First"
    assert double_substring("abc") == 0, "Second"
    assert double_substring("aghtfghkofgh") == 3, "Third"
    print("'Run' is good. How is 'Check'?")

# 另解
def double_substring2(line):
    result = 0
    for i in range(len(line)):
        for j in range(len(line[i:])):
            if (line.count(line[i:j]) > 1) and (len(line[i:j]) > result):
                result = len(line[i:j])
    return result

print(double_substring2("aghtfghkofgh"))
