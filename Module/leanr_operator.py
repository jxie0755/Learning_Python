# operator.attrgetter(attr)
# operator.attrgetter(*attrs)

# operator.itemgetter(item)
# operator.itemgetter(*items)

# please see in ZsimpleLearnings/attrgetter_and_itemgetter.py



# operator.lt(a, b)  ==   a < b
# operator.le(a, b)  ==   a <= b
# operator.eq(a, b)  ==   a == b
# operator.ne(a, b)  ==   a != b
# operator.ge(a, b)  ==   a > b
# operator.gt(a, b)  ==   a >= b

# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)

# 逻辑操作也通常适用于所有对象，并支持真值测试，身份测试和布尔运算

# operator.not_(obj)
# operator.__not__(obj)
# 返回not obj。（请注意，对象实例没有__not__()方法；只有解释器核定义了此操作。结果受到__bool__()和__len__()方法的影响。）

# operator.truth(obj)
# 如果obj为真，则返回True，否则返回False。这相当于使用bool构造函数。

# operator.is_(a, b)
# 返回a 是 b。测试对象标识。

# operator.is_not(a, b)
# 返回a 是 不是 b。测试对象标识。
print(operator.is_not(6, 6))

# 数学和按位操作是最多的：

# operator.abs(obj)
# operator.__abs__(obj)
# 返回obj的绝对值

# operator.add(a, b)
# operator.__add__(a, b)
# 返回a + b，对于a和b t5 >数字

# operator.and_(a, b)
# operator.__and__(a, b)
# 返回按位和a和b
print(operator.and_(True, True))

# operator.floordiv(a, b)
# operator.__floordiv__(a, b)
# 返回a // b。

# operator.index(a)
# operator.__index__(a)
# 返回a转换为整数。等同于a.__index__()

# operator.inv(obj)
# operator.invert(obj)
# operator.__inv__(obj)
# operator.__invert__(obj)
# 返回数字obj的按位逆。这相当于~obj
print(operator.inv(123))  # >>> -124

# operator.lshift(a, b)
# operator.__lshift__(a, b)
# 返回a向左移动b

# operator.mod(a, b)
# operator.__mod__(a, b)
# 返回a % b

# operator.mul(a, b)
# operator.__mul__(a, b)
# 返回a * b，对于a和b t5 >数字

# operator.matmul(a, b)
# operator.__matmul__(a, b)
# 返回a @ b

# operator.neg(obj)
# operator.__neg__(obj)
# 返回obj否定（-obj）。

# operator.or_(a, b)
# operator.__or__(a, b)
# 返回按位或a和b。

# operator.pos(obj)
# operator.__pos__(obj)
# 返回obj正（+obj）。

# operator.pow(a, b)
# operator.__pow__(a, b)
# 对于a和b，返回a ** b t5>数字。

# operator.rshift(a, b)
# operator.__rshift__(a, b)
# 返回a向右移动b。

# operator.sub(a, b)
# operator.__sub__(a, b)
# 返回a - b。

# operator.truediv(a, b)
# operator.__truediv__(a, b)
# 返回a / b其中2/3为.66而不是0。这也被称为“真正的”分裂。

# operator.xor(a, b)
# operator.__xor__(a, b)
# 返回a和b的逐位异或。

# 使用序列（其中一些与映射）的操作包括：

# operator.concat(a, b)
# operator.__concat__(a, b)
# 对于a和b返回a + b序列。

# operator.contains(a, b)
# operator.__contains__(a, b)
# 返回 t> a中的测试结果b 。注意反向操作数。

# operator.countOf(a, b)
# 返回a中b的出现次数。

# operator.delitem(a, b)
# operator.__delitem__(a, b)
# 删除索引b处a的值。

# operator.getitem(a, b)
# operator.__getitem__(a, b)
# 返回a在索引b的值。

# operator.indexOf(a, b)
# 返回a中b的第一个出现的索引。

# operator.setitem(a, b, c)
# operator.__setitem__(a, b, c)
# 将索引b处的a值设置为c。

# operator.length_hint(obj, default=0)
# 返回对象o的估计长度。首先尝试返回其实际长度，然后使用object.__length_hint__()进行估计，最后返回默认值。

# operator.iadd(a, b)
# operator.__iadd__(a, b)
# a = iadd(a, b) is equivalent to a += b.

# operator.iand(a, b)
# 操作符。 __ iand __ （ a，b ） t5 >
# a = iand(a, b) is equivalent to a &= b.

# operator.iconcat(a, b)
# operator.__iconcat__(a, b)
# a = iconcat(a, b) is equivalent to a += b for a and b sequences.

# operator.ifloordiv(a, b)
# operator.__ifloordiv__(a, b)
# a = ifloordiv(a, b) is equivalent to a //= b.

# operator.ilshift(a, b)
# operator.__ilshift__(a, b)
# a = ilshift(a, b) is equivalent to a <<= b.

# operator.imod(a, b)
# operator.__imod__(a, b)
# a = imod(a, b) is equivalent to a %= b.

# operator.imul(a, b)
# operator.__imul__(a, b)
# a = imul(a, b) is equivalent to a *= b.

# operator.imatmul(a, b)
# operator.__imatmul__(a, b)
# a = imatmul(a, b) is equivalent to a @= b.

# operator.ior(a, b)
# operator.__ior__(a, b)
# a = ior(a, b) is equivalent to a |= b.

# operator.ipow(a, b)
# operator.__ipow__(a, b)
# a = ipow(a, b) is equivalent to a **= b.

# operator.irshift(a, b)
# operator.__irshift__(a, b)
# a = irshift(a, b) is equivalent to a >>= b.

# operator.isub(a, b)
# operator.__isub__(a, b)
# a = isub(a, b) is equivalent to a -= b.

# operator.itruediv(a, b)
# operator.__itruediv__(a, b)
# a = itruediv(a, b) is equivalent to a /= b.

# operator.ixor(a, b)
# operator.__ixor__(a, b)
# a = ixor(a, b) is equivalent to a ^= b.
