# this is to show how to use quit to quit input

prompt = 'input anythings, input quit to exit'
message = ''       # a way to setup an empty string
while message != 'quit':
    message = input(prompt)
    print(message)
