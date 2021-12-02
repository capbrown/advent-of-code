# Advent of Code: Day 1

def n_greater_than_previous(depth_list):
	"""Compute the number of times an entry
	is greater than the previous entry."""
	n_times = 0
	for i in range(1, len(depth_list)):
		if depth_list[i] > depth_list[i-1]:
			n_times += 1
	return n_times

input_file_name = r'day01.txt'
with open(input_file_name) as f:
	depths = [int(n) for n in f.read().splitlines()]
	
print("Part 1: ", n_greater_than_previous(depths))

# Compute sliding window
window_size = 3
sliding_window_sums = []
for i in range(window_size-1, len(depths)):
	sliding_window_sums.append(sum(depths[i-(window_size-1):i+1]))

print("Part 2: ", n_greater_than_previous(sliding_window_sums))
