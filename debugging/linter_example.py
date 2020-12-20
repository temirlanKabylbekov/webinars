import itertools
import math


def circle_area(radius: float) -> float:
    return math.pi * radius ** 2


def combinations_of_fixed_length(data, length):
    return itertools.combinations(data, length)
