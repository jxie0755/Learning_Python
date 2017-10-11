def g(x):
    def h():
        x = 'abc'
        return x
    x = x + 1
    print('in g(x): x =', x)
    h()
    print('x =', x)
    return x
x = 3
z = g(x)
# 注意h()没有return value,所以在h()中虽然x='abc'但是对于程序没有任何影响