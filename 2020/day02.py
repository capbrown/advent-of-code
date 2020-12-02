# Advent of Code Day 2



# Part One
def day02_1(lines):
	n_valid = 0
	for line in lines:
		lower, upper, letter, password = tokenize(line)
		n_occurances_letter = int(password.count(letter))
		if n_occurances_letter in range(lower, upper + 1):
			n_valid += 1
	return n_valid


# Part Two
def day02_2(lines):
	n_valid = 0
	for line in lines:
		lower, upper, letter, password = tokenize(line)
		if (password[lower-1] == letter) != (password[upper-1] == letter):
			n_valid += 1
	return n_valid

	
def tokenize(line):
	tokens = line.split()
	lower, upper = [int(n) for n in tokens[0].split('-')]
	letter = tokens[1][0]
	password = tokens[2]
	return lower, upper, letter, password
	
	
if __name__ == "__main__":
	input02_file = 'input02.txt'
	with open(input02_file) as f:
		lines = f.read().splitlines()
	
	print(day02_1(lines)
	print(day02_2(lines)
