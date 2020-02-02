"""
doctest module
https://docs.python.org/3/library/doctest.html
"""

# Quick Example 1

def f(x):
    """times 2
    >>> f(2)
    4
    >>> f(5)
    10
    """
    return x * 2

def g(x):
    """times 3
    >>> g(2)
    6
    >>> g(5)
    15
    """
    return x * 3

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)  # 此处verbose默认为True,会输出结果,若为false则只有出错才出结果
    # 这里会测试整个文件的所有函数

# 若只单独测试一个函数, 可以利用独立测试文件,只测试模块中的一个函数
if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(f, globals(),verbose=True)



# 在terminal中使用
# input$ python -m doctest unnecessary_math.py
# input$ python -m doctest -v unnecessary_math.py
# 这里 -m 表示引用一个模块, -v 等价于 verbose=True. 运行输出与上面基本一样



# 独立测试文件
# 果不想将doctest测试用例嵌入到python的源码中, 则可以建立一个独立的文本文件来保存测试用例
# 建立leanr_doctest_indi.txt
# 注意txt文件中需要import原文件
