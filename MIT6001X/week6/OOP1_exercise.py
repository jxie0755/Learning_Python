class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
paris_clock.print_time()


class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8

w2 = Wild(X, Y)
print(w2.getX())
print(w2.getY())

w3 = Wild(17, 18)
print(w3.getX())
print(w3.getY())

w4 = Wild(X, 18)
print(w4.getX())
print(w4.getY())

X = w4.getX() + w3.getX() + w2.getX()
print(X)

print(w4.getX())  # 记住这里class内部数据被封装,不受外部干扰

Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)

print(w2.getY())  # 同上
