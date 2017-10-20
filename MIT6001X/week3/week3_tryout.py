# MIT class said that printing t1[1] should out put ('two',)
# with comma to indicate that it is a tuple
# but not any more in python 3.6.2
t1 = (1, 'two', 3, '4', 'five')
print(t1[1])

for i in range(0, 4):
    print(i)


print(min([5, 10]))
print(min(5, 10))



lettersGuessed = ['a', 'i', 'e', 'o']

j = 'x'.join(lettersGuessed)
print(j)
