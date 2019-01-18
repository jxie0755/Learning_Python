# Learn python bit calculations

# Python位运算符
# 按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：


# 下表中变量 a 为 60，b 为 13，二进制格式如下：

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a&b = 0000 1100  (12)  # 每位相同则为1, 不同则为0

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a|b = 0011 1101  (61)  # 每位相同则为该位, 不同则为1

# a =   0011 1100  (60)
# b =   0000 1101  (13)
# a^b = 0011 0001  (49)  # 每位相同则为0, 不同则为1


# ~: 按位取反运算符：对数据的每个二进制位取反, ~x 类似于 -x-1
# a =   0011 1100 (60)
# ~a  = 1100 0011  # 每位反转, 本来是0就换成1, 本来是1就换成0

print(~60)  # (-61)
print(bin(60))  #   111100
print(bin(-61))  # -111101
                #   000011
print(int('000011', 2))     # 3 ???

print(~100) # (-101)
print(bin(100))  #  1100100
print(bin(-101)) # -1100101
                 #  0011011
print(int('0011011', 2))    # 27 ???

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

# 一些同学可能会疑惑，~8不应该是 ~0b1000 = 0b0001 = 1 才对吗。
# 事情是这样的，计算机在内部表示负整数的时候用的是正数的补，
# 比如 0b0001 是1，它的补是 0b1110，这个时候0b1110 在计算机内部不是7，而是-1。
# 这样一来，可以推导出来~n的结果是 -n-1 。
# 不过你自己写的0b1111在这个语境下并不是一个负数，所以结果仍是15


# Even assuming you are using one byte:
#     60 would be 0011 1100
# So ~60 would be 1100 0011
#  -128 + 64 + 2 + 1 = -61 ???
