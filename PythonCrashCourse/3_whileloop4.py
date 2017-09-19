# Moving items from one list to another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while len(unconfirmed_users) > 0:
    confirmed_users.append(unconfirmed_users[0])
    del unconfirmed_users[0]

print(unconfirmed_users)
print(confirmed_users)

# 也可以用pop命令, 可以省一行命令

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while len(unconfirmed_users) > 0:
    confirmed_users.append(unconfirmed_users.pop(0))

print(unconfirmed_users)
print(confirmed_users)
