num = 10
for num in range(5):
    print(num)
print(num)

print()

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

print(2/2)

print()

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
print()

for letter in 'hola':
    print(letter)

print()

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

print()

greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

print()

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))