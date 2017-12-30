class SuperC():
    def __init__(self, a, b, c, d='X'):
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.E = 'what?'

class SubC(SuperC):
    def __init__(self, a, b, c, f):
        super().__init__(a, b, c)
        self.F = f

sup = SuperC(1, 2, 3)
print(sup.A)  # >>> 1
print(sup.B)  # >>> 2
print(sup.C)  # >>> 3
print(sup.D)  # >>> X
print(sup.E)  # what?

sub1 = SubC(5, 6, 7, 'Y')
print(sub1.A)  # >>> 5  # Ａ, B, C被继承而且数值被刷新
print(sub1.B)  # >>> 6
print(sub1.C)  # >>> 7
print(sub1.D)  # >>> X  # 此处虽然super()没有指定,但是由于SuperC中有默认值,所以仍然被继承
print(sub1.E)  # >>> what?
print(sub1.F)  # >>> Y

