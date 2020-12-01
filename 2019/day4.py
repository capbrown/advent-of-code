import numpy as np

test_cases = np.arange(109165, 576723 + 1).T

ns = 576723 + 1 - 109165

checks = np.zeros((ns, 6), dtype=int)

for i in range(ns):
    checks[i, :] = [int(d) for d in str(test_cases[i])]

n = 0
for i in range(ns):
    a = checks[i, :]
    b = np.sort(checks[i, :])
    _, n_uns = np.unique(a, return_counts=True)
    if np.array_equal(a, b) and 2 in n_uns:
        n += 1

print(n)
