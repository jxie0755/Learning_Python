def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    newhand = hand.copy()
    if word not in wordList:
        return False
    else:
        for i in word:
            if i not in newhand.keys():
                return False
            else:
                newhand[i] -= 1
        for v in newhand.values():
            if v < 0:
                return False
            else:
                return True


hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'
