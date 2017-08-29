x = 50
def func(x):
    print ('x is', x)
    x = 2
    print('Changed global x to', x)

x=2
func(x)
