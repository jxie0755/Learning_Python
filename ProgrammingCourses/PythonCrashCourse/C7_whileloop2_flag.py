# this is to show how to use a flag

active = True # set a flag

while active:
    message = input(prompt)

    if message == "quit":
        active = False

    else:
        print(message)
