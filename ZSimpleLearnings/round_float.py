# round()如果只有一个数作为参数，不指定位数的时候，返回的是一个整数，而且是最靠近的整数（这点上类似四舍五入）。
# 但是当出现.5的时候，两边的距离都一样，round()取靠近的偶数，这就是为什么round(2.5) = 2。
# 当指定取舍的小数点位数的时候，一般情况也是使用四舍五入的规则，
# 但是碰到.5的这样情况，如果要取舍的位数前的小树是奇数，则直接舍弃，如果偶数这向上取舍。看下面的示例：

# python 四舍五入的问题

# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。
print(round(1.5, 0))  # >>> 2.0
print(round(2.5, 0))  # >>> 2.0
# 也就是说，对1.5或者2.5的舍入运算都会得到2

print(round(1.45, 1))  # >>> 1.4
print(round(2.55, 1))  # >>> 2.5

# 不要将舍入和格式化输出搞混淆了。 如果你的目的只是简单的输出一定宽度的数，你不需要使用 round() 函数。
#  而仅仅只需要在格式化的时候指定精度即可。

print(format(1.5, '0.0f'))  # >>> 2
print(format(2.5, '0.0f'))  # >>> 2

# 由于小数转float过程中的误差造成
print(format(1.55, '0.1f'))  # >>> 1.6
print(format(2.55, '0.1f'))  # >>> 2.5

# 但是format仍然不解决四舍五入精度问题


print()
print('use decimal to solve rounding problem')
# 消除四舍五入误差请用decimal模块!!
# decimal 的默认 context 是“四舍六入五留双”，rounding=ROUND_HALF_EVEN 
# 四舍五入要把rounding改成ROUND_HALF_UP

from decimal import *
print(Decimal(Decimal('1.45').quantize(Decimal('.1'), rounding=ROUND_HALF_UP)))  # >>> 1.5
print(Decimal(Decimal('2.55').quantize(Decimal('.1'), rounding=ROUND_HALF_UP)))  # >>> 2.6

print(Decimal(Decimal('1.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP)))  # >>> 2
print(Decimal(Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP)))  # >>> 3

# 或者直接修改context(),这时再用round或者format就好了
# 记住一定用str input,不要用float
getcontext().rounding = ROUND_HALF_UP 
print(round(Decimal('1.45'), 1))  # >>> 1.5
print(round(Decimal('2.55'), 1))  # >>> 2.6
print(round(Decimal('1.5'), 0))  # >>> 2
print(round(Decimal('2.5'), 0))  # >>> 3

# 使用format()也可以
print(format(Decimal('1.45'), '0.1f'))  # >>> 1.5
print(format(Decimal('2.55'), '0.1f'))  # >>> 2.6
print(format(Decimal('1.5'), '0.0f'))  # >>> 2
print(format(Decimal('2.5'), '0.0f'))  # >>> 3

# f-string输出用法  
# 同时引用Decimal解决四舍五入问题
getcontext().rounding = ROUND_HALF_UP
print(f"{Decimal('1.45'):.1f}")  # >>> 1.5   
print(f"{Decimal('1.45'):.2}")   # >>> 1.5   
