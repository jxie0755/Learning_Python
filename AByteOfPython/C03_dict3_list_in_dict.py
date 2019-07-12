# LIST IN DICT
# Make pizza order, two type data, crust type and toppings

pizza = {"crust": "thick",
         "toppings": ["mushroom", "peperoni", "extra cheese"]
         }      # 直接把dict中的单个value换成一个list

print("You ordered a ", pizza["crust"], "-crust pizza", "with the following toppings:")
for topping in pizza["toppings"]:   # pizza["toppings"] 成了这个list的名字
    print("\t", topping)
