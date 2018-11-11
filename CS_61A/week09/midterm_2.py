# CS61A spring 2018 midterm exam 1

# Q1 Buggy Quidditch

# If an error occurs, write Error, but include all output displayed before the error.
# To display a function value, write Function.
# If an expression would take forever to evaluate, write Forever.

class Ball:
    points = 0
    time = lambda: 'Draco'

    def score(self, who):
        print(who, self.points)

    def __str__(self):
        return 'Magic'

class Snitch(Ball):
    points = 100
    time = lambda: 'Harry'

    def __init__(self):
        self.points = self.points + 50

    def score(self, p):
        if not time():
            print(Ball().score(p))
        else:
            Ball.score(self, p)

def chase(r):
    r.time = Snitch.time
    r.points += 1
    quaffle.points += 10
    print(r().points)

quaffle = Ball()
quaffle.points = 10
chasing = quaffle.score
time = lambda: Ball.points
malfoy = lambda: Ball.time()

print(Snitch().points)


print(chase(quaffle))


print(Snitch().score('Seeker'))


print(chase(Ball))


print(Snitch().score(malfoy()))

