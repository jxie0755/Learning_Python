try:
    a = int(input('a:'))
    b = int(input('b:'))
    print('a/b is', a/b)
except:
    print('something is not right')
else:
    print('else will be executed')
finally:
    print('There is always a final part')

