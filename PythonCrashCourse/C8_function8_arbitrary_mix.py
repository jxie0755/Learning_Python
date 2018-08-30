# Mixing arbitrary argument with positional arguments
# asterisk for arbitrary tuple

def make_pizza(size, *toppings): # AA后置
    print('\nMaking a ' + str(size) + '-inch pizza with following toppings:')
    for topping in toppings:
        print(topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
