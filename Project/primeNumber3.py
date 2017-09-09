# 最简练
# 不使用函数, 直接找出1-100 prime number,可以修改范围
pnumber = [x for x in range(2, 101) if all(x % i for i in range(2, x))]
print(pnumber)

