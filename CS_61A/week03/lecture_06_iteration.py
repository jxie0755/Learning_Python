# CS61A Lecture 06 Iteration


# A fibonacci Sequence using while loop
def fib(n):
    k, kth, difference = 0, 0, 1
    while k < n:
        kth, difference = kth + difference, kth
        k += 1
    return kth

if __name__ == '__main__':
    assert fib(0) == 0, 'regular'
    assert fib(8) == 21, '8th'


# Return
def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)


if __name__ == '__main__':
    print(search(is_three)) # >>> 3
    print(search(positive)) # >>> 11, as 11^2 = 121 - 100 = 21 as the first positive value
    sqrt = inverse(square)
    print(square(16)) # >>> 256
    print(sqrt(256)) # >>> 16


# Self reference
def print_all(x):
    print(x)
    return print_all

def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum


if __name__ == '__main__':
    print_all(1)(3)(5)   # keep adding argument as it return a function of itself
    # >>>
    # 1
    # 3
    # 5

    print_sum(1)(3)(5)
    # >>>
    # 1
    # 4
    # 9

# generate a wave file, (no compression file format)
# in this case, we generate a triangle wave

# Example: Sound

from wave import open
from struct import Struct
from math import floor

frame_rate = 11025


def encode(x):
    """Encode float x between -1 and 1 as two bytes.
    (See https://docs.python.org/3/library/struct.html)
    """
    i = int(16384 * x)
    return Struct('h').pack(i)


def play(sampler, name='/Users/Jxie0755/Documents/DXcodings/Learning_Python/CS_61A/week03/mario.wav', seconds=2):
    """Write the output of a sampler function as a wav file.
    (See https://docs.python.org/3/library/wave.html)
    """
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t = t + 1
    out.close()


def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave

    return sampler


c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

play(tri(e_freq))


def note(f, start, end, fade=.01):
    """Play f for a fixed duration."""

    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)

    return sampler


play(note(tri(e_freq), 1, 1.5))


def both(f, g):
    return lambda t: f(t) + g(t)


c = tri(c_freq)
e = tri(e_freq)
g = tri(g_freq)
low_g = tri(g_freq / 2)

play(both(note(e, 0, 1 / 8), note(low_g, 1 / 8, 3 / 8)))

play(both(note(c, 0, 1), both(note(e, 0, 1), note(g, 0, 1))))


def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1 / 8)
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(c, z, z + 1 / 8))
    z += 1 / 8
    song = both(song, note(e, z, z + 1 / 8))
    z += 1 / 4
    song = both(song, note(g, z, z + 1 / 4))
    z += 1 / 2
    song = both(song, note(low_g, z, z + 1 / 4))
    return song


def mario_at(octave):
    c = tri(octave * c_freq)
    e = tri(octave * e_freq)
    g = tri(octave * g_freq)
    low_g = tri(octave * g_freq / 2)
    return mario(c, e, g, low_g)


play(both(mario_at(1), mario_at(1 / 2)))
