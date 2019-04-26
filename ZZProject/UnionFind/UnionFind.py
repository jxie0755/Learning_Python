### Classical Union find data structure

class UnionFind(object):

    def __init__(self, size):
        self.id = list(range(size))

    def root(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rt_p = self.root(p)
        rt_q = self.root(q)
        if rt_p != rt_q:
            self.id[rt_p] = rt_q




if __name__ == '__main__':
    Q1 = UnionFind(10)
    Q1.union(4, 3)
    Q1.union(3, 8)
    Q1.union(6, 5)
    Q1.union(9, 4)
    Q1.union(2, 1)
    Q1.union(5, 0)
    Q1.union(7, 2)
    Q1.union(6, 1)
    Q1.union(7, 3)
    print(Q1.id)
    # >>>  [1, 8, 1, 8, 3, 0, 5, 1, 8, 8]



class UnionFindWeighted(object):

    def __init__(self, size):
        self.id = list(range(size))
        self.sz = [1] * size           # track the size of each tree (only on the root)
        self.mx = list(range(size))    # track the maximum element in this tree (only on the root)


    def root(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)


    def find(self, p):
        """returns the largest element in the connected component containing p"""
        return self.mx[self.root(p)]

    def union(self, p, q):
        rt_p = self.root(p)
        rt_q = self.root(q)

        if rt_p != rt_q:
            if self.sz[q] <= self.sz[p]:
                self.id[rt_q] = rt_p       # assign the new root to the bigger tree
                self.sz[rt_p] += self.sz[rt_q]  # update the size of the new root
                if self.mx[rt_q] > self.mx[rt_p]:
                    self.mx[rt_p] = self.mx[rt_q]
            else:
                self.id[rt_p] = rt_q
                self.sz[rt_q] += self.sz[rt_p]
                if self.mx[rt_p] > self.mx[rt_q]:
                    self.mx[rt_q] = self.mx[rt_p]

if __name__ == '__main__':
    Q2 = UnionFindWeighted(10)
    Q2.union(4, 3)
    Q2.union(3, 8)
    Q2.union(6, 5)
    Q2.union(9, 4)
    Q2.union(2, 1)
    Q2.union(5, 0)
    Q2.union(7, 2)
    Q2.union(6, 1)

    # Q2.union(7, 3)

    print(Q2.id)
    # >>> [6, 2, 6, 4, 4, 6, 6, 2, 4, 4]

    print(Q2.find(1)) # >>> 7



class UnionFindWeightedPathCompressed(object):

    def __init__(self, size):
        self.id = list(range(size))
        self.sz = [1] * size           # track the size of each tree (only on the root)
        self.mx = list(range(size))    # track the maximum element in this tree (only on the root)


    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]  # 在找root的时候顺便,把节点指向父节点的父节点(跳一级)
                                              # 不怕溢出, 因为root的父节点还是root本身
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)


    def find(self, p):
        """returns the largest element in the connected component containing p"""
        return self.mx[self.root(p)]

    def union(self, p, q):
        rt_p = self.root(p)
        rt_q = self.root(q)

        if rt_p != rt_q:
            if self.sz[q] <= self.sz[p]:
                self.id[rt_q] = rt_p       # assign the new root to the bigger tree
                self.sz[rt_p] += self.sz[rt_q]  # update the size of the new root
                if self.mx[rt_q] > self.mx[rt_p]:
                    self.mx[rt_p] = self.mx[rt_q]
            else:
                self.id[rt_p] = rt_q
                self.sz[rt_q] += self.sz[rt_p]
                if self.mx[rt_p] > self.mx[rt_q]:
                    self.mx[rt_q] = self.mx[rt_p]

if __name__ == '__main__':
    Q3 = UnionFindWeightedPathCompressed(10)
    Q3.union(4, 3)
    Q3.union(3, 8)
    Q3.union(6, 5)
    Q3.union(9, 4)
    Q3.union(2, 1)
    Q3.union(5, 0)
    Q3.union(7, 2)
    Q3.union(6, 1)
    # Q3.union(7, 3)

    print(Q3.id)
    # >>> [6, 2, 6, 4, 4, 6, 6, 2, 4, 4]

    print(Q2.find(1))  # >>> 7
