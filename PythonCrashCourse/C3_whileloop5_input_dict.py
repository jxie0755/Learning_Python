# Filling a dict with user input

menu = {}
running = True # Flag

while running:
    key0 = input('please enter a key, enter quit to exit:')
    if key0 == 'quit':
        break     # 此处如果使用running = False,还需要输入完value,添加quit到menu,再次运行whileloop才会终止.
                  # 所以应当使用break来立刻终止
                  # flag应该使用在好几个if条件中,当一个if完成就终止,而不是这种只有一个if,在半路就需要终止的情形
    value0 = int(input('please enter a value for the key:'))  # int可以输入数字
    menu[key0] = value0

print(menu)
