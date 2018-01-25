def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result = []
    for k, v in aDict.items():
        if v == target:
            result.append(k)
        result = sorted(result)
    return result



print(keysWithValue({1: 0, 2: 2, 3: 2, 4: 3, 6: 2, 9: 3, 10: 1}, 2))
