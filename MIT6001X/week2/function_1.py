def is_even(i):
   """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
   # """contains the specification docstring"""

   print("hi")
   return i % 2 == 0

is_even(3)

def f():
    global x   # global 不能作用于argument
    x = x + 1
    print("x=", x)
    return x
    print("nnnn")  # code after return can not be executed

x = 3
f()
f()
