# Based on V1
# Target: calculate the final price

# Menu list
base_list = {"thin": 7.99, "regular": 8.99, "pan": 9.99, "stuffed": 10.99}
cheese_list = {"light": 0.99, "regular": 1.99, "extra": 2.99}
vegi_list = {"green pepper": 0.49, "onion": 0.49, "olive": 0.49, "tomato": 1.99, "spinach": 0.99, "mushroom": 0.99}
meat_list = {"beef": 2.99, "steak": 3.99, "chicken": 1.99, "pepperoni": 1.99, "sausage": 1.99}
# Merge all the menu into one
total_list = {**base_list, **cheese_list, **vegi_list, **meat_list}

# Welcome customer
print("Welcome to Papa Denis pizza!\n")
customer_name = str(input("please enter your name for the order:"))
print("Hello! ", customer_name, "! You can order whenever you are ready:)\n")

# when customer is ready, take him to the pizza base options
print("Our pizza types are:")
for base, baseprice in base_list.items():
    print("{}: ${}".format(base, baseprice))
base_order = [str(input("please choose a base for your pizza:"))]

# show the cheese list and have customer order the cheese
print("\nPlease how much cheese do you want in the base:")
for cheese, cheeseprice in cheese_list.items():
    print("{}: ${}".format(cheese, cheeseprice))
cheese_order = [str(input("please choose the cheese for your pizza:"))]

# Summarize the order so far
print("\nSo far, you ordered a", base_order, "pizza with", cheese_order, "amount of cheese.")

# show the meat list and have customer order the meat
print("\nPlease take a look at our choice of meat:")
for meat, meatprice in meat_list.items():
    print("{}: ${}".format(meat, meatprice))

meat_order = []
max_length_list = 5
while len(meat_order) < max_length_list:
    meat_choice = input("\nEnter your meat option. You can choose multiple\nType \"done\" when finish:")
    meat_order.append(meat_choice)
    if "done" in meat_order:
        break
meat_order.remove("done")

print("\nYou ordered:")
for meat in meat_order:
    print(meat, end=", ")
print(" good choice!")

# show the vegetable list and have customer order the vegetable
print("\nWe also have a lot of options for vegetables:")
for vegi, vegiprice in vegi_list.items():
    print("{}: ${}".format(vegi, vegiprice))

vegi_order = []
max_length_list = 6
while len(vegi_order) < max_length_list:
    vegi_choice = input("\nEnter your meat option. You can choose multiple\nType \"done\" when you finish:")
    vegi_order.append(vegi_choice)
    if "done" in vegi_order:
        break
vegi_order.remove("done")

print("\nYou ordered:")
for vegi in vegi_order:
    print(vegi, end=", ")
print(" very healthy!\n")

print("Thank you, " + customer_name + "!" " To summarize,\nYou have ordered:", end=" ")
print("a", base_order[0], "pizza with", cheese_order[0], "cheese." )
topping_order = meat_order + vegi_order
print("Your choice of toppings are:", end=" ")
for item in topping_order:
    print(item, end=", ")

# Merge all the orders into one list
final_order = base_order + cheese_order + meat_order + vegi_order

# Calculate the total price by creating a new empty list, and put the price of items in final order into it.
final_price = []
for item in final_order:
    if item in total_list:
        final_price.append(total_list[item])
final_total_price = sum(final_price)

# print the final price and end this order.
print("\nYour total payment will be: $" + str(round(final_total_price, 2)))
print("Enjoy your meal!")
