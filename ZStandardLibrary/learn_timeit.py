# timeit module
# https://docs.python.org/3/library/timeit.html#module-timeit
# 本模块提供一个简单的方法来测量小的Python代码的时间

# 它同时具有Command-Line Interface以及python interface

import timeit
from ZSimpleLearnings.fibonacci import fib_gen_r

# 该模块定义了三个便利的函数和用一个公共类
print()
print("timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)")
# Create a Timer instance with the given statement
# setup code and timer function and run its timeit() method with number executions
print(timeit.timeit('list(range(0, 999))', number=10000))
# >>> 0.1661170139996102 # will vary depend on computer resource
print(type(timeit.timeit('list(range(0, 999))', number=10000)))
# >>> <class 'float'>

print(timeit.timeit('char in text', setup="text ='sample string'; char = 'g'", number=10000000))
# >>> 0.2998773199997231
print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))
# >>> 0.14675580299990543


# print(timeit.timeit('fib_gen_r(30)', number=10000))  # >>> 不能运行一个函数?
print(timeit.timeit('fib_gen_r(30)', setup='from __main__ import fib_gen_r', number=5))
# >>> 1.9347527580011956
# 此命令既可以对import的函数或者对本文件中的函数运行

print(timeit.timeit('fib_gen_r(30)', setup='from ZSimpleLearnings.fibonacci import fib_gen_r', number=5))
# >>> 2.0236477670005115
# 这样可以省略import,直接在timeit.timeit中引用


print()
print("timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000, globals=None)")

# 好处就是可以做repeat,得到一组运行时间的list,方便求平均值
print(timeit.repeat('list(range(0, 999))', repeat=3, number=10000))
# >>> [0.17210359499949845, 0.15265621899925463, 0.15970960199956608] # 输出一个list可以算平均值

# 函数同样可以在repeat中相似方法运行
print(timeit.repeat('fib_gen_r(30)', setup='from __main__ import fib_gen_r', repeat=3, number=3))
# >>> [1.2522393469989765, 1.2651939509996737, 1.2109857380000904]



print()
print("class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)")
# 为一个类,接用timeit和repeat方法

# timeit(number=1000000)  方法
print(timeit.Timer('list(range(0, 999))').timeit(number=10000))  # >>> 0.16091239100023813
# repeat(repeat=3, number=1000000) 方法
print(timeit.Timer('list(range(0, 999))').repeat(repeat=3, number=10000))
# >>> [0.1699522140006593, 0.15189915299924905, 0.16639813700021477]
print(timeit.Timer('fib_gen_r(30)', setup='from __main__ import fib_gen_r').repeat(repeat=3, number=5))
# >>> [1.9957611610007007, 1.9907497040003364, 1.9418537080000533]



print()
print("timeit.default_timer()")
# 默认计时器，始终为time.perf_counter()


print()
print("print_exc(file=None)")
# 从被计时的代码打印回溯的helper
# 典型用法:
t = timeit.Timer('list(range(0, 999))')       # outside the try/except
try:
    t.timeit(number=100000)    # or t.repeat(...)
except Exception:
    t.print_exc()