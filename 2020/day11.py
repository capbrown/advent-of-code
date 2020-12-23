# Advent of Code Day 11

import numpy as np


def get_n_adjacent(grid, i, j):
    adjacent_is = [(i-1, j), (i, j-1), (i-1, j-1), (i+1, j), (i, j+1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]

    # get is within bounds i.e. edge checking
    valids = []
    for inds in adjacent_is:
        if inds[0] >= 0 and inds[1] >= 0 and inds[0] < grid.shape[0] and inds[1] < grid.shape[1]:
            valids.append(inds)
    n_a = 0
    for inds in valids:
        if grid[inds[0], inds[1]] == 2:
            n_a += 1
    return n_a


if __name__ == "__main__":
    with open("inputs/input11.txt") as f:
        lines = f.read().splitlines()

    # convert to numpy array
    height = len(lines)
    width = len(lines[0])

    seat_grid = np.zeros((height, width), dtype=int)
    for i in range(height):
        line = lines[i]
        for j in range(width):
            c = line[j]
            if c == 'L':
                seat_grid[i, j] = 1
            else:
                seat_grid[i, j] = 0

    changed = True
    while changed:
        temp = np.copy(seat_grid)
        changed = False
        for i in range(height):
            for j in range(width):  # too many loops. map that
                if seat_grid[i, j] != 0:
                    n = get_n_adjacent(seat_grid, i, j)
                    if n == 0 and seat_grid[i, j] == 1:
                        temp[i, j] = 2
                        changed = True
                    elif n >= 4 and seat_grid[i, j] == 2:
                        temp[i, j] = 1
                        changed = True
        seat_grid = temp

    print(np.unique(seat_grid, return_counts=True))
