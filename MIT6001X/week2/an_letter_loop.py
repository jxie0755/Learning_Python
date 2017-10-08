an_letters = 'aefhilmnorsxAEFHILMNORSX'

word = input('Give me a word:')
times = int(input('Times to repeat:'))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + ": " + char + "!")
    else:
        print("Give me a " + char + ": " + char + "!")
    i += 1
print("What does that spell?")
for n in range(times):
    print(word + " !!!")