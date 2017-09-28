# 先做一个函数以供测试
# 显示名字的简单函数
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


# 进行测试
import unittest


class NamesTestCase(unittest.TestCase):
    """测试name function"""

    def test_first_last_name(self):
        # 函数的结果应该等于过程(假设一组实参)
        formatted_name = get_formatted_name('Denis', 'Xie')
        # assert断言结果应该是第二实参
        self.assertEqual(formatted_name, 'Denis Xie')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Adrienne', 'Xie', 'Yijun')
        self.assertEqual(formatted_name, 'Adrienne Yijun Xie')


unittest.main()