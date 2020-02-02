"""
decimal module
https://docs.python.org/3/library/decimal.html#module-decimal
"""

# decimal模块支持快速正确舍入的十进制浮点运算. 它提供了优于float数据类型的几个优点
    # * 十进制"是基于一个浮点模型, 其设计考虑了人类计算习惯. 
    # * 十进制数可以精确表示. 相反, 诸如1.1和2.2的数字在二进制浮点中没有精确表示. 最终用户通常不会期望1.1 + 2.2显示为3.3000000000000003与二进制浮点. 
    # * 精确性转化为算术. 在十进制浮点中, 0.1 + 0.1 + 0.1 - 0.3完全等于零. 在二进制浮点中, 结果为5.5511151231257827e-017. 当接近零时, 差异阻止可靠的相等测试, 并且差异可累积. 因此, 在具有严格相等不变量的会计应用程序中, 十进制是首选. 
    # * 十进制模块包含重要位置的概念, 以便1.30 + 1.20是2.50尾随零被保留以指示重要性. 这是货币应用的习惯表述. 对于乘法, "教科书"方法使用被乘数中的所有数字. For instance, 1.3 * 1.2 gives 1.56 while 1.30 * 1.20gives 1.5600.
    # * 与基于硬件的二进制浮点不同, 十进制模块具有用户可改变的精度(默认为28个位置), 其可以与给定问题所需的一样大

from decimal import *

# 解决四舍五入问题,请看ZSimpleLearnings/round_float.py

print()
print("decimal.getcontext()")
# 使用getcontext()查看当前上下文, 如果需要, 可以为精度, 四舍五入或启用陷阱设置新值
# python 3.5新功能: 上下文精度和舍入仅在算术运算期间起作用
print(decimal.getcontext())
# >>>
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        # capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])


# 计算精度控制
decimal.getcontext().prec = 6
num1 = Decimal(1) / Decimal(7)
print(type(num1))  # >>> <class "decimal.Decimal">  # 计算结果仍然是decimal的实例
print(num1)  # >>> 0.142857  # show as __str__ for human to read

getcontext().prec = 12
print(num1)  # >>> 0.142857  # 一旦num1在精度为6计算出来,则保持精度,就算改变精度也不会改变其自身
num2 = Decimal(1) / Decimal(7)
print(num2)  # >>> 0.142857142857

print(type(num2))  # >>> <class "decimal.Decimal">
print(repr(num2))  # >>> Decimal("0.142857142857")



print()
print("class decimal.Decimal(value='0', context=None)")

# value可以是整数, 字符串, 元组, float或另一个Decimal对象. 如果未给出值, 则返回Decimal("0")
# 推荐使用字符串

# value 可选字符串
# sign           ::=  "+" | "-"
# digit          ::=  "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
# indicator      ::=  "e" | "E"
# digits         ::=  digit [digit]...
# decimal-part   ::=  digits "." [digits] | ["."] digits
# exponent-part  ::=  indicator [sign] digits
# infinity       ::=  "Infinity" | "Inf"
# nan            ::=  "NaN" [digits] | "sNaN" [digits]
# numeric-value  ::=  decimal-part [exponent-part] | infinity
# numeric-string ::=  [sign] numeric-value | [sign] nan

n0 = Decimal()
n1 = Decimal("12.13")
n2 = Decimal("infinity")
n3 = Decimal("NaN")

# If value is a tuple, it should have three components
# a sign (0 for positive or 1 for negative), a tuple of digits, and an integer exponent.
print(Decimal((1, (1, 4, 1, 4), -3)))  # >>> -1.414
print(Decimal((0, (2, 0, 0, 8), 5)))   # >>> 2.008E+8

print(n0, n1, n2, n3)  # >>> 0 12.13 456 Infinity NaN
print(n2 * n1)  # >>> Infinity



print()
print("余数处理")

# 余数操作符%应用于十进制对象时, 结果的符号是被除数的符号, 而不是除数的符号
print((-7) % 4)                  # >>> 1   # 余数为正
print(Decimal(-7) % Decimal(4))  # >>> -3  # 余数为负, 符号跟随被除数(-7)
print(7 % (-4))                  # >>> -1
print(Decimal(7) % Decimal(-4))  # >>> 3

# 整除//也有区别
print((-7) // 4)                  # >>> -2   # 倾向让余数正
print(Decimal(-7) // Decimal(4))  # >>> -1   # 倾向余数为负

# 整除//也有区别, 返回一个整数值,使得 (x//y) = (x - x % y) / y
print((-7) // 4)                  # >>> -2
print(Decimal(-7) // Decimal(4))  # >>> -1
print((Decimal(-7) // Decimal(4)) == (Decimal(-7) - Decimal(-7) % Decimal(4))/Decimal(4))  # >>> True

# 维持自身逻辑统一: x == (x // y) * y + x % y
print(Decimal(-7) // Decimal(4) * Decimal(4) + Decimal(-7) % Decimal(4))  # >>> -7



print()
print("Decimal类方法")

# adjusted()
# 在移出系数的最右边数字之后, 返回调整后的指数, 直到只剩下前导数字
print(Decimal("12345").adjusted())  # >>> 4  # 1.2345e4
print(Decimal("321e5").adjusted())  # >>> 7 # 这里321e5 == 32100000 = 3.21e7, 所以为7

# as_integer_ratio()  # python 3.6 新方法
# Return a pair (n, d) of integers that represent the given Decimal instance as a fraction, in lowest terms and with a positive denominator
print(Decimal("1.25").as_integer_ratio())  # >>> (5, 4)
# print(Decimal(1.33).as_integer_ratio())    # >>> (748723438050345, 562949953421312)  # because input floats
print(Decimal("1.33").as_integer_ratio())  # >>> (133, 100)   # always use string input!!!
# getcontext() can solve the floats problem
# getcontext().traps[FloatOperation] = True  # this can raise error message to remind that you made a mistake by using floats
print(Decimal(0.8) > 0.7)  # >>> True  # this will be prevented if FloatOperation was set to True

# as_tuple()
# 返回named tuple表示形式
print(Decimal("12345").as_tuple())  # >>> DecimalTuple(sign=0, digits=(1, 2, 3, 4, 5), exponent=0)
print(Decimal("-321e5").as_tuple())  # >>> DecimalTuple(sign=1, digits=(3, 2, 1), exponent=5)
# same as tuple input, but this output as a tuple

# canonical()
# 返回参数的规范编码. 目前, Decimal实例的编码始终是规范的, 因此此操作将返回其参数不变
print(Decimal("123").canonical())  # >>> 123

# compare(other, context=None)
# 比较两个小数实例的值. compare()返回一个Decimal实例, 如果任一操作数是NaN, 则结果为NaN
n1 = Decimal(207)
n2 = Decimal(133)
print(n1.compare(n2))  # >>> 1   # a > b : Decimal("1")
print(n2.compare(n1))  # >>> -1  # a < b : Decimal("-1")
print(Decimal(1.23e+4).compare(Decimal(12.3e+3)))  # >>> 0  # a == b : Decimal("0")

# compare_signal(other, context=None)
# This operation is identical to the compare() method, except that all NaNs signal.
# That is, if neither operand is a signaling NaN then any quiet NaN operand is treated as though it were a signaling NaN

# compare_total(other, context=None)¶
# Compare two operands using their abstract representation rather than their numerical value.
# Similar to the compare() method, but the result gives a total ordering on Decimal instances.
# Two Decimal instances with the same numeric value but different representations compare unequal in this ordering
print(Decimal("12.0").compare_total(Decimal("12")))  # >>> -1
print(Decimal("12.0").compare_total(Decimal(12.0)))  # >>> -1
print(Decimal("12").compare_total(Decimal(12)))  # >>> 0

# compare_total_mag(other, context=None)
print(Decimal("-12").compare_total_mag(Decimal(12)))  # >>> 0

# copy_abs()
# Return the absolute value of the argument
print(Decimal("-5e3").copy_abs())  # >>> 5E+3

# copy_negate()
# Return the negation of the argument
print(Decimal("-5e3").copy_negate())  # >>> 5E+3
print(Decimal("5e-3").copy_negate())  # >>> -0.005

# copy_sign(other, context=None)
# Return a copy of the first operand with the sign set to be the same as the sign of the second operand
print(Decimal("2.3").copy_sign(Decimal("-1.5")))  # >>> -2.3

# exp(context=None)
# Return the value of the (natural) exponential function e**x at the given number.
print(Decimal("2").exp())  # >>> 7.389056098930650227230427461  # e^2

# from_float(f)
# Classmethod that converts a float to a decimal number
# return a python True floats that is acting like a decimal value of the float
print(Decimal.from_float(0.1))  # >>> 0.1000000000000000055511151231257827021181583404541015625
print(0.1000000000000000055511151231257827021181583404541015625 * 2)  # >>> 0.2

# fma(other, third, context=None)
# Fused multiply-add. Return self*other+third with no rounding of the intermediate product self*other
print(Decimal("5.1").fma(2, 3))  # >>> 13.2

# TODO 未学完
