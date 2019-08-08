"""From Yeluo to solve N-Queens"""

def diagonal(column):
    n = len(column)
    for i in range(0,n):
        for j in range(i+1,n):
            if abs(column[j]-column[i]) == abs(j-i):
                return True
    return False

def output(column,counter):
    n = len(column)
    print("=================")
    print(counter)
    for i in range(0,n):
        for j in range(0,n):
            if column[i] == j:
                print("O",end=" ")
            else:
                print("X",end=" ")
        print(end="\n")

def possible_remove(column,n,i):
    possible = [x for x in range(0,n)]
    for x in range(0,n):
        if column[x] in possible:
            possible.remove(column[x])
    for x in range(0,column[i]+1):
         if x in possible:
            possible.remove(x)
    return possible

def queens(n):
    column = [-1]*n
    result_counter = 0
    i = 0

    while i>=0:
        if i == n:
            if not diagonal(column):
                result_counter += 1
                output(column,result_counter)
            i -= 1
            continue
        possible = possible_remove(column,n,i)
        if column[i] == n-1 or len(possible) == 0:
            column[i] = -1
            i -= 1
            continue
        if i < n and i >=0:
            column[i] = possible[0]
            i += 1
    return result_counter

if __name__ == "__main__":
    print(queens(8))
    pass
