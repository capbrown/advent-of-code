# Advent of Code: Day 5

import numpy as np

input_file_name = r'day05.txt'
with open(input_file_name) as f:
	lines = f.read().splitlines()

board = np.zeros((1000,1000))

for line in lines:
	groups = line.split(' -> ')
	x1, y1 = [int(n) for n in groups[0].split(',')]
	x2, y2 = [int(n) for n in groups[1].split(',')]
	
	if x1 == x2 or y1 == y2: # part 1
		board[min([y1,y2]):max([y1,y2])+1, min([x1,x2]):max([x1,x2])+1] +=  1
	else: # part 2
		inds = list(zip(np.linspace(y1,y2,abs(y1-y2)+1), np.linspace(x1,x2,abs(x1-x2)+1)))
		for ind in inds:
			ind = tuple([int(n) for n in ind])
			board[ind] = board[ind] + 1

intersections = board[np.nonzero(board > 1)]
print(len(intersections))
