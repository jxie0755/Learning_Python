pnumber1b = list(range(2, 101))
pnumber1a = list(range(2, 101))
for x in pnumber1b:
    for i in range(2, x):
        if x % i == 0:
            if x in pnumber1a:
                pnumber1a.remove(x)
    else:
        continue
print(pnumber1a)
