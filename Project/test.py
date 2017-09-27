Dict = {'thin': 7.99, 'regular': 8.99, 'pan': 9.99, 'stuffed': 10.99}

while True:
    order = input('please input:')
    if order in Dict.keys():
        print('in')
        break
    if order not in Dict.keys():
        print('not in')
        continue