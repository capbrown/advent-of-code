# Advent of Code: Day 3

def most_in_position(codes, use_most_common, part1=False, position=0):
	
	threshold = len(codes)/2 # whether 1s are the majority
	
	if len(codes) == 1: # base case for recursion
		return ''.join(map(str,codes[0]))
	
	base = [0]*len(codes[0])
	
	# the number of 1s in each position
	for c in codes:
		for i in range(len(c)):
			base[i] = base[i] + c[i]
	
	gamma = ''
	epsilon = ''
	for n in base:
		if n > threshold: # if there are more 1s
			if use_most_common:
				gamma += '1'
			else:
				gamma += '0'
		elif n == threshold:
			if use_most_common:
				gamma += '1'
			else:
				gamma += '0'
		else:
			if use_most_common:
				gamma += '0'
			else:
				gamma += '1'	
	if part1:
		return gamma
		
	majority_value = int(gamma[position])
	filtered_codes = [line for line in codes if line[position] == majority_value]
	return most_in_position(filtered_codes, use_most_common, part1, position+1)
	

input_file_name = r'day03.txt'
with open(input_file_name) as f:
	codes = [list(c) for c in f.read().splitlines()]
	codes = [[int(n) for n in c] for c in codes]

gamma = most_in_position(codes, True, True)
epsilon = most_in_position(codes, False, True)
print('Part 1: ', int(gamma, 2) * int(epsilon, 2))

oxygen_generator = most_in_position(codes, True)
co2_scrubber = most_in_position(codes, False)
print('Part 2: ', int(oxygen_generator, 2) * int(co2_scrubber, 2))
