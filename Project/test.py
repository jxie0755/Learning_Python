pnumber1b_fix2 = list(range(2, 101))
pnumber1b_fix2b = list(range(2, 101))
for x in pnumber1b_fix2b:
    for i in range(2, x):
        if x % i == 0:
            if x in pnumber1b_fix2:
                pnumber1b_fix2.remove(x)
            else:
                continue
        else:
            break
print(pnumber1b_fix2)
