import re

while True:
    input_str = input("Please provide some info: ")
    if not re.match("^[0-1]*$", input_str):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        print("ok, this is good")
        break
