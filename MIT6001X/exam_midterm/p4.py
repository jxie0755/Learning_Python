def dotProduct(listA, listB):
    ""'
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    ""'
    index = len(listA)
    result = 0
    for i in range(0, index):
        result += listA[i]*listB[i]
    return result

listA = [1, 2, 3]
listB = [4, 5, 6]
print(dotProduct(listA, listB))
