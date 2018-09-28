# CS61A Exam Prep 05


# 1
def live(long):
    def prosper(spock, live):
        nonlocal long
        if len(long) == 1:
            return spock+1
        long[1] = live(long[0])
        long = long[1:]

        prosper(long[0], abs)
        return spock[0]+1

    prosper(long, lambda trek: trek-3)

print(live([1, 4]))

# 2
class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ', I work'

    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'

    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'

class Proletariat(Worker):
    greeting = 'Comrade'

    def work(self, other):
        other.greeting = self.greeting + ' ' + other.greeting
        other.work() # for revolution
        return other

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

print(Worker().work())  # >>> 'Sir, I work'
print(jack.work()[10:]) # >>> 'rk'

Proletariat().work(john)
# >>>
# Comrade Peon, I work

# print(john.elf.work(john))
# >>>
# Comrade Peon, I work
