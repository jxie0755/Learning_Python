# From MIT 6.00.1X week 2

# Move a pile of disks from A to B
# bigger disk must under smaller disk

# Recursive thinking:
# if move a stack of n disks, what is the solution for small stack?
# move a slightly smaller stack to the spare, move the bottom to target place, then move the stack to the target


def printMove(A="A", B="B"):
    print("move from " + str(A) + " --> " + str(B))

def Towers(n, A="A", B="B", spare="S"):
    global move
    if n == 1:
        printMove(A, B)
        move += 1

    else:
        Towers(n-1, A, spare, B)
        Towers(1, A, B, spare)
        Towers(n-1, spare, B, A)

move = 0
Towers(4)
print("it will take:", move, "moves")

# 另解
def hanoi(n, a="1", s="2", b="3"):
    global move
    if n == 1:
        print("move", a, "-->", b)
        move += 1
    else:
        hanoi(n-1, a, b, s)
        print("move", a, "-->", b)
        move += 1
        hanoi(n-1, s, a, b)

move = 0
print(hanoi(3))
print("it will take:", move, "moves")
