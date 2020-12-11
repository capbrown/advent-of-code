# Advent of Code Day 9

import itertools


def is_sum(n, list_to_check):
	combs = list(itertools.combinations(list_to_check, 2))
	combs = [sum(p) for p in combs]
	return n in combs

	
if __name__ == "__main__":

	with open("input09.txt") as f:
		lines = f.read().splitlines()
	lines = [int(n) for n in lines]

	# Part One
	block_size = 25
	window = lines[:block_size]
	remainder = lines[block_size:]
	invalid_number = -1
	for n in remainder:
		if not is_sum(n, window):
			invalid_number = n
			break
		window = window[1:] + [n]	
	print(invalid_number)
	
	# Part Two
	for i in range(len(lines)):
		n = lines[i]
		block = [n]
		next = i
		if n != invalid_number:
			while sum(block) <= invalid_number:
				if sum(block) == invalid_number:
					print(min(block)+max(block))
					break
				else:
					next += 1
					block = block + [lines[next]]
