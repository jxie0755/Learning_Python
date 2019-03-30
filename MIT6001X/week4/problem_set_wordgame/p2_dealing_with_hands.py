def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for i in word:
        new_hand[i] -= 1
    return new_hand

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'
print(updateHand(hand, word))
