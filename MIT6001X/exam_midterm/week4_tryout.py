dictA = {"a": 1, "b": 2, "c": 3, "d": 4,
             "e": 5, "f": 6, "g": 7, "h": 8,
             "i": 9, "j": 10, "k": 11, "l": 12,
             "m": 13, "n": 14, "o": 15, "p": 16,
             "q": 17, "r": 18, "s": 19, "t": 20,
             "u": 21, "v": 22, "w": 23, "x": 24,
             "y": 25, "z": 26}

word = "add"
word = word.lower()
letter_score_list = []
letter_index = -1
for i in word:
    letter_index += 1
    letter_score = dictA[i] * letter_index
    letter_score_list.append(letter_score)
print(letter_score_list)



l = [1, 3, 2, 8]
l.remove(3)
print(l)
