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
    
    
# what if the decimal number is a float?
def deci_float_to_bi(target):
    """converts a decimal float number to binary float numebr
    target should be a positive decimal float number"""
    p = 0
    
    # 首先要把浮点数乘以2的p次方,变成一个整数
    while ((2 ** p) * target) % 1 != 0:  # 很关键,这里设定必须被1整除,才是整数
        p += 1
    print('Magnify target 2^', p, 'times, to be an integer:')
    num = int(target * (2 ** p))  # 这里得到一个整数num
    print('target is now', num)
    
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    
    # 预防措施,万一p大于result的长度,需要补0在前方
    for i in range(p - len(result)):
        result = '0' + result
    
    
    # 由于之前放大了target, 2^p倍,所以现在要缩小回去,除以10^p得到最终结果
    # 这里用字符串处理,避免前置0被省略
    result = result[0:-p] + '.' + result[-p:]
    print('Convert target to binary number:', result)
    
    return float(result)

if __name__ == '__main__':
    print(deci_float_to_bi(1.123123))
