x = 50
def func(x):
    print ('x is', x)
    x = 2
    print('Changed global x to', x)

func(x)
print('Value of x is still', x)



