# CS61A Lecture 14 Mutable Functions

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        # nonlocal is to change the variable in mother frame from sub-frame.

        if amount > balance: # this is ok, because it is not value-binding, so it look a frame above
            return "Insufficient funds"

        balance = balance - amount  # re-bind value of balance
        # without non-local, this value binding action will look for balance in this frame, and it won't find any.

        return balance
    return withdraw

if __name__ == "__main__":
    w = make_withdraw(100)
    print(w(10))


def make_withdraw_list(balance):
    b = [balance] # put balance in a list

    def withdraw(amount):
        if amount > b[0]:
            return "Insufficient funds"
        b[0] = b[0] - amount
        # b can change because it is a mutable data value.
        # it is not a value-binding, because we are merely referring to b, not changing what it is bound to.

        return b[0]

    return withdraw



# Multiple Mutable Function
def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
if __name__ == "__main__":
    a = f(1)  # x = 1, but then x = 4
    b = a(2)  # y = 2
    print(b(3) + b(4)) # z = 3 and z = 4
    # >>>
    # it should be:
    # b(3): (4 + 1) + 2 + 3 = 10
    # b(4): (4 + 1) + 2 + 4 = 11
    # together is 21
    # actually 22, because x in b(4) is affected by b(3), so that it is no longer 4 + 1 but (4 + 1) + 1

    # but replace b(3) with 10, it will end up at 21 instead of 22.
    # therefore this program does not have referential transparency!!


def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk - ley
        return [berk, cal(berk)]
    return cal(2)

print(oski(abs))
# >>>
# [2, [3, 1]]
# bear can change during the process.
