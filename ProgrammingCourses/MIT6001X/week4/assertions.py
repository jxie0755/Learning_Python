def avg(grades):
    assert not len(grades) == 0, "no grades data"
    return sum(grades)/len(grades)

g1 = [95, 98, 100]
g2 = []
print(avg(g1))
print(avg(g2))
