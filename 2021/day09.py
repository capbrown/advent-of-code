# Advent of Code: Day 9

import numpy as np
	
def check_neighbours(input_array, j, i):
	limit_j, limit_i = input_array.shape
	neighbours = [(j-1, i), (j, i-1), (j, i+1), (j+1, i)]
	is_greater = []
	for n in neighbours:
		if n[0] < 0 or n[0] > limit_j-1 or n[1] < 0 or n[1] > limit_i-1:
			is_greater.append(True)
		else:
			if input_array[n[0],n[1]] > input_array[j,i] and input_array[j,i] != 9:
				is_greater.append(True)
			else:
				is_greater.append(False)	
	return all(is_greater)
	
def check_neighbours_size(input_array, j, i):
	limit_j, limit_i = input_array.shape
	neighbours = [(j-1, i), (j, i-1), (j, i+1), (j+1, i)]
	is_greater = []
	for n in neighbours:
		if n[0] < 0 or n[0] > limit_j-1 or n[1] < 0 or n[1] > limit_i-1:
			pass
		else:
			if input_array[n[0],n[1]] > input_array[j,i] and input_array[j,i] != 9:
				is_greater.append(n)
	return is_greater

input_file_name = r'day09.txt'
with open(input_file_name) as f:
	lines = [[int(n) for n in list(l)]for l in f.read().splitlines()]

lines = np.asarray(lines)

# Part 1
risk_sum = 0
for j in range(lines.shape[0]):
	for i in range(lines.shape[1]):
		if check_neighbours(lines, j, i):
			risk_sum += lines[j, i] +1
print("Part 1: ", risk_sum)


# Part 2
basin_map = np.zeros(lines.shape)
max_top = 10
lines_copy = np.copy(lines)
for j in range(lines.shape[0]):
	for i in range(lines.shape[1]):
		if check_neighbours(lines, j, i):
			basin_map[j, i] = 1
			lines_copy[j, i] = max_top
			max_top += 1

lines = lines_copy
changed = True
while changed:
	changed = False
	for j in range(lines.shape[0]):
		for i in range(lines.shape[1]):
			if lines[j, i] != 9:
				bigger = check_neighbours_size(lines, j, i)
				for b in bigger:
					if lines[b[0], b[1]] > 9:
						basin_map[j, i] = 1
						lines[j, i] = lines[b[0], b[1]]
						changed = True
	
basin_map = np.array(basin_map, dtype=bool)
clusters = lines[basin_map]
ns, counts = np.unique(clusters, return_counts=True)
counts = np.delete(counts,np.nonzero(ns <= 9))
counts = np.sort(counts)
print(np.product(counts[-3:]))
