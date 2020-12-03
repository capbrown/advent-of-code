# Advent of Code Day 3


def day03(lines, right, down):
	input_width = len(lines[0])
	input_height = len(lines)
	horizontal_coordinate = 0
	vertical_coordinate = 0
	n_trees = 0
	while vertical_coordinate < input_height:
		line = lines[vertical_coordinate]
		if line[horizontal_coordinate % input_width] == '#':
			n_trees += 1
		horizontal_coordinate += right
		vertical_coordinate += down
	return n_trees

	
if __name__ == "__main__":
	input_file = 'input03.txt'
	with open(input_file) as f:
		lines = f.read().splitlines()
	
	# Part One
	print(day03(lines, 3, 1))
	
	# Part Two
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	product = 1
	for slope in slopes:
		product *= day03(lines, *slope)
	print(product)