# Advent of Code: Day 7

import numpy as np

input_file_name = r'day07.txt'
state = np.genfromtxt(input_file_name, delimiter=',', dtype='int')

fuel = np.zeros(len(state)+1)

for i in range(len(fuel)):
	#fuel[i] += np.sum(np.abs(state-i)) # part 1
	
	fuel[i] += np.sum([sum(range(n+1)) for n in np.abs(state-i)]) # part 2
	
print(np.min(fuel))
