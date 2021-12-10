# Advent of Code: Day 10

input_file_name = r'day10.txt'
with open(input_file_name) as f:
	lines = f.read().splitlines()

matches = {')': '(', ']': '[', '}': '{', '>': '<'}
incomplete_chars = []
corrupt_chars = []
for line in lines:
	bracket_stack = []
	corrupted = False
	for c in line:
		if c in '([{<':
			bracket_stack.append(c)
		elif c in ')]}>':
			if bracket_stack.pop() != matches[c]:
				corrupt_chars.append(c)
				corrupted = True
				break
	if not corrupted:
		incomplete_chars.append(bracket_stack)

# Part 1
error_score = corrupt_chars.count(')') * 3
error_score += corrupt_chars.count(']') * 57
error_score += corrupt_chars.count('}') * 1197
error_score += corrupt_chars.count('>') * 25137
print(error_score)

# Part 2
scores = {'(': 1, '[': 2, '{': 3, '<': 4}
line_scores = []
for line in incomplete_chars:
	line.reverse()
	score = 0
	for c in line:
		score *= 5
		score += scores[c]
	line_scores.append(score)
line_scores.sort()
print(line_scores[(len(line_scores)-1)//2])
