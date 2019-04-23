def f(lst, dt):
    result = [[]]
    for d in dt:
        if d in lst:
            # result = [x + y for x in result for y in [[d] * n for n in range(1, dt[d] + 1)]]
            # 等同于以下:

            new_result = []
            for x in result:
                for y in [[d] * n for n in range(1, dt[d] + 1)]:
                    new_result.append(x + y)
            result = new_result

    return result


print(f(['A','B'], {'A':2, 'B':2, 'C': 2}))
# >>> [['A', 'B'], ['A', 'B', 'B'], ['A', 'A', 'B'], ['A', 'A', 'B', 'B']]


