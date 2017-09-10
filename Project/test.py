# 这样就实现了当1个x值被remove后,打断第二重迭代,继续第一重x的迭代,测试下个x.这样就不会出现相同的x需要被remove所形成的冲突.
pnumber1b_fix = list(range(2, 101))
pnumber1b_fixB = list(range(2, 101))
for x in pnumber1b_fixB:
    for i in range(2, x):
        if x % i == 0:
            pnumber1b_fix.remove(x)
            break
print(pnumber1b_fix)
