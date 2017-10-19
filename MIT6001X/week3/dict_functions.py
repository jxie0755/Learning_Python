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
lyc = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'j', 'x']

print(lyrics_to_frequencies(lyc))
fq = lyrics_to_frequencies(lyc)

# find the word that occured at least x times
def most_common_words(freqs):

    # 巧妙提取出现次数最多的value
    values = freqs.values()
    best = max(values)

    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

result = most_common_words(fq)
print(result)

# find the words occurred more often than a number
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)    # 不断计算最高频的词
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])    # 如果这个最高频率超过目标频率,则记录,然后删除,然后再次计算下一个最高频率
        else:
            done = True
    return result

# 也可以直接对lyc动手得到lyrics_to_frequency,会是另一种写法,此处略过

print(words_often(fq, 3))
