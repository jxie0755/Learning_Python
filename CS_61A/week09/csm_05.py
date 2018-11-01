# CS61A CSM 05: Linked Lists and Midterm Review



# Linked list

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

# if link is Link.empty:
#     print('This linked list is empty!')


# Q1 What will Python output?
a = Link(1, Link(2, Link(3)))
print(a.first)
# >>> 1

a.first = 5
print(a.first)
# >>> 5

print(a.rest.first)
# >>> 2

# print(a.rest.rest.rest.rest.first)
# >>> error

a.rest.rest.rest = a
print(a.rest.rest.rest.rest.first)
# >>> 2


# Q2
