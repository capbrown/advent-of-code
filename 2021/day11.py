# Advent of Code: Day 11

import numpy as np

def flash(octopi, j, i):
	limit_j, limit_i = octopi.shape
	neighbours = [(j-1,i), (j,i-1), (j,i+1), (j+1,i), (j-1,i-1), (j-1,i+1), (j+1,i+1), (j+1,i-1)]
	neighbours = [n for n in neighbours if n[0] >= 0 and n[0] <= limit_j-1 and n[1] >= 0 and n[1] <= limit_i-1]
	return neighbours

lines = '''2682551651
3223134263
5848471412
7438334862
8731321573
6415233574
5564726843
6683456445
8582346112
4617588236'''.splitlines()

lines = [[int(c) for c in line] for line in lines]

octopi = np.asarray(lines)
print(octopi)

time_steps = 1000

flash_count = 0

for i in range(time_steps):
	octopi += 1
	flashed = np.nonzero(octopi > 9)
	flash_ready = np.nonzero(octopi > 9)
	flashed = list(zip(flash_ready[0], flash_ready[1]))
	octopi[flash_ready] = 0
	flash_count += flash_ready[0].size
	while flash_ready[0].size: # oh boy
		all_neighbours = []
		for z in zip(flash_ready[0], flash_ready[1]):
			all_neighbours.append(flash(octopi, z[0], z[1]))
		all_neighbours = [item for sublist in all_neighbours for item in sublist]
		for n in all_neighbours:
			octopi[n[0],n[1]] += 1
		flash_ready = np.nonzero(octopi > 9)
		flash_count += flash_ready[0].size
		octopi[flash_ready] = 0
		for zz in zip(flash_ready[0], flash_ready[1]):
			flashed.append(zz)
	for nn in flashed:
		octopi[nn] = 0
	n_zeros = octopi == 0
	if n_zeros.all():
		print("All flashed at: ", i+1)
		break

print(flash_count)
