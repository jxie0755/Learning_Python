# Simple learning on the concept of iterator and its relationship with generator in python
# STOF: https://stackoverflow.com/a/2776865/8435726


# iterator is a more general concept: any object whose class has a next method (__next__ in Python 3)
# and an __iter__ method that does return self.

# Every generator is an iterator, but not vice versa.

# Generator version
def squares(start, stop):
    for i in range(start, stop + 1):
        yield i * i

if __name__ == '__main__':
    print('Test generator:')
    generator_1 = squares(5, 9)
    for i in generator_1:
        print(i)


# Iterator version (not a real iterator)
# would take more code to build as a custom iterator:
class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current

if __name__ == '__main__':
    print('Test iterator:')
    iterator_1 = Squares(5, 9)
    for i in iterator_1:
        print(i)
