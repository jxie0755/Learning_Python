a = [2,3,4,2, 1, 3,5,4,3,2]


min_price, max_price = float('inf'), -float('inf')
i = 0
while i != len(a):
    current = a[i]
    if current < min_price:
        min_price = current
    if current > max_price:
        max_price = current
    i += 1

print(min_price, max_price)