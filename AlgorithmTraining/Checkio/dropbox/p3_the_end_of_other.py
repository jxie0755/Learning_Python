"""
In this task, you are given a set of words in lower case.
Check whether there is a pair of words, such that one word is the end of another (a suffix of another).
For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.
Output: True or False, as a boolean.
"""


import itertools
def checkio(words_set):
    # get sub group of two words in combination
    subgroup = [sorted([x, y], key=len) for x, y in itertools.combinations(words_set, 2)]

    # check each sub group, if first item is a suffix of the second
    for i in subgroup:
        if i[1].endswith(i[0]):  # use string methods!!
            return True
    return False


if __name__ == "__main__":
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
