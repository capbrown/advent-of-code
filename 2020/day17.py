import numpy as np
import itertools


def get_adjacent_indices(i):
    x_ = np.linspace(i[0] - 1, i[0] + 1, 3, dtype=int).tolist()

    y_ = np.linspace(i[1] - 1, i[1] + 1, 3, dtype=int).tolist()
    z_ = np.linspace(i[2] - 1, i[2] + 1, 3, dtype=int).tolist()
    print(x_, y_, z_)
    z = list(itertools.product(x_, y_, z_))
    z.remove(i)
    return [el for el in z if all(i > 0 for i in el)]

initial_state = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])



middle = n / 2
b = np.zeros((n, n, n), dtype=int)

b[middle, middle - 1:middle + 2, middle - 1:middle + 2] = initial_state

n_cycles = 6
for _ in range(n_cycles):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                current_index = (i, j, k)
                adjs = get_adjacent_indices(current_index)