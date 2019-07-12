varA = -5
varB = "sadfadf"

print(type(varA))


if type(varA) and type(varB) == int:
    if varA > varB:
        print("bigger")
    if varA == varB:
        print("equal")
    if int(varA) < int(varB):
        print("string involved")
else:
    print("string involved")