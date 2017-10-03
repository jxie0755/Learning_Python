import inspect

def func(a, b):
    """calculation of sum of two parameters"""
    print(a + b)

func(2, 5)
inspect.getcomments(func)