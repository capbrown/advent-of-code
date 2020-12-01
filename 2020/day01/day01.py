import itertools
import numpy as np
import sys

# Advent of Code Day 1


def day01_a(input_file_name, n):
    with open(input_file_name) as f:
        input01 = [int(n) for n in f.read().splitlines()]
        for a in itertools.combinations(input01, n):
            if sum(a) == 2020:
                return np.prod(a)


# Need to refactor version B to work with Part Two
def day01_b(input_file_name):
    with open(input_file_name) as f:
        pos = 0
        while True:
            f.seek(pos)
            current = f.readline()
            pos += len(current) + 1  # 1 for newline char
            for next_line in f:
                a = int(current)
                b = int(next_line)
                if a + b == 2020:
                    return a * b


if __name__ == '__main__':
    input_file = 'input01.txt'

    # Part One
    print(day01_a(input_file, 2))

    # Part Two
    print(day01_a(input_file, 3))
