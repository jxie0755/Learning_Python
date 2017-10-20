letterGuessed = ['a', 'g', 'x', 'y', 'z']

letter_list = ['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']

available_letters = ''
for i in letter_list:
    if i not in letterGuessed:
        available_letters += i

print(available_letters)
