number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')

elif guess < number:
    print('No, it is a little higher than that')

else:
    print('No, it is a little lower than that')

print('Done')
print(__name__)
# 只能猜一次，需要不停的Run这个代码一次一次实验。
