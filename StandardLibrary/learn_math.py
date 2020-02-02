"""
math module
https://docs.python.org/3/library/math.html#module-math
"""


import math

# module attributes

# math.pi
# 数学常量 π = 3.141592......, 到现有的精度. 

# math.e
# 数学常数 e = 2.718281......, 到现有的精度. 

# math.inf
# 浮点正无穷大. (对于负无穷大, 请使用-math.inf. )相当于float("inf")的输出. 

# math.nan
# 浮点数"不是数字"(NaN)值. 等效于float("nan")的输出

print()
print("数理论和表示函数")

# math.ceil(x)
# Return the ceiling of x, 大于等于 x 的最小整数.如果x是整数,则返回本身.
print(math.ceil(4.1234))   # >>> 5
print(math.ceil(-4.1234))  # >>> -4
print(math.ceil(5))        # >>> 5

# math.floor(x)
# Return the floor of x, 小于等于 x的最大整数.如果x是整数,则返回本身.
print(math.floor(4.1234))   # >>> 4
print(math.floor(-4.1234))  # >>> -5
print(math.floor(5))        # >>> 5

# math.copysign (x, y)
# 返回x的绝对值大小和y的符号
print(math.copysign(-5, -6))  # >>> -5.0
print(math.copysign(-5, 7))   # >>> 5.0

# math.fabs(x)
# 返回x的绝对值
print(math.fabs(-5.5))  # >>> 5.5

# math.factorial(x)
# 返回x的阶乘. 如果x不是整数或者是负数, 返回错误ValueError
print(math.factorial(4))  # >>> 24  # (4*3*2*1)

# math.fmod(x, y)
# 计算余数, 与x%y略有不同
print(math.fmod(4, 2))  # >>> 0.0
print(math.fmod(10, 3.3))  # >>>> 0.10000000000000053

# math.frexp(x)
# 将x的尾数和指数作为对(m, e)返回 so that x == m * 2**e
print(math.frexp(20))  # >>>  (0.625, 5)

# math.ldexp(x, i)
# 返回x*(2**i). 这基本上是函数frexp()的逆运算
print(math.ldexp(0.625, 5))  # >>> 20

# math.fsum(iterable)
# 在可迭代中返回值的准确浮动点总和
# 通过跟踪多个中间部分款项, 避免了精度损失
print(sum([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))        # 10 * 0.1  # >>>  0.9999999999999999
print(math.fsum([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))  # 10 * 0.1  # >>>  1.10

# math.gcd(a, b)
# 返回整数a和b的最大公约数, gcd(0, 0)返回0
print(math.gcd(12,16))  # >>> 4

# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
# 如果a和b的值彼此接近, 则返回True, 反之则False
# rel_tol is the relative tolerance – it is the maximum allowed difference between a and b
# To set a tolerance of 5%, pass rel_tol=0.05
# abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero
print(math.isclose(100, 90, rel_tol=0.05))  # >>> False  # 设置为百分比

# math.isfinite(x)
# 如果x既不是无穷大也不是NaN, 则返回True, 否则返回False. 注意0.0 是被认为是有限的
print(math.isfinite(5))    # >>> True
print(math.isfinite(1/3))  # >>> True  # 无限循环小数也是有限的
print(math.isfinite(math.pi))  # True  # 无限不循环小数也是有限
# print(math.isfinite(1/0))    # raise ZeroDivisionError

# math.isinf(x)
# 如果x是正或负无穷大, 则返回True, 否则返回False
print(9e2)  # >>> 900.0
print(math.isinf(9e999))  # >>> True

# math.isnan(x)
# 如果x是NaN(不是数字), 则返回True, 否则返回False

# math.modf(x)
# 返回x的小数和整数部分. 这两个结果携带的x标志, 也是浮点型
print(math.modf(5.25))  # >>> (0.25, 5.0)  # in a tuple
print(math.modf(5.123))  # >>> (0.12300000000000022, 5.0)
print(5.123 == sum(math.modf(5.123)))  # True  # 虽然显示起来不是,但是数学上成立

# math.trunc(x)
# 将Real值x返回到Integral(通常为整数), 代表x.__trunc__()
# behaves as a ceiling function for negative number and floor function for positive number
# 不确定x的正负值的时候使用
print(math.trunc(10.5))   # >>> 10
print(math.trunc(-10.5))  # >>> -10



print()
print("幂函数和对数函数")

# math.exp(x)
# 返回 e**x (e的x幂方)
print(math.exp(2))  # >>> 7.38905609893065

# math.expm1(x)
# 返回e**x - 1
print(math.expm1(2))  # >>> 6.38905609893065

# math.log(x[, base])
# 具有一个可选参数, 默认则返回的x (以e) 的自然对数
print(math.log(5))  # 相当于 ln(5)
print(math.log(81, 3))  # >>> 4.0  # 相当于 log3^81

# math.log1p(x)
# 返回1 + x (底数e) 的自然对数. 其结果被计算在某种程度上是准确, 可用于x接近于零
print(math.log1p(4))  # 相当于 ln(4+1)

# math.log2(x)
# 返回x的基2对数这通常比log(x, 2)更准确
print(math.log2(8))  # >> 3.0  # 相当于 log2^8

# math.log10(x)
# 返回x的对数. 这通常比log(x, 10)更准确
print(math.log10(1000))  # >>> 3.0  # 相当于 log10^1000

# math.pow(x, y)
# 返回x的y次幂

# math.sqrt(x)
# 返回 x 的平方根



print()
print("三角函数")

# math.sin(x)
print(math.sin(math.pi/2))  # >>> 1.0
print(math.sin(math.pi))    # >>> 1.2246467991473532e-16  也就是0

# math.cos(x)
# math.tan(x)
# math.acos(x)
# math.asin(x)
# math.atan(x)
# math.atan2(y, x)  # 它可以计算角度的正确象限

# math.hypot(x, y)
# 返回欧氏方程, sqrt(x * x + y * y). 这是从原点到点(x,  y)的向量长度

print()
print("角度转换")

# math.degrees(x)
# 将角度x从弧度转换为度
print(math.degrees(math.pi))    # >>> 180.0
print(math.degrees(math.pi/2))  # >>> 90.0
print(math.degrees(math.pi/4))  # >>> 45

# math.radians(x)
# 将角度x从度转换为弧度
print(math.radians(180))    # >>> 3.141592653589793  # pi



print()
print("双曲线函数是基于双曲线而不是圆的三角函数的类似")
# math.sinh(x)
# 返回x的双曲正弦值. 

# math.cosh(x)
# 返回x的双曲余弦值. 

# math.tanh(x)
# 返回x的双曲正切值. 

# math.asinh(x)
# 返回x的反双曲正弦值. 

# math.acosh(x)
# 返回x的反双曲余弦值. 

# math.atanh(x)
# 返回x的反双曲正切值. 



print()
print("特殊函数")

# math.erf(x)
# 在x返回错误函数. 
# erf()函数可用于计算传统的统计函数, 例如累积标准正态分布

# math.erfc(x)
# 返回在x的余误差函数. 定义为1.0 - erf(x)

# math.gamma(x)
# 返回 x 的 Gamma function (伽马函数)

# math.lgamma(x)
# 返回伽玛函数在x的绝对值的自然对数
