import numpy

from lib.decorators import timer

__all__ = ['slow', 'fast', 'faster']

"""
    Sum the numbers from 0 to n-1.
"""


@timer
def slow():
    i = 0
    sum = 0
    while(i < 100_000_000):
        sum += i
        i += 1

    return sum


@timer
def fast():
    sum = 0
    for i in range(100_000_000):
        sum += i

    return sum


@timer
def faster():
    sum = numpy.sum(numpy.arange(100_000_000))
    return sum
