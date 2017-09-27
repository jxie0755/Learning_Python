input = input('input:')
with open('USN_list.txt') as f:
    lines = f.readlines()
print(lines)
if input + '\n' in lines:
    print('in')
else:
    print('not in')