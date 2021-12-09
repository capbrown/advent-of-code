# Advent of Code: Day 8

import numpy as np
	
def remove_letters(word, letters_to_remove):
	for c in letters_to_remove:
		word = word.replace(c,'')
	return word
	
def all_a_in_b(a, b):
	if all([c in b for c in a]):
		return True
	return False

input_file_name = r'day08.txt'
with open(input_file_name) as f:
	lines = [l.split(' ') for l in f.read().splitlines()]

final_sum = 0
for line in lines:
	decoded = [None]*10
	input_digits = line[:10]
	output_digits = line[11:]
	
	for word in input_digits:
		if len(word) == 2:
			decoded[1] = word
		if len(word) == 4:
			decoded[4] = word
		if len(word) == 3:
			decoded[7] = word
		if len(word) == 7:
			decoded[8] = word
	
	input_digits = [i for i in input_digits if i not in decoded]
	
	top = remove_letters(decoded[7], decoded[1])
	
	for word in input_digits:
		if all_a_in_b(decoded[4], word):
			decoded[9] = word
			input_digits.remove(word)
			break
			
	# now we know: 1,4,7,8,9
	
	# with the 9 found, can find bottom left label with 8 - 9
	for c in decoded[8]:
		if c not in decoded[9]:
			bottom_left = c
	
	# we can find the bottom by removing top and 4 from 9
	bottom = remove_letters(decoded[9], decoded[4] + top)
	
	# find 3 and 0
	for word in input_digits:
		if all_a_in_b(top+bottom+decoded[1], word):
			if len(word) == 5:
				decoded[3] = word
				middle = remove_letters(word,top+bottom+decoded[1])
			if len(word) == 6:
				decoded[0] = word
	input_digits.remove(decoded[0])
	input_digits.remove(decoded[3])
	
	# find top left by removing middle and 1 from 4
	top_left = remove_letters(decoded[4], decoded[1] + middle)
	
	# find 6
	for word in input_digits:
		if len(word) == 6:
			decoded[6] = word
			input_digits.remove(decoded[6])
	
	bottom_right = remove_letters(decoded[6],top+bottom+middle+bottom_left+top_left)
	top_right = remove_letters(decoded[1],bottom_right)
	
	decoded[2] = top + top_right + middle + bottom_left + bottom
	decoded[5] = top + top_left + middle + bottom_right + bottom
	
	# found all the segments, so decode
	output_number = ''
	for word in output_digits:
		for i, decode in enumerate(decoded):
			if all_a_in_b(word, decode) and len(decode) == len(word):
				output_number += str(i)
				break
	
	final_sum += int(output_number)
	
print(final_sum)
