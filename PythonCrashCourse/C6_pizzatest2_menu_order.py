# continuously input and form a list out of it
# has to be able to quit the input

# base on above to create notification if input something wrong

price_list = {"beef": 2.99, "steak": 3.99, "chicken": 1.99, "pepperoni": 1.99, "sausage": 1.99, "done": 0}  # add done in this dictionary to avoid conflict, not the best method

input_list = []
max_length_list = 5

while len(input_list) < max_length_list:
    input_item = input("please input:")
    if input_item not in price_list:
        print("we don\"t have this')
        continue
    if input_item in price_list:
        input_list.append(input_item)
    if "done" in input_list:
        break
input_list.remove("done")

print("your input:", end=" ")
print(input_list)
