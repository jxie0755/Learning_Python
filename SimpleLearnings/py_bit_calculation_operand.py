"""
Learn python bit calculations
"""

# Python位运算符
# 按位运算符是把数字看作二进制来进行计算的. Python中的按位运算法则如下: 


# 下表中变量 a 为 60, b 为 13, 二进制格式如下: 

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a&b = 0000 1100  (12)  # 每位相同则为1, 不同则为0

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a|b = 0011 1101  (61)  # 每位相同则为该位, 不同则为1

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a^b = 0011 0001  (49)  # 每位相同则为0, 不同则为1


# ~: 按位取反运算符: 对数据的每个二进制位取反, ~x 类似于 -x-1
# a =   0011 1100 (60)
# ~a  = 1100 0011  # 每位反转, 本来是0就换成1, 本来是1就换成0

print(~60)  # (-61)
print(bin(60))  #   111100
print(bin(-61))  # -111101
print(bin(61))   #  111101
                #   000011
print(int("000011", 2))     # 3 ???

print(~100) # (-101)
print(bin(100))  #  1100100
print(bin(-101)) # -1100101
                 #  0011011
print(int("0011011", 2))    # 27 ???

# 以上都不对,原因是:

bin(~0b110) # get the binary representation of inverted 0b110
# 1|001         = each bit simply inverted (invert sign bit too (1|))
# -|4+2+0 +1    = each bit's contribution to the int, ‡See note
# -1*(4+2+0+1)  = -7    (the answer we want that represents each bit flipped)
# -0b111        = binary representation of -7
# -0b111          = it resembles 1|111 but it in memory it is actually 1|001
# -0b111 is 1|001 in memory!!!
# You shouldn't interpret a -ve binary number representation as what is stored in memory, unlike with a positive binary number.

# Note: Negative numbers in binary count backwards, so each -ve bit position is only counted toward composing the int if it's 0, and you must add -1 to the final result:

# in-memory  = int  (displayed as)
# 1|11..111    = -1   (-0b1)
# 1|11..110    = -2   (-0b10)
# 1|11..101    = -3   (-0b11)
# 1|11..100    = -4   (-0b100)
# and so on...

# 一些同学可能会疑惑, ~8不应该是 ~0b1000 = 0b0001 = 1 才对吗. 
# 事情是这样的, 计算机在内部表示负整数的时候用的是正数的补, 
# 比如 0b0001 是1, 它的补是 0b1110, 这个时候0b1110 在计算机内部不是7, 而是-1. 
# 这样一来, 可以推导出来~n的结果是 -n-1 . 
# 不过你自己写的0b1111在这个语境下并不是一个负数, 所以结果仍是15


# Even assuming you are using one byte:
#     60 would be 0011 1100
# So ~60 would be 1100 0011
#  -128 + 64 + 2 + 1 = -61 ???


# https://bytes.com/topic/python/answers/714382-bit-wise-unary-operator
# In C?
a = 7978
print(bin(a)) # 0001 1111 0010 1010
              # 1110 0000 1101 0101
print(int("1110000011010101", 2))  # 57557


# Final Example, 10
def binaryToInt(biNum, bUnsigned = False):
    iNum = 0
    bSign = int(biNum[0]) if not (bUnsigned or biNum[-1] == "u") else 0
    biNum = biNum[(1 if not (bUnsigned or biNum[-1] == "u") else 0):(len(biNum) if biNum[-1] != "u" else -1)]
    for i in range(len(biNum)):
        iNum += int(biNum[i]) * 2**(len(biNum) - 1 - i)
    return (iNum if not bSign else -iNum)

def intToBinary(iNum, bUnsigned = False):
    bSign = "1" if iNum < 0 else "0"
    iLoopNum = int((iNum ** 2) ** 0.5) #make positive!
    biNum = ""
    while iLoopNum:
        biNum += str(iLoopNum%2)
        iLoopNum /= 2
    return bSign + biNum[::-1] if not bUnsigned else biNum[::-1] + "u"


a = 10
print(bin(a)) # 01010
    # invert to 10101
print(int("10101", 2)) # 21 ??
# It is not right! Because, this is not how negative number is tranlated!!
print(bin(-11))  # -1011?? Not right!
# Correct way:
print(bin(11))   # 01011
       # invert to 10100
            # then add 1
                 # 10101 (negative 11)

# Therefore, ~10 is -11, because 01010 and 10101 is inverted.

# 32bit
# 10 is      00000000000000000000000000001010
# invert to  11111111111111111111111111110101
print(int("11111111111111111111111111110101", 2))  # 4294967285

print(binaryToInt("11111111111111111111111111110101", True))  # 4294967285
print(binaryToInt("11111111111111111111111111110101", False)) # -2147483637

# https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8
# 维基百科 2补数

# 符号
print(int("1111111", 2)) # 127
# 0	| 111 1111	=	127
# 1	| 000 0000	=	−128  (invert)
# 1	| 000 0001	=	−127

# 0	| 000 0010	=	2
# 1	| 111 1111	=	−1    (invert)
# 1	| 111 1110	=	−2    (invert, then +1)

# 0	| 000 0001	=	1
# 1	| 111 1110	=	−2    (invert)
# 1	| 111 1111	=	−1    (invert, then +1)


# 另一种较简单的方式, 可以找出二进制数字的补码: 

# 先由最低比特开始找. 
# 若该比特为0, 将补码对应比特填0, 继续找下一比特(较高的比特). 
# 若找到第一个为1的比特, 将补码对应比特填1. 
# 将其余未转换的比特进行比特反相, 将结果填入对应的补码. 
# 以0011 1100为例(图中的^表示当前转换的数字, -表示还不确定的位数): 
#
#    原数字       补码
#  0011 1100  ---- ---0(此比特为0)
#          ^
#
#  0011 1100  ---- --00(此比特为0)
#         ^
#
#  0011 1100  ---- -100(找到第1个为1的比特)
#        ^
#
#  0011 1100  1100 0100(其余比特直接反相)
#  ^
# 因此其结果为1100 0100



# x >> y and x << y
x = 10
x <<= 3  # means x = x * 2**3 = 10 * 8
# same as x = x << 3
print(10 << 3)  # means 10 * 2**3
print(x)  # >>> 80


x = 20
x >>= 3  # means x = x // 2**3 = 20 // 8
print(x) # >>> 2
