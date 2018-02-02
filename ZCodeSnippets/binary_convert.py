# A function to convert a binary number to decimal number
# 1011 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
def bi_to_deci_0(target):
    """target should be a binary number made with '1' and '0'"""
    target = str(target)
    ans = 0
    numlevel = len(target)
    for index in range(0, numlevel):
        ans += int(target[numlevel - index - 1]) * 2**index  
                                                   # 此处2,代表2进制.
    return ans

if __name__ == '__main__':
    print(bi_to_deci_0(1010))  # >>> 10

# 先把target反过来,再计算就更简短
def bi_to_deci(target):
    """target should be a binary number made with '1' and '0'"""
    target = str(target)
    target = target[::-1]
    ans = 0
    for i in range(len(target)):
        ans += int(target[i]) * 2**i
    return ans

if __name__ == '__main__':
    print(bi_to_deci(1010))  # >>> 10
    

# A function to convert a decimal number to binary
# 用2辗转相除至结果为1
# 将余数和最后的1从下向上倒序写 就是结果 （逆序）
# 例如10
# 10/2 = 5 余0
# 5/2 = 2 余1
# 2/2 = 1 余0
# 1/2 = 0 余1  # 一定要除以2结果最终到0
# 故二进制为1010

def deci_to_bin(target):
    """target should be an positive integer"""
    ans = ''
    while target != 0:
        target, digit = divmod(target, 2)
        ans = str(digit) + ans
    return int(ans)

if __name__ == '__main__':
    print(deci_to_bin(10))  # >>> 1010
