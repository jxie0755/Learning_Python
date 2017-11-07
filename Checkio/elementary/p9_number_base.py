# You are given a positive number as a string along with the radix for it.
# Your function should convert it into decimal form.
# The radix is less than 37 and greater than 1.
# The task uses digits and the letters A-Z for the strings.
# 将其它进制转换为十进制

# Input: Two arguments. A number as string and a radix as an integer.
# Output: The converted number as an integer.

def checkio(str_number, radix):
    import string
    a = dict(zip(string.digits, list(range(0,10))))
    b = dict(zip(string.ascii_uppercase, list(range(10, 37))))
    c = {**a, **b}
    ans = 0
    numlevel = len(str_number)
    for index in range(len(str_number)):
        if c[str_number[numlevel - index - 1]] >= radix:
            return -1
        ans += c[str_number[numlevel - index - 1]] * radix**index
    return ans

if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# Other solutions
def checkio(str_number, radix):
    try:
        return int(str_number,radix)
    except ValueError:
        return -1
