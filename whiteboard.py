import timeit

# 测试一个函数?
print(timeit.timeit('fib_gen_r(30)', setup='from ZCodeSnippets.fibonacci import fib_gen_r', number=5))
# >>> 1.9347527580011956
# 此命令既可以对import的函数或者对本文件中的函数运行
# 若fib_gen_r()为本地函数则'from __main__ import fib_gen_r'