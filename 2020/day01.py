import itertools
import numpy as np
from datetime import datetime


# Advent of Code Day 1


def day01(input_file_name, n):
    with open(input_file_name) as f:
        input01 = [int(n) for n in f.read().splitlines()]
        for a in itertools.combinations(input01, n):
            if sum(a) == 2020:
                return np.prod(a)


if __name__ == '__main__':
    input_file = 'inputs/input01.txt'

    # Part One
    print(day01(input_file, 2))

    # Part Two
    print(day01(input_file, 3))

