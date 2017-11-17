# Learning leading zero 

a = '1'  # must convert a number first
print('%03d' % int(a))  
print('{:03}'.format(int(a)))  
print('{num:03d}'.format(num=int(a)))
print('{0:03'.format(int(a)))
print('{0:03d}'.format(int(a)))            # add a 'd'
print(f'{0:02}{int(a)}')                   # f-string
print(f'{0:02d}{int(a)}')                  
print(a.zfill(3))                          # zfill() works on str not int
print(a.rjust(3, '0'))                     # rjust() also works on str
# >>> 001 for all of above

dd = 'abc'
print(dd.zfill(5))       # 注意参数使用最终的长度,而不是加几个0
print(dd.rjust(5, '0'))  
# >>> 00abc

b = 1.5
print('%03d' % b)    # >>> 001 # 忽略小数点
print(str(b).zfill(5))        # zfill只能添加0
print(str(b).rjust(5, '0'))   # rjust,ljust, center可以加任何str
# >>> 001.5

print(str(b).center(7, 'a'))  # >>> aa1.5aa
