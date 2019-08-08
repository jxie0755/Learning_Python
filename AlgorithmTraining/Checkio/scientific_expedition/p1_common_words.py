"""
Let's continue examining words. You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string.

Input: Two arguments as strings.
Output: The common words as a string.
"""

def checkio(first, second):
    F = first.split(",")
    S = second.split(",")
    result = []
    for i in F:
        if i in S:
            result.append(i)
    return ",".join(i for i in sorted(result))

if __name__ == "__main__":
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"

# 另解: 利用交集 A & B
def checkio(first, second):
    common = set(first.split(",")) & set(second.split(","))
    return ",".join(sorted(common))
