# random module
# https://docs.python.org/3/library/random.html#module-random


# Python的这个库在底层使用通用的算法，经过长久的考验，可靠性没得说，但该模块的伪随机生成器不应该用于安全目的!

# 几乎所有模块函数都依赖于基本函数random()，其在半开放范围[0.0,1.0)(包括0但是不包括1)中均匀地生成随机浮点数
#   * 对于整数，有一个范围的均匀选择
#   * 对于序列，存在随机元素的均匀选择，产生就地列表的随机置换的函数，以及用于无替换的随机采样的函数

# 该模块提供的函数实际上是random.Random类的隐藏实例的约束方法. 您可以实例化您自己的Random实例，以获得不共享状态的生成器

#   * 如果你想使用你自己设计的不同的基本生成器，类Random也可以是子类：在这种情况下，覆盖random()，seed()，getstate()和setstate()方法。
#   * 可选地，新的生成器可以提供getrandbits()方法 - 这允许randrange()在任意大的范围上产生选择
#   * random模块还提供SystemRandom类，它使用系统函数os.urandom()从操作系统提供的源生成随机数

import random

# 基本功能 Book-keeping function
print()
print('random.seed(a=None, version=2)')
# 初始化生成器的随机数
# 改变随机数生成器的种子(也就是seed永远不会重复)，可以在调用其他随机模块函数之前调用此函数
# 要每次产生随机数相同就要设置种子，相同种子数的Random对象，相同次数内,生成的随机数字是完全相同的
random.seed(5)
print(random.random())  # >>> 0.6229016948897019
print(random.random())  # >>> 0.7417869892607294  # seed只能用于生成一次
random.seed(5)
print(random.random())  # >>> 0.6229016948897019  # seed相同就生成相同的随机数

print()
print('random.getstate()')
# 返回捕获生成器的当前内部状态的对象。此对象可以传递到setstate()以恢复状态

print('random.setstate(state)')
# 状态应该从先前对getstate()的调用获得，并且setstate()将生成器的内部状态恢复为是在当时getstate()被调用

# STOF: https://stackoverflow.com/q/48504854/8435726
# state就是为了方便使用seed(), 不需要记忆seed设置,只需要保存为一个state,随时可以setstate()来保证生成相同随机数 (应用于多个不同的seed的场景,可以理解为为seed命名)
# 速度上用state更快,因为seed()会生成一个state,而每次call seed都会生成一个相同的state,比getstate()保存一个state速度慢

random.seed(5)
st1 = random.getstate()  # 这是seed之后立刻保存
print(random.random())  # >>> 0.6229016948897019

random.setstate(st1)    # 每次生成之前setstate
print(random.random())  # >>> 0.6229016948897019

print()
print('random.getrandbits(k)')
# 返回一个 k 位(bit) 的随机整数, 如k=8,返回8bit范围内的随机数，即0-255的随机数
print(random.getrandbits(8))  # >>> 177



# 生成随机整数的函数
print()
print('random.randrange(stop)')
print('random.randrange(start, stop[, step])')
# 从range(start, stop, step)返回一个start到end范围内的随机整数(start, end, step都是整数, 不包含end), 可以指定step
# 位置参数模式与range()匹配。不应使用关键字参数，因为函数可能以意想不到的方式使用它们

print(random.randrange(10))  # 生成0 to 9之间的随机整数
print(random.randrange(-10, 0))  # 负数要规定范围,不能单参数(-10 to -1)
print(random.randrange(10, 21, 2))  # 随机生成10 to 20之间的偶数

print()
print('random.randint(a, b)')
# 返回一个随机整数N，a <= N <= b, 相当于randrange(a, b+1)


# 生成随机序列的函数
print()
print('random.choice(seq)')
# 从非空序列seq返回一个随机元素。如果seq为空，则引发IndexError
print(random.choice([1,2,3]))  # >>> 2  #  从序列中随机抽取一个元素
print(random.choice(range(5)))  # >>> 3  # from iterator/generator

print()
print('random.shuffle(x[, random])')
# 原地搅乱序列x。可选参数random是一个具有0个参数的函数，返回一个[0.0, 1.0)之间的随机浮点数；默认情况下为函数random()
lst = [1, 2, 3, 4]
random.shuffle(lst)  # 注意是原地搅乱,不生成新序列
print(lst)  # >>> [3, 1, 4, 2]

print()
print('random.sample(population, k)')
# 返回从群体序列或集合中选择的唯一元素的k长度列表。用于随机抽样，无需更换
# 适合用于不可变序列 (tuple)
# 如果样本大小大于总体大小，则会引发ValueError
tup = (1, 2, 3, 4, 5)
print(random.sample(tup, 3))  # >>> [4, 2, 1]
print(random.sample(range(5), 5))  # >>> [1, 0, 4, 2, 3]  # from iterator/generator



# 生成特定的实值分布的函数
print()
print('random.random()')
# 返回下一个在范围 [0.0, 1.0) 中的随机浮点数

print()
print('random.uniform(a, b)')
# Return a random floating point number N such that a <= N <= b
# 包含两端端点
print(random.uniform(1, 2))      # >>> 1.6945944582538162
print(random.uniform(1.5, 2.5))  # >>> 2.343164464258881

print()
print('random.triangular(low, high, mode)')
# 返回随机浮点数N, 使得低 N = 高，并指定模式。低和高边界默认为零和一. 模式参数默认为边界之间的中点, 给出对称分布
# mode = 0.5表示正太分布, 调整模式可以调整随机分布模式(偏离中点)

print()
print('random.betavariate(alpha, beta)')
# Beta分布. Conditions on the parameters are alpha > 0 and beta > 0. 返回值的范围为0到1

print()
print('random.expovariate(lambd)')
# 指数分布。lambd为1.0除以所需平均值。它应该是非零的。（该参数将被称为“lambda”，但这是Python中的保留字。）
# 如果lambd为正，返回值的范围为0到正无穷大，如果lambd为负，则从负无穷大到0

print()
print('random.gammavariate(alpha, beta)')
# 伽玛分布. (不是伽玛函数!) Conditions on the parameters are alpha > 0 and beta > 0

print()
print('random.gauss(mu, sigma)')
# 高斯分布. mu是平均值, sigma是标准偏差

print()
print('random.normalvariate(mu, sigma)')
# 正态分布. mu是平均值, sigma是标准偏差

print()
print('random.lognormvariate(mu, sigma)')
# 对数正态分布. 如果采用此分布的自然对数, 您将得到平均值mu和标准偏差sigma的正态分布. mu可以具有任何值, 并且sigma必须大于零

print()
print('random.paretovariate(alpha)')
# 帕累托分布. alpha是形状参数.

print()
print('random.weibullvariate(alpha, beta)')
# Weibull分布. alpha是缩放参数, beta是形状参数
