class Container(object):

    def __init__(self, length, width, depth):
        self.L = length
        self.W = width
        self.D = depth
        self.size = [self.L, self.W, self.D]


A = Container(5,6,7)
print(A.size)
# >>> [5, 6, 7]



