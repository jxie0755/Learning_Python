# if in the order, customer has more than one purchase of the same item:
# this script is not automatic enough, has to be input by user and customized to any order

DictA = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
order = ['B', 'D', 'F']
nB = 2
nD = 3
nF = 2

price = []
for item in DictA:
    if item in order:
        price.append(DictA[item])
print(price[0] * nB + price[1] * nD + price[2] * nF)
