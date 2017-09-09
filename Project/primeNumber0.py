pnumber = []
for x in range(2, 101):
    for i in range(2, x):
        if all(x % i) == True:
            pnumber.append(x)
print(pnumber)


