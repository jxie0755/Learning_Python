# CS61A Lecture 13 Mutable Values

a = [1,2,3]
b = list(a)
print(b)  # >>> [1,2,3]
b[0] = a
print(b)  # >>> [[1, 2, 3], 2, 3]



def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw2(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        # nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        return balance - amount
    return withdraw

if __name__ == '__main__':

    hundred = make_withdraw(100)
    print(hundred(25)) # >>> 75
    print(hundred(15)) # >>> 60  balance changed from previous operation

    hundred = make_withdraw2(100)
    print(hundred(25)) # >>> 75
    print(hundred(15)) # >>> 85 balance not changed, still calculate from 100 everytime

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)
b(3) + b(4)
