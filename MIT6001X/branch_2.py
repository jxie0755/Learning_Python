num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

print()

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

print()
i = 2
while True:
    if i > 10:
        break
    print(i)
    i += 2

print()

i = 10
print('Hello!')
while True:
    if i < 2:
        break
    print(i)
    i -= 2

print()
end = 6
total = 0
current = 1
while current <= end:
    total += current
    current += 1

print(total)

print()
for i in range(11, 2):
    if i % 2 == 0:
        print(i)
print("Goodbye!")


print()
print("Hello!")
for j in range(0, 9):
    if j % 2 == 0:
        i = 10 - j
        print(i)

print()
end = 6
total = 0
for i in range(1, end+1):
    total += i
print(total)