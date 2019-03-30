# Function without modifying the list:

def movinglist(listU, listC):
    while listU:
        listC.append(listU.pop(0))
    else:
        print('in-func U:', listU)
        print('in-func C:', listC)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

movinglist(unconfirmed_users[:], confirmed_users[:])

print('original U:', unconfirmed_users)
print('original C:', confirmed_users)
