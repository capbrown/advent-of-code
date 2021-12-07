# Advent of Code: Day 6

import numpy as np

input_file_name = r'day06.txt'
state = np.genfromtxt(input_file_name, delimiter=',', dtype='int')

n_days = 256

days, day_counts = np.unique(state, return_counts=True)

population = np.zeros(9)
population[days] = day_counts

for i in range(1,n_days+1):
	n_zeros = population[0]
	population = np.roll(population, shift=-1)
	population[-1] = n_zeros
	population[6] += n_zeros
	
print(np.sum(population))
