def get_ratios(L1, L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float("NaN"))  # NaN = Not a Number
        except:
            raise ValueError("get_ratios called with bad arg")
    return ratios

a = [1, 2, 3]
b = [2, 3, 4]
c = [2, 0, 5]
d = [2, 3]
print(get_ratios(a, b))
print(get_ratios(a, c))
print(get_ratios(a, d))
