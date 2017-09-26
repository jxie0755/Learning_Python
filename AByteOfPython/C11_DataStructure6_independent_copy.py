print('Simple Assignment')
shoplist = ['apple', 'mango', 'caroot', 'banana']
mylist = shoplist  # 用等号连接的新list并不独立

del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]  # 用fullslice的方法拷贝一个list，等形成独立的list
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
