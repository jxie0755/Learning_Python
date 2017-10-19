# song lyrics analysis
# how many times a word appears in a lyric of a song

# first create a frequency dictionary mapping the str:int
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# find the word that occurs the most


# find the word that occured at least x times


