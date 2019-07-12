# you should find a repeating sequence inside the substring
# Input: String.
# Output: String.

def repeat_inside(line):
    # write a function to tell whether the string is a repeating string
    def check_repeat(x):
        i = 1
        while i <= len(x) // 2:
            if x[0:i] * (len(x) // i) == x:
                return True
            i += 1
        return False

    # break down line to substrings from long to short, and check on the run
    temp = []
    n, m = 0, 0
    index = len(line)
    while n < index:
        for m in range(0, n + 1):
            substring = line[m:index - n + m]
            if check_repeat(substring):
                return substring
        else:
            n += 1
    return ""


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside("aaaaa") == "aaaaa", "First"
    assert repeat_inside("aabbff") == "aa", "Second"
    assert repeat_inside("aababcc") == "abab", "Third"
    assert repeat_inside("abc") == "", "Forth"
    assert repeat_inside("abcabcabab") == "abcabc", "Fifth"
    print(""Run" is good. How is "Check"?")
