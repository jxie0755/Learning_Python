"""
Learn Python Type Hint
PEP 484 - https://www.python.org/dev/peps/pep-0484/
PEP 526 - https://www.python.org/dev/peps/pep-0526/

全面理解Python中的类型提示（Type Hints）
https://sikasjc.github.io/2018/07/14/type-hint-in-python/


众所周知，Python 是动态类型语言，运行时不需要指定变量类型
而在2014年9月，Guido van Rossum (Python BDFL) 创建了一个Python增强提议(PEP-484)，为Python添加类型提示（Type Hints）
并在一年后，于2015年9月作为Python3.5.0的一部分发布了.
于是对于存在了二十五年的Python，有了一种标准方法向代码中添加类型信息
"""


def send_request(request_data : Any,
                 headers: Optional[Dict[str, str]],
                 user_id: Optional[UserId] = None,
                 as_json: bool = True) -> "List[Any]":

    return [request_data, headers, user_id, as_json]



def test2(a: typing.List[str],
                    b: typing.List[str],
                    c: typing.Dict[int, str]) -> typing.Dict[str, str]:
    return {a[1]: "a1", b[2]: "b2", c[3]: "c3"}


# request_data可以是任何数据
# header的内容是一个可选的字符串字典
# UserId是可选的（默认为None），或者是符合编码UserId的任何数据
# as_json需要始终是一个布尔值（本质上是一个flag，即使名称可能没有提供这种提示）


# 使用
# ":"  语句将信息附加到变量或函数参数中。
# "->" 运算符用于将信息附加到函数/方法的返回值中。


# 这种方法
# 好处是:
    # 这是实现类型提示的规范方式，这意味着是类型提示中最干净的一种方式
    # 因为类型信息附加在代码的右侧，这样我们可以立刻明晰类型

# 缺点是：
    # 它不向后兼容。至少需要Python 3.6才能使用它。
    # 强制你导入所有类型依赖项，即使它们根本不在运行时使用。
    # 在类型提示中，会使用到复合类型，例如List[int]。而为了构造这些复杂类型，解释器在首次加载此文件时需要执行一些操作。
