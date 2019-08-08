# 出现异常exception

# print(5/0)
# 在以上例子: ZeroDivisionError 就是一个异常对象Exception Object

# 通过try...except方式解决
try:
    print(5/0)
except ZeroDivisionError:
    print("You can\"t divide by zero.')
