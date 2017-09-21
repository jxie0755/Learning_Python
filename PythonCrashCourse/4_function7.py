# Don't know how many arguments there will be (arbitrary arguments)
# 不确定参数数目

def make_pizza(*toppings):
  print('toppings are:', toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushroom', 'pineapple')

#改变输出为string
def make_pizza(*toppings):
    print('\ntoppings are:')
    for i in toppings:
        print(i, end=' ')

make_pizza('pepperoni')
make_pizza('pepperoni', 'mushroom', 'pineapple')
# 注意arbitrary argument最后输出是一个tuple元组
