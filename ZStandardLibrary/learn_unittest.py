# https://docs.python.org/3/library/unittest.html

import unittest

# 一般来说testing写在一个独立的文件里,然后import要测试的单元进来. 这里放在一起,方便显示
# 注意一次只能运行一个test case,这里整合在一起只是方便浏览 


# Testing functions

# Example 1, 测试一个简单函数 (显示名字)
# 先做一个函数以供测试
# 

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()


# 创建一个unittest.TestCase类
class NamesTestCase(unittest.TestCase):
    """测试name function"""
    def test_first_last_name(self):    # 建立测试方法,测试方法必须start with test
        # 函数的结果应该等于过程(假设一组实参)
        formatted_name = get_formatted_name('Denis', 'Xie')
        self.assertEqual(formatted_name, 'Denis Xie') # assert断言结果应该是第二实参

# 进行测试
if __name__ == '__main__':
    unittest.main()

# >>>
# E   # 第一场生成E, 指出有一个单元测试导致了错误
# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)  # 指出了错误出处
# ----------------------------------------------------------------------
# Traceback (most recent call last): # 指出错误原因
#   File "main.py", line 21, in test_first_last_name
#     formatted_name = get_formatted_name('Denis', 'Xie')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1)


# Example 2, 使用多个测试方法
# 改进函数,让其支持middle name

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
         full_name = first + ' ' + last
    return full_name.title()  # return a value很重要,不要用print


# 定制多个测试
class NamesTestCase(unittest.TestCase):
    """测试name function"""
    def test_first_last_name(self):
        # 函数的结果应该等于过程(假设一组实参)
        formatted_name = get_formatted_name('Denis', 'Xie')
        self.assertEqual(formatted_name, 'Denis Xie')
    
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Adrienne', 'Xie', 'Yijun')
        self.assertEqual(formatted_name, 'Adrienne Yijun Xie')

if __name__ == '__main__':
    unittest.main()

# Example 3, 一个求证参数是否为质数的函数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class PNumTest(unittest.TestCase):
    def test_is_prime_number(self):
        self.assertEqual(isPrime(97), True) # 不要使用'True',而是用bool value True

if __name__ == '__main__':
    unittest.main()

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


class PNumTest(unittest.TestCase):
    def test_is_prime_number(self):  
        # 使用遍历的方法测试同一个类型的多个参数
        plist = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in plist:
            self.assertTrue(isPrime(i))  # 使用asertTrue()

    def test_is_prime_number2(self):
        plist = [4, 6, 8, 10]
        for i in plist:
            self.assertFalse(isPrime(i))  # 使用asserFalse()

if __name__ == '__main__':
    unittest.main()
    
    
    

