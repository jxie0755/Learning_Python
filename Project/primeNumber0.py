# 寻找prime number
pnumber1 = []
for x in range(2, 101):
    for i in range(2, x):
        if x % i == 0:
            break
            # 这是两重迭代,第一重:历遍每一个x去除以i. 第二重:x要除以历遍的每一个i.
            # 这个break是针对第二重迭代,使得只要有一个i能满足余数=0,那么这个x就不符合质数条件
            # 然后回到第一重迭代,试下一个x,如此往复.
    else:
        pnumber1.append(x)
print(pnumber1)


# 这是跟上一版本相反的做法,先创造一个list把所有2-100的数字包括进去,然后去掉不是质数的数,剩下的保留
# !!!!!这个不会work,因为: 当一个item被remove,下次迭代的时候,发现这个item对于下个i又需要被remove
# 然后由于在上一个i的迭代中已经被remove,检查list的时候会发生冲突: 结果就是返回list.remove(x): x not in list
# pnumber1b = list(range(2, 101))
# for x in pnumber1b:
#    for i in range(2, x):
#        if x % i == 0:
#            pnumber1b.remove(x)
#        else:
#            break
# print(pnumber1b)

# 双list法:由于上一个版本发生list冲突,所以解决办法就是设计两个一样的list,把条件放到list1,执行放到list2
# 这样就实现了当1个x值被remove后,打断第二重迭代,继续第一重x的迭代,测试下个x.这样就不会出现相同的x需要被remove所形成的冲突.
# 这样做虽然繁琐,但是能达到目的
pnumber1b_fix = list(range(2, 101))
pnumber1b_fixB = list(range(2, 101))
for x in pnumber1b_fixB:
    for i in range(2, x):
        if x % i == 0:
            pnumber1b_fix.remove(x)
            break
print(pnumber1b_fix)

# 这个跟上一版本一致(双list法)
# 上一版本是只要有一个i为有效因数满足就不再试其他i,这个办法显然更笨重
# 区别就是如果不直接break掉i的迭代,那么设置一个检查如果x已经被除掉,那就继续尝试下一个i,直到所有i被迭代完才终止,然后试下一个x,直到x迭代完.
pnumber1b_fix2 = list(range(2, 101))
pnumber1b_fix2b = list(range(2, 101))
for x in pnumber1b_fix2b:
    for i in range(2, x):
        if x % i == 0:
            if x in pnumber1b_fix2:
                pnumber1b_fix2.remove(x)
    else:
        continue
print(pnumber1b_fix2)




# 这个版本就是利用all()来省去迭代i的for loop,使得过程更容易理解和控制: 必须是每一个i都能有余数(不为0,True)才可以满足条件.
pnumber2 = []
for x in range(2, 101):
    if all(x % i for i in range(2, x)):
        # 使用all(),等于简写break的第二重历遍.
        # all()要求只有x除以每一个i都能余数!=0,(=0就是False,!=0也就是必须为True),这个x才能符合质数条件.
        pnumber2.append(x)
print(pnumber2)

# 跟上一版本相比,这里用if not命令,如果不是质数,则跳过,否则就加入
pnumber2b = []
for x in range(2, 101):
    if not all(x % i for i in range(2, x)):
        continue         #使用contine因为此处是一重循环,如果break则会终止在第一个不是质数的x,也就是4.所以只会变成[2, 3]
    else:
        pnumber2b.append(x)
print(pnumber2b)




# 这个是反写, 首先创造一个list包含全部的2-100.
# 然后条件反转,如果能整除(余数=0, not all), 则不符合质数条件,从而删掉一个x
# 最终留下来的就是质数
pnumber3 = list(range(2, 101))
for x in range(2, 101):
    if not all(x % i for i in range(2, x)):
        pnumber3.remove(x)
print(pnumber3)

# 还是创造一个list包含全部的2-100.
# 但是跟上一版不同的是：如果是质数就保留，不然就去除(非质数)
pnumber3b = list(range(2, 101))
for x in range(2, 101):
    if all(x % i for i in range(2, x)):
        continue
    else:
        pnumber3b.remove(x)
print(pnumber3b)



# 投机取巧法,还是建立0-100的list,但是不直接从这里减去item, 而是再造一个list,把非质数集合在一起(append)
# 最后把两个list相减,得到质数list
to_remove = []
pnumber1b = list(range(2, 101))
for x in pnumber1b:
    for i in range(2, x):
        if x % i == 0:
            to_remove.append(x)
            break  # 注意这个break只是break第二重,i的循环
for r in to_remove:
    pnumber1b.remove(r)
print(pnumber1b)
