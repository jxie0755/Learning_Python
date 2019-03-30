bri = set(['brazil', 'russia', 'india'])

print('india' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri)) # 超集
print(bri.issubset(bric)) # 子集

bri.remove('russia')
print(bri & bric)  # 交集
print(bri.intersection(bric)) # 交集


shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist2 = ['organge', 'mango', 'pear', 'banana']

name = 'swaroop'

print('apple' in shoplist)
print('apple' in shoplist2)
# print(shoplist & shoplist2) list是不能求子集交集的,只能用于set
