# Advent of Code Day 10

import functools
import itertools
import numpy as np
from operator import mul

if __name__ == "__main__":
    with open("input10.txt") as f:
        lines = f.read().splitlines()
    lines = [int(n) for n in lines]
    lines = [0] + lines + [max(lines) + 3]
    lines = np.array(lines)
    lines = np.sort(lines)

    # Part One
    diffs = np.diff(lines)
    n_1 = np.count_nonzero(diffs == 1)
    n_3 = np.count_nonzero(diffs == 3)
    print(n_1*n_3)

    # Part Two
    answer = []
    lines = diffs.tolist()
    for key, consecutives in itertools.groupby(lines):
        ls = len(list(consecutives))
        if key != 3 and ls != 1:
            answer.append(ls)

    a = [3*n-5 if n > 2 else 2 for n in answer]
    print(functools.reduce(mul, a, 1))
