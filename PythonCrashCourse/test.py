
LIST = {'A4': 20, 'A6': 25, 'A8': 30}

for make, model in LIST.items():
    Maker = LIST.get(make)

print(Maker)
