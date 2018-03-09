# Lecture 1: Function


# Numeric expressions
print()
print(2018)
print(2000 + 18)
print(1 - 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9))

# Call expressions
print()
print(max(3, 4.5))
print(pow(100, 2))
print(pow(2, 100))
print(max(1, -2, 3, -4))
print(max(pow(10, 2), pow(2, 10), 1010))

# Importing and arithmetic with call expressions
print()
from operator import add, mul
print(add(1, 2))
print(mul(4, 6))
print(mul(add(4, mul(4, 6)), add(3, 5)))
print(add(2, mul(9, mul(add(4, mul(4, 6)), add(3, 5)))))

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
print()
shakes = open('shakespeare.txt')
text = shakes.read().split()
print(len(text))
print(text[:25])
print(text.count('the'))
print(text.count('thou'))
print(text.count('you'))
print(text.count('forsooth'))
print(text.count(','))

# Sets
print()
words = set(text)
print(len(words))
print(max(words))
print(max(words, key=len))

# Reversals
print()
print('draw'[::-1])
print({w for w in words if w == w[::-1] and len(w)>4})
print({w for w in words if w[::-1] in words and len(w) == 4})
print({w for w in words if w[::-1] in words and len(w) > 6})
