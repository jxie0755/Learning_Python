def longest_palindromic(text):
    result = []
    n, m = 0, 0
    index = len(text)
    while n < index:
        for m in range(0, n + 1):
            result.append(text[m:index - n + m])
        else:
            n += 1
    print(result)
    for i in result:
        if i == i[::-1]:
            return i
    else:
        return None


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    print('done')

