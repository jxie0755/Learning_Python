# Moving items from one list to another

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while len(unconfirmed_users) > 0:
    confirmed_users.append(unconfirmed_users[0])
    del unconfirmed_users[0]

print(unconfirmed_users)
print(confirmed_users)

# 也可以用pop命令, 可以省一行命令

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while len(unconfirmed_users) > 0:
    confirmed_users.append(unconfirmed_users.pop(0))

print(unconfirmed_users)
print(confirmed_users)

# 函数式
def movinglist(listU, listC):
    while listU: # 等同于while len(listU) > 0:
      listC.append(listU.pop(0))

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

movinglist(unconfirmed_users, confirmed_users)
print("U:", unconfirmed_users)
print("C:", confirmed_users)
