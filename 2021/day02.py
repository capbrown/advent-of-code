# Advent of Code: Day 2

input_file_name = r'day02.txt'
with open(input_file_name) as f:
	directions = [d.split(' ') for d in f.read().splitlines()]

directions = [[d[0], int(d[1])] for d in directions]

horizontal = 0
depth = 0
for d in directions:
	direction = d[0]
	amount = d[1]
	if direction == 'forward':
		horizontal += amount
	elif direction == 'up':
		depth -= amount
	elif direction == 'down':
		depth += amount
part1 = horizontal * depth
print("Part 1: ", part1)


horizontal = 0
depth = 0
aim = 0
for d in directions:
	direction = d[0]
	amount = d[1]
	if direction == 'forward':
		horizontal += amount 
		depth += amount*aim
	elif direction == 'up':
		aim -= amount
	elif direction == 'down':
		aim += amount
part2 = horizontal * depth
print("Part 2: ", part2)
