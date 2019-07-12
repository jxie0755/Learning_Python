# this provides a sample of how to restrict input by using re module and a while loop
# in this case it only allows to input "0" and "1"

import re

while True:
    target = input("please input a binary number:")
    if not re.match("^[0-1]*$", target):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        break
        
