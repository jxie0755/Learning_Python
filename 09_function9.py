# return后面不赋值则返回None

def maximum(x, y):
    if x > y:
        return x
    if x == y:
        return
    else:
        return y

print(maximum(4, 3))
print(maximum(3, 3))
print(maximum(2, 3))

# pass 也表示return none
def some_function():
    pass
print(some_function())
