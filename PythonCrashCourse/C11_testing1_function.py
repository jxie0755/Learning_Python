# V1
# 先定义函数, 然后
def get_formatted_name(first, last):
    """Generate a neatly formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()

# import模块
import unittest

# 创建一个类
class NamesTestCase(unittest.TestCase):  # 固定是TestCase
    """测试name function"""

    # 创建测试方法
    def test_first_last_name(self):         # 记得方法必须以'test'开头,否则不会运行
        # 函数的结果应该等于过程(假设一组实参)
        formatted_name = get_formatted_name('Denis', 'Xie')
        # assert断言结果应该是第二实参
        self.assertEqual(formatted_name, 'Denis Xie')

unittest.main()