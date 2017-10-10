x = 0.375
p = 0
int_x = x * 2 ** p

while int_x % 1 != 0:
    p += 1
    int_x *= 2

int_x = int(int_x)

