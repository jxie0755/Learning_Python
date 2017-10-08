# guess a secret number that you have in your mind

low = 0
high = 100
guess = int((low + high) / 2)

while True:
    ans = input("Is your secret number " + str(guess) + ":\n" + "Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans != 'h' and ans != 'l' and ans != 'c':
        print("Sorry, I did not understand your input.")
        continue
    if ans == 'h':
        high = guess
    if ans == 'l':
        low = guess
    if ans == 'c':
        print("Game over. Your secret number was:", guess)
        break
    guess = int((low + high) / 2)