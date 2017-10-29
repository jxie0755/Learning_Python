def checkio(data):
    result = []
    for i in data:
        if data.count(i) > 1:
            result.append(i)
    print(result)

data = [1, 2, 3, 1, 3]
checkio(data)
