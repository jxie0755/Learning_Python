# Input a list

# MAP creates iterator that will be consumed by a list() command.
# Without the list() to save it, the iterator can only be used once.
numArray = list(map(int, input('input and output numbers:').split()))
numArray2 = list(input('input and output strings:').split())

# Input should use ' 'space to separate, not ','comma
print('numArray is', numArray)
print('numArray2 is', numArray2)

sum_integer = 0
# Write the logic to add these numbers here
for number in numArray:
    sum_integer += number*number

# Print the sum
print('sum is:', sum_integer)
