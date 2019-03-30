# Use a function with a while loop
# function is in an infinite loop

def format_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    # 这里将input形成的f_name和l_name指定为function中的first_name和last_name
    f_name = input('First name:')
    l_name = input('last name:')
    name = format_name(f_name, l_name)
    print('\nHello,', name, '!')
