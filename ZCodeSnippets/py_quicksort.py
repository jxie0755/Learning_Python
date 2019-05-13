# This is to learn Quicksort in python from Algorithm Part 1 Lecture 06


import random

class Quicksort:
    def exch(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def knuth_shuffle(self, array):
        for i in range(len(array)):
            r = random.randrange(i + 1)
            self.exch(array, i, r)

    ### This is the trickiest part, very easy to make mistakes
    def partition(self, array, lo, hi):

        i = lo
        j = hi + 1
        keyelem = array[lo]

        while True:

            while True:
                i += 1
                if array[i] >= keyelem:
                    break
                if i == hi:
                    break

            while True:
                j -= 1
                if keyelem >= array[j]:
                    break
                if j == lo:
                    break

            if i >= j:
                break

            self.exch(array, i, j)

        self.exch(array, lo, j)
        return j


    def raw_sort(self, array, lo, hi):
        if hi > lo:
            print('lo', lo, 'hi', hi)
            j = self.partition(array, lo, hi)
            print('j', j)
            print(array)
            self.raw_sort(array, lo, j - 1)
            self.raw_sort(array, j + 1, hi)

    def sort(self, array):
        self.knuth_shuffle(array)
        self.raw_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    a = ['K', 'R', 'A', 'T', 'E', 'L', 'E', 'P', 'U', 'I', 'M', 'Q', 'C', 'X', 'O', 'S']
    Quicksort().sort(a)


    b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Quicksort().sort(b)

