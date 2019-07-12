# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".

# Input: String.
# Output: String.

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # obtain a list contains all the possible sub-string in line
    substring_list = []
    n = 0
    m = 0
    word = len(line)
    while n < word:
        for m in range(0, word):
            if 1 + m + n <= word:
                substring_list.append(line[m:1 + m + n])
        else:
            n += 1

    def check_repeat(x):
        temp = []
        for i in x:
            if i in temp:
                return False
            else:
                temp.append(i)
        return True
    try:
        return max(list(filter(check_repeat, substring_list)), key=len)
    except ValueError:
        return ""

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat("aaaaa") == "a", "First"
    assert non_repeat("abdjwawk") == "abdjw", "Second"
    assert non_repeat("abcabcffab") == "abcf", "Third"
    assert non_repeat("fghfrtyfgh") ==  "ghfrty", "extra check"
    assert non_repeat("") == "", "empty string"
    print(""Run" is good. How is "Check"?")
