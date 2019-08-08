"""This is to learn python looping + condition"""

# while...else...
i = 0
while i != 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("finished") # not printed because loop break

# >>>
# 0
# 1
# 2
# 3


i = 0
while i != 5:
    print(i)
    i += 1
else:
    print("finished") # printed as loop end normally

# >>>
# 0
# 1
# 2
# 3
# 4
# finished


# for...else...

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("finished")  # not printed because loop break

# >>>
# 0
# 1
# 2
# 3

for i in range(5):
    print(i)
else:
    print("finished")  # printed as loop end normally

# >>>
# 0
# 1
# 2
# 3
# 4
# finished
