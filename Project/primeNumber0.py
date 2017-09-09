pnumber = []
for x in range(2, 101):
    for i in range(2, x):
        if x % i == 0:
            break
            # 这是两重迭代,第一重:历遍每一个x去除以i. 第二重:x要除以历遍的每一个i.
            # 这个break是针对第二重迭代,使得只要有一个i能满足余数=0,那么这个x就不符合质数条件
            # 然后回到第一重迭代,试下一个x,如此往复.
    else:
        pnumber.append(x)
print(pnumber)


pnumber2 = []
for x in range(2, 101):
        if all(x % i for i in range(2, x)):
        # 使用all(),等于简写break的第二重历遍.
        # all()要求只有x除以每一个i都能余数!=0,(=0就是False,!=0也就是必须为True),这个x才能符合质数条件.
            pnumber2.append(x)
print(pnumber2)

# 这个是反写, 首先创造一个list包含全部的2-100.
# 然后条件反转,如果能整除(余数=0, not all), 则不符合质数条件,从而删掉一个x
# 最终留下来的就是质数
pnumber2 = list(range(2, 101))
for x in range(2, 101):
        if not all(x % i for i in range(2, x)):
            pnumber2.remove(x)
print(pnumber2)
