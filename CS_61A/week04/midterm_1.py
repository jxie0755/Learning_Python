# CS61A spring 2018 midterm exam 1

# --------------------------------------------------------------------
# Q1 Frame of Thrones
# --------------------------------------------------------------------
from operator import add, sub
def winterfell(a, b):
    a
    b
    return b(a+1, b(a))

da, ny = 20, 18

while da > ny:
    da = ny
    da, ny = ny + 1, da + 3

def tar(gar, yen):
    if print(yen):
        print(yen + 1)
    return gar(yen)

def st(ar, k=None):
    return lambda a, y: ar(y, a)

night = st(sub)
king = st(st(pow))

def jon(sn, ow):
    print(ow)
    jon = sn(ow)
    print(ow)
    return jon

def snow(ow):
    def tarly(snow):
        return ow + snow
    ow += 2
    return tarly

# What would python show:
print((print(2) or 3) // (0 or 1))
# >>>
# 2
# 3
print(winterfell(2, print))
# >>>
# 2
# 3 None
# None
print(ny)
# >>>
# 21
print(tar(lambda x: x-7, 8))
# >>>
# 8 (from if condition)
# 1
print(night(king(2, 3), 4))
# >>>
# -4
print(jon(snow(5), 2))
# >>>
# 2
# 2
# 9


# --------------------------------------------------------------------
# Q2 Stranger Frames
# --------------------------------------------------------------------
def lucas(mike):
    return will

def dustin(lucas):
    will = 1
    def dustin(mike):
        will = 2
        return lucas
    return lambda mad: dustin(3)(will)

will = 5 + 6
lucas = dustin(lucas)
print(lucas(max))
# >>>
# 11
