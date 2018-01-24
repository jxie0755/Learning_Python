# this is to create a template using the timeit module
# the codes can be used for algorithm test by calculating the time

def f(x):  # power function
    return x**2

if __name__ == '__main__':
    from timeit import repeat
    result = repeat('f(3)', setup='from __main__ import f', repeat=3, number=1000000)
    print(round(sum(result)/len(result), 4))
