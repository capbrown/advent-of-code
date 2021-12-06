# Advent of Code: Day 4
import numpy as np

def find_winners(call_order, all_boards):
	winners = []
	for call in call_order:
		for i, current_board in enumerate(all_boards):
			current_board[np.nonzero(current_board == float(call))] = -1
			
			# check for bingo
			horsum = np.sum(current_board, axis=0)
			versum = np.sum(current_board, axis=1)
			
			sum_of_unmarked = np.sum(current_board[np.nonzero(current_board >= 0)])
			
			if -5.0 in horsum or -5.0 in versum:
				winners.append(i+1)
				#return call * sum_of_unmarked # first winning score for part 1
			
			if len(set(winners)) == len(all_boards):
				return call * sum_of_unmarked

input_file_name = r'day04.txt'
with open(input_file_name) as f:
	codes = f.read().splitlines()

call_order = [int(n) for n in codes[0].split(',')]

raw_boards = np.loadtxt(input_file_name,skiprows=1)
all_boards = np.array_split(raw_boards, raw_boards.shape[0]/5)

print(find_winners(call_order,all_boards))
