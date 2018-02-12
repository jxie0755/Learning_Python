# http://liuchunming033.github.io/posts/2016/06/13/python-doctest.html

# Python has a great way to quickly write tests for your code. These are called doctests, and look like this:

def multiply(a, b):
        """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

# >>>
# Trying:
# multiply(4, 3)
# Expecting:
# 12
# ok
# Trying:
#     multiply('a', 3)
# Expecting:
#     'aaa'
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#   2 tests in __main__.multiply
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.

