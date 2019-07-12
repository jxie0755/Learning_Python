class Account:
    """An account has a balance and a holder.

    >>> a = Account("John")
    >>> a.holder
    "John"
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    "Insufficient funds"
    >>> a.balance
    10
    >>> a.interest
    0.02
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance

# Inheritance ("is a" relationship), subclass is used.
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount("Jack")
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        # Alternatively:
        return super().withdraw(amount + self.withdraw_fee)


# Composition ("has a" relationship), subclass is not used
class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account("John", 10)
    >>> jack = bank.open_account("Jack", 5, CheckingAccount)
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.6
    >>> jack.balance
    5.05
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type=Account):
        """Open an account_type for holder and deposit amount."""
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        """Pay interest to all accounts."""
        for account in self.accounts:
            account.deposit(account.balance * account.interest)


# Inheritance Example

class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5


print(C(2).n)     # >>> 4
print(a.z == C.z) # >>> True
print(a.z == b.z)  # >>> False
print(b.z) # >>> <__main__.B object at 0x0000023B5FE13438>

# Which evaluates to an integer?
# b.z            # >>> inst B(0)
# b.z.z          # >>> inst C(1)
# b.z.z.z        # >>> C(1).z == C.f(1) == 1
# b.z.z.z.z      # >>> 1.z == AttributeError
print(b.z.z.z) # >>> 1



# Multiple Inheritance

class SavingsAccount(Account):
    """A bank account that charges for deposits."""

    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """A bank account that charges for everything."""

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # A free dollar!

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]


# Another multiple inherintance check:
class A:
    def __init__(self, name):
        self.name = name
    def f(self):
        print("from A")


class B(A):
    def f(self):
        print("from B")


class C(A):
    def f(self):
        print("from C")


class D(B, C):
    pass

D(5).f()
# >>> from B      # why? becaue B is closer in the D()

class E(C, B):
    pass
E(5).f()
# >>> from C      # now C is closer.
