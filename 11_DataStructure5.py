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

