"""
此代码为a byte of python 中增强版, 附加1-100提示(使用continue), 和22, 24错误导致break引用
Guess a number
"""

number = 23
running = True

while running:
    guess = int(input("please guess the number that I have in mind : "))
    print("\n")
    if guess == 23:
        print("Congratulations! You are correct!")
        running = False
    if guess > 100:
        print("Please pick a number between 1-100")
        continue
    if guess == 24:
        print("Boom!! It's very close, but your chance is over!")
        break
    if guess == 22:
        print("Boom!! It's very close, but your chance is over!")
        break
    if guess > 23:
        print("It is lower than that")
    if guess < 23:
        print("it is higher than that")

else:
    print("Good work!\n")

print("Program over")
